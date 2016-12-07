# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore, QtGui
from sap_ui import Ui_sap
from sql_driver import SQL_driver
from sap_data import SAP_data

class SAP_main(QtGui.QMainWindow):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_sap()
        self.ui.setupUi(self)
        
        self.mysql= SQL_driver()
        self.mydata=SAP_data()
        
        self.mysql.delete_default()
        
        self.refresh_databases()
        self.tab_ability(False)
        
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate ())
        
        self.cari_disable()
        self.ui.txtCariDeskrip.setEnabled(True)
        self.edit_ability(False)
        
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.actionAbout_triggered)
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.actionExit_triggered)
        QtCore.QObject.connect(self.ui.actionMain_Data_as_Table, QtCore.SIGNAL("triggered()"), self.actionMain_Data_as_Table_triggered)
        QtCore.QObject.connect(self.ui.actionMain_Data_as_PDF, QtCore.SIGNAL("triggered()"), self.actionMain_Data_as_PDF_triggered)
        QtCore.QObject.connect(self.ui.btnDbExisting, QtCore.SIGNAL("clicked()"), self.btnDbExisting_clicked)
        QtCore.QObject.connect(self.ui.btnDbNew, QtCore.SIGNAL("clicked()"), self.btnDbNew_clicked)
        QtCore.QObject.connect(self.ui.btnDbDelete, QtCore.SIGNAL("clicked()"), self.btnDbDelete_clicked)
        
    def actionAbout_triggered(self):
        self.msg_about()
        
    def actionExit_triggered(self):
        QtGui.QApplication.quit()
        
    def actionMain_Data_as_Table_triggered(self):
        self.mydata.view_table(self.ui.cmbDbExisting.currentText())
        
    def actionMain_Data_as_PDF_triggered(self):
        pass
#        self.mydata.view_pdf(self.ui.cmbDbExisting.currentText())
        
    def btnDbExisting_clicked(self):
        if self.ui.cmbDbExisting.currentText()=="information_schema": 
            msg = QtGui.QMessageBox(self)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Database Terlarang")
            msg.setText("silahkan pilih database lain atau buat baru")
            msg.show()
            return
            
        if self.ui.cmbDbExisting.currentText().isEmpty():
            msg = QtGui.QMessageBox(self)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Database Tidak ada")
            msg.setText("Nama Database tidak ada")
            msg.show()
            return
            
        if self.ui.btnDbExisting.text()=="Use":
            self.tab_ability(True)
            self.ui.cmbDbExisting.setEnabled(False)
            self.ui.btnDbExisting.setText("Unuse")
        elif self.ui.btnDbExisting.text()=="Unuse":
            self.tab_ability(False)
            self.ui.cmbDbExisting.setEnabled(True)
            self.ui.btnDbExisting.setText("Use")
            
    def btnDbNew_clicked(self):
        namadb = QtCore.QString()
        namadb = self.ui.txtDbNew.text()
        self.mysql.create_database(namadb)
        self.mysql.create_table(namadb)
        self.refresh_databases()
        
        msg = QtGui.QMessageBox(self)
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setWindowTitle("Sudah tercipta")
        msg.setText("Data " + namadb + " tercipta !!")
        msg.show()
        
    def btnDbDelete_clicked(self):
        namadb=QtCore.QString()
        namadb=self.ui.cmbDbDelete.currentText()
        
        if namadb=="information_schema":
            msg = QtGui.QMessageBox(self)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setWindowTitle("Database Terlarang")
            msg.setText("silahkan pilih database lain atau buat baru")
            msg.show()
            return
            
        msg = QtGui.QMessageBox(self)
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle("Yakin?")
        msg.setText("yakin akan mnghapus data " + namadb + " selamanya ?!!")
        retval = msg.exec_()
        if retval == QtGui.QMessageBox.Ok:
            self.mysql.delete_database(namadb)
            self.refresh_databases()
            
            msg = QtGui.QMessageBox(self)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setWindowTitle("Terhapus Selamanya")
            msg.setText("Data " + namadb + " selamanya !!")
            msg.show()
            
