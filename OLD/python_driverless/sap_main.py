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
        
        self.refresh_databases()
        self.tab_ability(False)
        
        self.cmb_jenis()
        self.cmb_debet()
        self.cmb_kredit()
        
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate ())
        
        self.cari_disable()
        self.ui.txtCariDeskrip.setEnabled(True)
        self.edit_ability(False)
        
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.actionAbout_triggered)
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.actionExit_triggered)
        QtCore.QObject.connect(self.ui.actionMain_Data_as_Table, QtCore.SIGNAL("triggered()"), self.actionMain_Data_as_Table_triggered)
        QtCore.QObject.connect(self.ui.actionMain_Data_as_CSV, QtCore.SIGNAL("triggered()"), self.actionMain_Data_as_CSV_triggered)
        
        QtCore.QObject.connect(self.ui.btnDbExisting, QtCore.SIGNAL("clicked()"), self.btnDbExisting_clicked)
        QtCore.QObject.connect(self.ui.btnDbNew, QtCore.SIGNAL("clicked()"), self.btnDbNew_clicked)
        QtCore.QObject.connect(self.ui.btnDbDelete, QtCore.SIGNAL("clicked()"), self.btnDbDelete_clicked)
        QtCore.QObject.connect(self.ui.btnDbExport, QtCore.SIGNAL("clicked()"), self.btnDbExport_clicked)
        QtCore.QObject.connect(self.ui.btnDbImport, QtCore.SIGNAL("clicked()"), self.btnDbImport_clicked)
        
        QtCore.QObject.connect(self.ui.btnTrsSave, QtCore.SIGNAL("clicked()"), self.btnTrsSave_clicked)
        QtCore.QObject.connect(self.ui.btnTrsClear, QtCore.SIGNAL("clicked()"), self.btnTrsClear_clicked)
        QtCore.QObject.connect(self.ui.btnTrsNow, QtCore.SIGNAL("clicked()"), self.btnTrsNow_clicked)
        
        QtCore.QObject.connect(self.ui.rbtCariDeskrip, QtCore.SIGNAL("clicked()"), self.rbtCariDeskrip_clicked)
        QtCore.QObject.connect(self.ui.rbtCariNilai, QtCore.SIGNAL("clicked()"), self.rbtCariNilai_clicked)
        QtCore.QObject.connect(self.ui.rbtCariJenis, QtCore.SIGNAL("clicked()"), self.rbtCariJenis_clicked)
        QtCore.QObject.connect(self.ui.rbtCariDebet, QtCore.SIGNAL("clicked()"), self.rbtCariDebet_clicked)
        QtCore.QObject.connect(self.ui.rbtCariKredit, QtCore.SIGNAL("clicked()"), self.rbtCariKredit_clicked)
        QtCore.QObject.connect(self.ui.rbtCariTanggal, QtCore.SIGNAL("clicked()"), self.rbtCariTanggal_clicked)
        QtCore.QObject.connect(self.ui.btnCariClear, QtCore.SIGNAL("clicked()"), self.btnCariClear_clicked)
        QtCore.QObject.connect(self.ui.btnCariNow, QtCore.SIGNAL("clicked()"), self.btnCariNow_clicked)
        QtCore.QObject.connect(self.ui.btnCari, QtCore.SIGNAL("clicked()"), self.btnCari_clicked)
        
        QtCore.QObject.connect(self.ui.btnEditNow, QtCore.SIGNAL("clicked()"), self.btnEditNow_clicked)
        QtCore.QObject.connect(self.ui.btnEditShow, QtCore.SIGNAL("clicked()"), self.btnEditShow_clicked)
        QtCore.QObject.connect(self.ui.btnEditChange, QtCore.SIGNAL("clicked()"), self.btnEditChange_clicked)
        QtCore.QObject.connect(self.ui.btnEditDelete, QtCore.SIGNAL("clicked()"), self.btnEditDelete_clicked)
        