#======================================================================================================

    def msg_about(self):
        qtver=QtCore.QString()
        qtver+= QtCore.QT_VERSION_STR
         
        mysqlver=QtCore.QString()
        mysqlver= self.mysql.procSqlVersion()
         
        aboutmsg=QtCore.QString()
        aboutmsg += "Simple Accounting Program \n"
        aboutmsg += "\n"
        aboutmsg += "Credit: \n"
        aboutmsg += "Accounting Scheme written by Hilmi F. \n"
        aboutmsg += "GUI Program written by Achmadi \n"
        aboutmsg += "\n"
        aboutmsg += "Using: \n"
        aboutmsg += "Qt version " + qtver + "\n"
        aboutmsg += "MySQL version " + mysqlver
        
        if platform.system() == "Linux":
            bashver = QtCore.QString()
            bashver = self.mysql.procCmdVersion()
            aboutmsg += "Bash version " + bashver
            
            bashver = QtCore.QString()
            osver = self.mysql.procOsVersion()
            aboutmsg += "Linux version " + osver
            
        elif platform.system() == "Windows":
            osver=QtCore.QString()
            osver = self.mysql.procOsVersion()
            aboutmsg += "OS version " + osver
            
        aboutmsg += "\n"
        
        msg = QtGui.QMessageBox(self)
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setWindowTitle("About Me")
        msg.setText(aboutmsg)
        msg.show()
        
    def refresh_databases(self):
        self.ui.cmbDbDelete.clear()
        self.ui.cmbDbDelete.insertItems(0,self.mysql.list_database())

        self.ui.cmbDbExisting.clear()
        self.ui.cmbDbExisting.insertItems(0,self.mysql.list_database())

        self.ui.cmbDbExport.clear()
        self.ui.cmbDbExport.insertItems(0,self.mysql.list_database())

        self.ui.cmbDbImport.clear()
        self.ui.cmbDbImport.insertItems(0,self.mysql.list_database())
        
    def tab_ability(self, ability):
        self.ui.tabMain.setTabEnabled(1,ability)
        self.ui.tabMain.setTabEnabled(2,ability)
        self.ui.tabMain.setTabEnabled(3,ability)
        self.ui.actionMain_Data_as_Table.setEnabled(ability)
        self.ui.actionMain_Data_as_PDF.setEnabled(ability)
        
    def cmb_jenis(self):
        jenis=QtCore.QStringList()
        jenis.append("PEMBELIAN BAHAN BAKU TUNAI")
        jenis.append("PEMBELIAN BAHAN BAKU KREDIT")
        jenis.append("RETUR PEMBELIAN TUNAI")
        jenis.append("RETUR PEMBELIAN KREDIT")
        jenis.append("PENJUALAN TUNAI")
        jenis.append("PENJUALAN KREDIT")
        jenis.append("RETUR PENJUALAN TUNAI")
        jenis.append("RETUR PENJUALAN KREDIT")
        jenis.append("PEMBAYARAN GAJI")
        jenis.append("PEMBAYARAN TELP, AIR & LISTRIK")
        jenis.append("PEMBAYARAN UTANG MELALUI KAS DI TANGAN")
        jenis.append("PEMBAYARAN TRANSPORTASI")
        jenis.append("DISETOR MODAL TUNAI")
        jenis.append("PENYETORAN TUNAI KE BANK")
        jenis.append("PINJAMAN DARI BANK")
        jenis.append("PEMBAYARAN UTANG MELALUI BANK")
        jenis.append("DITERIMA PEMBAYARAN PIUTANG")
        jenis.append("DIBELI PERALATAN")
        jenis.append("DEPRESIASI PERALATAN")
        jenis.append("SEWA BANGUNAN DIBAYAR DIMUKA")
        jenis.append("PEMBAYARAN SEWA BANGUNAN")
        jenis.append("BEBAN GARANSI ESTIMASI")
        jenis.append("BEBAN GARANSI REALISASI")
        jenis.append("BEBAN GARANSI TAK TEREALISASI")
        
        self.ui.cmbTrsJenis.clear()
        self.ui.cmbTrsJenis.insertItems(0,jenis)

        self.ui.cmbEditJenis.clear()
        self.ui.cmbEditJenis.insertItems(0,jenis)

        self.ui.cmbCariJenis.clear()
        self.ui.cmbCariJenis.insertItems(0,jenis)
        
    def cmb_debet(self):
        debet=QtCore.QStringList()
        debet.append("PEMBELIAN")
        debet.append("KAS DI TANGAN")
        debet.append("UTANG USAHA")
        debet.append("PIUTANG USAHA")
        debet.append("RETUR PENJUALAN")
        debet.append("BEBAN GAJI")
        debet.append("BEBAN TELP, AIR & LISTRIK")
        debet.append("BEBAN TRANSPORTASI")
        debet.append("KAS DI BANK")
        debet.append("PERALATAN")
        debet.append("BEBAN PENYUSUTAN PERALATAN")
        debet.append("SEWA BANGUNAN DI BAYAR DIMUKA")
        debet.append("BEBAN SEWA BANGUNAN")
        debet.append("BEBAN GARANSI")
        debet.append("CADANGAN GARANSI")
        
        self.ui.cmbCariDebet.clear()
        self.ui.cmbCariDebet.insertItems(0,debet)
        
    def cmb_kredit(self):
        kredit=QtCore.QStringList()
        kredit.append("KAS DI TANGAN")
        kredit.append("UTANG USAHA")
        kredit.append("RETUR PEMBELIAN")
        kredit.append("PENJUALAN")
        kredit.append("PIUTANG USAHA")
        kredit.append("MODAL PEMILIK")
        kredit.append("KAS DI BANK")
        kredit.append("AKUMULASI PENYUSUTAN PERALATAN")
        kredit.append("SEWA BANGUNAN DIBAYAR DI MUKA")
        kredit.append("CADANGAN GARANSI")
        
        self.ui.cmbCariKredit.clear()
        self.ui.cmbCariKredit.insertItems(0,kredit)
        
    def cari_disable(self):
        self.ui.txtCariDeskrip.setEnabled(False)
        self.ui.txtCariNilai.setEnabled(False)
        self.ui.cmbCariJenis.setEnabled(False)
        self.ui.cmbCariDebet.setEnabled(False)
        self.ui.cmbCariKredit.setEnabled(False)
        self.ui.dateCariTanggal.setEnabled(False)
        self.ui.btnCariNow.setEnabled(False)
        
    def app_cari_data(self):
        if self.ui.rbtCariDeskrip.isChecked():self.mydata.view_search(self.ui.cmbDbExisting.currentText(),"transaksi",self.ui.txtCariDeskrip.text())
        if self.ui.rbtCariNilai.isChecked():self.mydata.view_search(self.ui.cmbDbExisting.currentText(),"harga",self.ui.txtCariNilai.text())
        if self.ui.rbtCariJenis.isChecked():self.mydata.view_search(self.ui.cmbDbExisting.currentText(),"jenis",QtCore.QString.number(self.ui.cmbCariJenis.currentIndex()))
        if self.ui.rbtCariDebet.isChecked():self.mydata.view_search(self.ui.cmbDbExisting.currentText(),"debet",QtCore.QString.number(self.ui.cmbCariDebet.currentIndex()))
        if self.ui.rbtCariKredit.isChecked():self.mydata.view_search(self.ui.cmbDbExisting.currentText(),"kredit",QtCore.QString.number(self.ui.cmbCariKredit.currentIndex()))
        if self.ui.rbtCariTanggal.isChecked():self.mydata.view_search(self.ui.cmbDbExisting.currentText(),"tanggal",self.ui.dateCariTanggal.text())
        
    def show_one_data(self, dataid):
        self.ui.txtEditDeskrip.setText(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"transaksi",dataid))
        self.ui.txtEditNilai.setText(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"harga",dataid))
        self.ui.cmbEditJenis.setCurrentIndex(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"jenis",dataid).toInt())
        self.ui.dateEditTanggal.setDate(QtCore.QDate.fromString(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"tanggal",dataid),"yyyy-MM-dd"))
        
    def edit_ability(self,  ability):
        self.ui.txtEditDeskrip.setEnabled(ability)
        self.ui.txtEditNilai.setEnabled(ability)
        self.ui.cmbEditJenis.setEnabled(ability)
        self.ui.dateEditTanggal.setEnabled(ability)

        self.ui.btnEditNow.setEnabled(ability)
        self.ui.btnEditChange.setEnabled(ability)
        self.ui.btnEditDelete.setEnabled(ability)