#======================================================================================================
        
    def actionAbout_triggered(self):
        self.msg_about()
        
    def actionExit_triggered(self):
        QtGui.QApplication.quit()
        
    def actionMain_Data_as_Table_triggered(self):
        self.mydata.view_table(self.ui.cmbDbExisting.currentText())
        
    def actionMain_Data_as_CSV_triggered(self):
        self.mydata.print_csv(self.ui.cmbDbExisting.currentText())
        
    def btnDbExisting_clicked(self):
            
        if self.ui.cmbDbExisting.currentText().isEmpty():
            msg = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Database Tidak ada","Nama Database tidak ada",QtGui.QMessageBox.Ok, self )
            msg.show()
            return
            
        if self.ui.btnDbExisting.text()=="Use":
            self.tab_ability(True)
            self.ui.cmbDbExisting.setEnabled(False)
            self.ui.btnDbDelete.setEnabled(False)
            self.ui.cmbDbDelete.setEnabled(False)
            self.ui.btnDbExisting.setText("Unuse")
        elif self.ui.btnDbExisting.text()=="Unuse":
            self.tab_ability(False)
            self.ui.cmbDbExisting.setEnabled(True)
            self.ui.btnDbDelete.setEnabled(True)
            self.ui.cmbDbDelete.setEnabled(True)
            self.ui.btnDbExisting.setText("Use")
            
    def btnDbNew_clicked(self):
        namadb = self.ui.txtDbNew.text()
        
        if namadb ==  "performance_schema" or namadb ==  "mysql" or namadb ==  "test" or namadb ==  "information_schema":
            msg = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Nama terlarang","Nama database \"" + namadb + "\" dilarang digunakan.\nSilahkan pilih nama lain !!",QtGui.QMessageBox.Ok, self )
            msg.show()
            return
        
        self.mysql.create_database(namadb)
        self.mysql.create_table(namadb)
        self.refresh_databases()
        
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Information,"Sudah tercipta","Data " + namadb + " tercipta !!",QtGui.QMessageBox.Ok, self )
        msg.show()
        
    def btnDbDelete_clicked(self):
        namadb=self.ui.cmbDbDelete.currentText()
            
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Warning,"Yakin?", "yakin akan mnghapus data " + namadb + " selamanya ?!!",QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, self )
        retval = msg.exec_()
        if retval == QtGui.QMessageBox.Ok:
            self.mysql.delete_database(namadb)
            self.refresh_databases()
            
            msg = QtGui.QMessageBox(QtGui.QMessageBox.Information,"Terhapus Selamanya","Data " + namadb + " selamanya !!",QtGui.QMessageBox.Ok, self )
            msg.show()
            
    def btnDbExport_clicked(self):
        namadb=self.ui.cmbDbExport.currentText()

        fileName=QtGui.QFileDialog.getSaveFileName(None,"Export Database",QtCore.QString(),"*.sql")
        if fileName.isEmpty():
            return
        if QtCore.QFileInfo(fileName).suffix().isEmpty():
            fileName.append(".sql")
            
        self.mysql.export_database(namadb, fileName)
        
    def btnDbImport_clicked(self):
        namadb=self.ui.cmbDbImport.currentText()
            
        fileName=QtGui.QFileDialog.getOpenFileName(self,"Import Data", QtCore.QString(), "*.sql")
        if fileName.isEmpty():
            return
        
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Warning,"Yakin?", "seluruh isi data " + namadb + " akan ditimpa data baru, lanjutkan ?!!",QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, self )
        retval = msg.exec_()
        if retval == QtGui.QMessageBox.Ok:
            self.mysql.import_database(namadb,fileName)
            
    def btnTrsSave_clicked(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strTgl=self.ui.dateTrsTanggal.text()
        strDesk=self.ui.txtTrsDeskrip.text()
        strNilai=self.ui.txtTrsNilai.text()
        intJenis=self.ui.cmbTrsJenis.currentIndex()
        strDebet=self.mydata.jenis2debet(intJenis)
        strKredit=self.mydata.jenis2kredit(intJenis)
        
        self.mysql.data_insert(namadb, strTgl, strDesk, strNilai, intJenis, strDebet, strKredit)
        self.ui.txtTrsDeskrip.clear()
        self.ui.txtTrsNilai.clear()
        self.ui.cmbTrsJenis.setCurrentIndex(0)
        
    def btnTrsClear_clicked(self):
        self.ui.txtTrsDeskrip.clear()
        self.ui.txtTrsNilai.clear()
        self.ui.cmbTrsJenis.setCurrentIndex(0)
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
    
    def btnTrsNow_clicked(self):
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        
    def rbtCariDeskrip_clicked(self):
        self.cari_disable()
        self.ui.txtCariDeskrip.setEnabled(True)
        
    def rbtCariNilai_clicked(self):
        self.cari_disable()
        self.ui.txtCariNilai.setEnabled(True)
        
    def rbtCariJenis_clicked(self):
        self.cari_disable()
        self.ui.cmbCariJenis.setEnabled(True)
        
    def rbtCariDebet_clicked(self):
        self.cari_disable()
        self.ui.cmbCariDebet.setEnabled(True)
        
    def rbtCariKredit_clicked(self):
        self.cari_disable()
        self.ui.cmbCariKredit.setEnabled(True)
        
    def rbtCariTanggal_clicked(self):
        self.cari_disable()
        self.ui.dateCariTanggal.setEnabled(True)
        self.ui.btnCariNow.setEnabled(True)
        
    def btnCariClear_clicked(self):
        self.ui.txtCariDeskrip.clear()
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate())
        self.ui.txtCariNilai.clear()
        self.ui.cmbCariJenis.setCurrentIndex(0)
        self.ui.cmbCariDebet.setCurrentIndex(0)
        self.ui.cmbCariKredit.setCurrentIndex(0)
    
    def btnCariNow_clicked(self):
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate())
        
    def btnCari_clicked(self):
        self.cari_data()
        
    def btnEditNow_clicked(self):
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate())
        
    def btnEditShow_clicked(self):
        txtID=self.ui.txtEditID.text()
        self.show_one_data(txtID)
        
        self.edit_ability(True)
        self.ui.btnEditShow.setEnabled(False)
        self.ui.txtEditID.setEnabled(False)
        
    def btnEditChange_clicked(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strID=self.ui.txtEditID.text()
        strTgl=self.ui.dateEditTanggal.text()
        strDesk=self.ui.txtEditDeskrip.text()
        strNilai=self.ui.txtEditNilai.text()
        intJenis=self.ui.cmbEditJenis.currentIndex()
        strDebet=self.mydata.jenis2debet(intJenis)
        strKredit=self.mydata.jenis2kredit(intJenis)
        
        self.mysql.data_update(namadb, strID, strTgl, strDesk, strNilai, intJenis, strDebet, strKredit)
        
        self.ui.txtEditID.clear()
        self.ui.txtEditDeskrip.clear()
        self.ui.txtEditNilai.clear()
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate())
        self.ui.cmbEditJenis.setCurrentIndex(0)
        
        self.edit_ability(False)
        self.ui.btnEditShow.setEnabled(True)
        self.ui.txtEditID.setEnabled(True)
        
    def btnEditDelete_clicked(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strID=self.ui.txtEditID.text()
        
        self.mysql.data_delete(namadb, strID)
        
        self.ui.txtEditID.clear()
        self.ui.txtEditDeskrip.clear()
        self.ui.txtEditNilai.clear()
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate())
        self.ui.cmbEditJenis.setCurrentIndex(0)
        
        self.edit_ability(False)
        self.ui.btnEditShow.setEnabled(True)
        self.ui.txtEditID.setEnabled(True)
        
#======================================================================================================

    def msg_about(self):
        qtver= QtCore.QT_VERSION_STR
        pyver=platform.python_version()
        mysqlver= self.mysql.procSqlVersion()

        aboutmsg = "Simple Accounting Program \n"
        aboutmsg += "\n"
        aboutmsg += "Credit: \n"
        aboutmsg += "Accounting Scheme written by Hilmi F. \n"
        aboutmsg += "GUI Program written by Achmadi \n"
        aboutmsg += "\n"
        aboutmsg += "Using: \n"
        aboutmsg += "Qt version " + qtver + "\n"
        aboutmsg += "Python version " + pyver + "\n"
        aboutmsg += "MySQL version " + mysqlver
        
        if platform.system() == "Linux":
            bashver = self.mysql.procCmdVersion()
            aboutmsg += "Bash version " + bashver
            
            osver = self.mysql.procOsVersion()
            aboutmsg += "Linux version " + osver
            
        elif platform.system() == "Windows":
            osver = self.mysql.procOsVersion()
            aboutmsg += "OS version " + osver
            
        aboutmsg += "\n"
        
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Information,"About Me",aboutmsg,QtGui.QMessageBox.Ok, self )
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
        self.ui.actionMain_Data_as_CSV.setEnabled(ability)
        
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
        
    def cari_data(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strDesk=self.ui.txtCariDeskrip.text()
        strNilai=self.ui.txtCariNilai.text()
        strJenis=QtCore.QString.number(self.ui.cmbCariJenis.currentIndex())
        strDebet=QtCore.QString.number(self.ui.cmbCariDebet.currentIndex())
        strKredit=QtCore.QString.number(self.ui.cmbCariKredit.currentIndex())
        strDate=self.ui.dateCariTanggal.text()
        
        if self.ui.rbtCariDeskrip.isChecked():self.mydata.view_search(namadb,"transaksi",strDesk)
        if self.ui.rbtCariNilai.isChecked():self.mydata.view_search(namadb,"harga",strNilai)
        if self.ui.rbtCariJenis.isChecked():self.mydata.view_search(namadb,"jenis",strJenis)
        if self.ui.rbtCariDebet.isChecked():self.mydata.view_search(namadb,"debet",strDebet)
        if self.ui.rbtCariKredit.isChecked():self.mydata.view_search(namadb,"kredit",strKredit)
        if self.ui.rbtCariTanggal.isChecked():self.mydata.view_search(namadb,"tanggal",strDate)
        
    def show_one_data(self, dataid):
        self.ui.txtEditDeskrip.setText(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"transaksi",dataid))
        self.ui.txtEditNilai.setText(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"harga",dataid))
        self.ui.cmbEditJenis.setCurrentIndex(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"jenis",dataid).toInt()[0])
        self.ui.dateEditTanggal.setDate(QtCore.QDate.fromString(self.mysql.data_get_one(self.ui.cmbDbExisting.currentText(),"tanggal",dataid),"yyyy-MM-dd"))
        
    def edit_ability(self,  ability):
        self.ui.txtEditDeskrip.setEnabled(ability)
        self.ui.txtEditNilai.setEnabled(ability)
        self.ui.cmbEditJenis.setEnabled(ability)
        self.ui.dateEditTanggal.setEnabled(ability)

        self.ui.btnEditNow.setEnabled(ability)
        self.ui.btnEditChange.setEnabled(ability)
        self.ui.btnEditDelete.setEnabled(ability)
