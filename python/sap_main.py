# -*- coding: utf-8 -*-

import platform
from sap_ui import Ui_sap
from PyQt4 import QtCore, QtGui
from sap_storage import SAP_storage
from sap_info import SAP_info
from sap_jurnal import SAP_jurnal

class SAP_main(QtGui.QMainWindow):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_sap()
        self.ui.setupUi(self)
        
        self.my_storage=SAP_storage()
        self.my_info=SAP_info()
        self.my_jurnal=SAP_jurnal()
        
        self.refresh_databases()
        self.tab_ability(False)
        
        self.cmb_debet()
        self.cmbTrsDebet_changed()
        self.cmbEditDebet_changed()
        self.cmb_cari_kredit()
        
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate ())
        
        self.edit_ability(False)
        self.cari_disable()
        self.ui.txtCariDeskrip.setEnabled(True)
        
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.actionExit_triggered)
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.actionAbout_triggered)
        QtCore.QObject.connect(self.ui.actionMain_Data_as_Table, QtCore.SIGNAL("triggered()"), self.actionMain_Data_as_Table_triggered)
        
        QtCore.QObject.connect(self.ui.btnDbExisting, QtCore.SIGNAL("clicked()"), self.btnDbExisting_clicked)
        QtCore.QObject.connect(self.ui.btnDbNew, QtCore.SIGNAL("clicked()"), self.btnDbNew_clicked)
        QtCore.QObject.connect(self.ui.btnDbDelete, QtCore.SIGNAL("clicked()"), self.btnDbDelete_clicked)
        QtCore.QObject.connect(self.ui.btnDbExport, QtCore.SIGNAL("clicked()"), self.btnDbExport_clicked)
        
        QtCore.QObject.connect(self.ui.btnTrsClear, QtCore.SIGNAL("clicked()"), self.btnTrsClear_clicked)
        QtCore.QObject.connect(self.ui.btnTrsNow, QtCore.SIGNAL("clicked()"), self.btnTrsNow_clicked)
        QtCore.QObject.connect(self.ui.btnTrsSave, QtCore.SIGNAL("clicked()"), self.btnTrsSave_clicked)
        QtCore.QObject.connect(self.ui.cmbTrsDebet, QtCore.SIGNAL("currentIndexChanged(int)"), self.cmbTrsDebet_changed)
        
        QtCore.QObject.connect(self.ui.rbtCariDeskrip, QtCore.SIGNAL("clicked()"), self.rbtCariDeskrip_clicked)
        QtCore.QObject.connect(self.ui.rbtCariNilai, QtCore.SIGNAL("clicked()"), self.rbtCariNilai_clicked)
        QtCore.QObject.connect(self.ui.rbtCariDebet, QtCore.SIGNAL("clicked()"), self.rbtCariDebet_clicked)
        QtCore.QObject.connect(self.ui.rbtCariKredit, QtCore.SIGNAL("clicked()"), self.rbtCariKredit_clicked)
        QtCore.QObject.connect(self.ui.rbtCariTanggal, QtCore.SIGNAL("clicked()"), self.rbtCariTanggal_clicked)
        QtCore.QObject.connect(self.ui.btnCariClear, QtCore.SIGNAL("clicked()"), self.btnCariClear_clicked)
        QtCore.QObject.connect(self.ui.btnCariNow, QtCore.SIGNAL("clicked()"), self.btnCariNow_clicked)
        QtCore.QObject.connect(self.ui.btnCari, QtCore.SIGNAL("clicked()"), self.btnCari_clicked)
        
        QtCore.QObject.connect(self.ui.btnEditNow, QtCore.SIGNAL("clicked()"), self.btnEditNow_clicked)
        QtCore.QObject.connect(self.ui.btnEditShow, QtCore.SIGNAL("clicked()"), self.btnEditShow_clicked)
        QtCore.QObject.connect(self.ui.cmbEditDebet, QtCore.SIGNAL("currentIndexChanged(int)"), self.cmbEditDebet_changed)
        QtCore.QObject.connect(self.ui.btnEditChange, QtCore.SIGNAL("clicked()"), self.btnEditChange_clicked)
        QtCore.QObject.connect(self.ui.btnEditDelete, QtCore.SIGNAL("clicked()"), self.btnEditDelete_clicked)
        
#======================================================================================================

    def actionExit_triggered(self):
        QtGui.QApplication.quit()
        
    def actionAbout_triggered(self):
        self.msg_about()
        
    def actionMain_Data_as_Table_triggered(self):
        self.my_info.view_tbl_jurnal(self.ui.cmbDbExisting.currentText())
        
#======================================================================================================

    def btnDbExisting_clicked(self):
        if self.ui.cmbDbExisting.currentText().isEmpty():
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
        
        self.my_storage.create_database(namadb)
        self.my_storage.create_table(namadb)
        self.refresh_databases()
        
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Information,"Sudah tercipta","Data " + namadb + " tercipta !!",QtGui.QMessageBox.Ok, self )
        msg.show()
        self.ui.txtDbNew.clear()
        
    def btnDbDelete_clicked(self):
        namadb=self.ui.cmbDbDelete.currentText()
            
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Warning,"Yakin?", "yakin akan mnghapus data " + namadb + " selamanya ?!!",QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, self )
        retval = msg.exec_()
        if retval == QtGui.QMessageBox.Ok:
            self.my_storage.drop_database(namadb)
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
            
        self.my_storage.export_database(namadb, fileName)
        
    def btnDbImport_clicked(self):
        namadb=self.ui.cmbDbImport.currentText()
            
        fileName=QtGui.QFileDialog.getOpenFileName(self,"Import Data", QtCore.QString(), "*.sql")
        if fileName.isEmpty():
            return
        
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Warning,"Yakin?", "seluruh isi data " + namadb + " akan ditimpa data baru, lanjutkan ?!!",QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, self )
        retval = msg.exec_()
        if retval == QtGui.QMessageBox.Ok:
            self.my_storage.import_database(namadb,fileName)
            
#======================================================================================================

    def btnTrsClear_clicked(self):
        self.ui.txtTrsDeskrip.clear()
        self.ui.txtTrsNilai.clear()
        self.ui.cmbTrsJenis.setCurrentIndex(0)
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        
    def cmbTrsDebet_changed(self):
        self.ui.cmbTrsKredit.clear()
        self.ui.cmbTrsKredit.insertItems(0,self.my_jurnal.txtlst_kredit_debet(self.ui.cmbTrsDebet.currentText()))
    
    def btnTrsNow_clicked(self):
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        
    def btnTrsSave_clicked(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strTgl=self.ui.dateTrsTanggal.text()
        strDesk=self.ui.txtTrsDeskrip.text()
        strNilai=self.ui.txtTrsNilai.text()
        strDebet=self.ui.cmbTrsDebet.currentText()
        strKredit=self.ui.cmbTrsKredit.currentText()
        
        if strDebet == "-- pilih salah satu --":
            msg = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Debet Kosong","Pilih alah satu jenis transaksi debet !!",QtGui.QMessageBox.Ok, self )
            msg.show()
            return
        
        self.my_storage.insert_tbl_jurnal(namadb, strTgl, strDesk, strNilai, strDebet, strKredit)
        
        self.ui.txtTrsDeskrip.clear()
        self.ui.txtTrsNilai.clear()
        self.ui.cmbTrsDebet.setCurrentIndex(0)
        self.ui.cmbTrsKredit.setCurrentIndex(0)

#======================================================================================================

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
        self.ui.cmbCariDebet.setCurrentIndex(0)
        self.ui.cmbCariKredit.setCurrentIndex(0)
            
    def btnCariNow_clicked(self):
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate())
        
    def btnCari_clicked(self):
        self.cari_data()
        
#======================================================================================================

    def btnEditNow_clicked(self):
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate())
    
    def btnEditShow_clicked(self):
        txtID=self.ui.txtEditID.text()
        self.show_one_data(txtID)
        
        self.edit_ability(True)
        self.ui.btnEditShow.setEnabled(False)
        self.ui.txtEditID.setEnabled(False)
        
    def cmbEditDebet_changed(self):
        self.ui.cmbEditKredit.clear()
        self.ui.cmbEditKredit.insertItems(0,self.my_jurnal.txtlst_kredit_debet(self.ui.cmbEditDebet.currentText()))
        
    def btnEditChange_clicked(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strID=self.ui.txtEditID.text()
        strTgl=self.ui.dateEditTanggal.text()
        strDesk=self.ui.txtEditDeskrip.text()
        strNilai=self.ui.txtEditNilai.text()
        strDebet=self.ui.cmbEditDebet.currentText()
        strKredit=self.ui.cmbEditKredit.currentText()
        
        if strDebet == "-- pilih salah satu --":
            msg = QtGui.QMessageBox(QtGui.QMessageBox.Critical,"Debet Kosong","Pilih alah satu jenis transaksi debet !!",QtGui.QMessageBox.Ok, self )
            msg.show()
            return
        
        self.my_storage.update_tbl_jurnal(namadb, strID, strTgl, strDesk, strNilai, strDebet, strKredit)
        
        self.ui.txtEditID.clear()
        self.ui.txtEditDeskrip.clear()
        self.ui.txtEditNilai.clear()
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate())
        self.ui.cmbEditDebet.setCurrentIndex(0)
        self.cmbEditDebet_changed()
        
        self.edit_ability(False)
        self.ui.btnEditShow.setEnabled(True)
        self.ui.txtEditID.setEnabled(True)
        
    def btnEditDelete_clicked(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strID=self.ui.txtEditID.text()
        
        self.my_storage.delete_tbl_jurnal(namadb, strID)
        
        self.ui.txtEditID.clear()
        self.ui.txtEditDeskrip.clear()
        self.ui.txtEditNilai.clear()
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate())
        self.ui.cmbEditDebet.setCurrentIndex(0)
        self.cmbEditDebet_changed()
        
        self.edit_ability(False)
        self.ui.btnEditShow.setEnabled(True)
        self.ui.txtEditID.setEnabled(True)

#======================================================================================================

    def msg_about(self):
        qtver= QtCore.QT_VERSION_STR
        pyver=platform.python_version()
        mysqlver= self.my_storage.sql_version()
        mysqldbver=self.my_storage.driver_version

        aboutmsg = "Simple Accounting Program \n"
        aboutmsg += "\n"
        aboutmsg += "Credit: \n"
        aboutmsg += "Accounting Scheme written by Hilmi F. \n"
        aboutmsg += "GUI Program written by Achmadi \n"
        aboutmsg += "\n"
        aboutmsg += "Using: \n"
        aboutmsg += "Qt version " + qtver + "\n"
        aboutmsg += "Python version " + pyver + "\n"
        aboutmsg += "MySQL version " + mysqlver + "\n"
        aboutmsg += "MySQLdb version " + mysqldbver + "\n"
        
        if platform.system() == "Linux":
            bashver = self.my_info.procCmdVersion()
            aboutmsg += "Bash version " + bashver
            
            osver = self.my_info.procOsVersion()
            aboutmsg += "Linux version " + osver
            
        elif platform.system() == "Windows":
            osver = self.my_info.procOsVersion()
            aboutmsg += "OS version " + osver
            
        aboutmsg += "\n"
        
        msg = QtGui.QMessageBox(QtGui.QMessageBox.Information,"About Me",aboutmsg,QtGui.QMessageBox.Ok, self )
        msg.show()

    def refresh_databases(self):
        result_all=self.my_storage.show_databases()
        result=QtCore.QStringList()
        for rowdata in result_all:
            if rowdata[0] == "performance_schema":
                pass
            elif rowdata[0] == "mysql":
                pass
            elif rowdata[0] == "test":
                pass
            elif rowdata[0] == "information_schema":
                pass
            else:
                result.append(str(rowdata[0]))
                
        self.ui.cmbDbDelete.clear()
        self.ui.cmbDbDelete.insertItems(0,result)

        self.ui.cmbDbExisting.clear()
        self.ui.cmbDbExisting.insertItems(0,result)

        self.ui.cmbDbExport.clear()
        self.ui.cmbDbExport.insertItems(0,result)

        self.ui.cmbDbImport.clear()
        self.ui.cmbDbImport.insertItems(0,result)
        
    def tab_ability(self, ability):
        self.ui.tabMain.setTabEnabled(1,ability)
        self.ui.tabMain.setTabEnabled(2,ability)
        self.ui.tabMain.setTabEnabled(3,ability)
        self.ui.actionMain_Data_as_Table.setEnabled(ability)
        
    def cmb_debet(self):
        self.ui.cmbTrsDebet.clear()
        self.ui.cmbTrsDebet.insertItems(0,self.my_jurnal.txtlst_debet())
        self.ui.cmbCariDebet.clear()
        self.ui.cmbCariDebet.insertItems(0,self.my_jurnal.txtlst_debet())
        self.ui.cmbEditDebet.clear()
        self.ui.cmbEditDebet.insertItems(0,self.my_jurnal.txtlst_debet())
        
    def cmb_cari_kredit(self):
        self.ui.cmbCariKredit.clear()
        self.ui.cmbCariKredit.insertItems(0,self.my_jurnal.txtlst_kredit())
        
    def edit_ability(self,  ability):
        self.ui.txtEditDeskrip.setEnabled(ability)
        self.ui.txtEditNilai.setEnabled(ability)
        self.ui.cmbEditDebet.setEnabled(ability)
        self.ui.cmbEditKredit.setEnabled(ability)
        self.ui.dateEditTanggal.setEnabled(ability)
        self.ui.btnEditNow.setEnabled(ability)
        self.ui.btnEditChange.setEnabled(ability)
        self.ui.btnEditDelete.setEnabled(ability)
        
    def cari_disable(self):
        self.ui.txtCariDeskrip.setEnabled(False)
        self.ui.txtCariNilai.setEnabled(False)
        self.ui.cmbCariDebet.setEnabled(False)
        self.ui.cmbCariKredit.setEnabled(False)
        self.ui.dateCariTanggal.setEnabled(False)
        self.ui.btnCariNow.setEnabled(False)
        
    def cari_data(self):
        namadb=self.ui.cmbDbExisting.currentText()
        strDesk=self.ui.txtCariDeskrip.text()
        strNilai=self.ui.txtCariNilai.text()
        strDebet=self.ui.cmbCariDebet.currentText()
        strKredit=self.ui.cmbCariKredit.currentText()
        strDate=self.ui.dateCariTanggal.text()
        
        if self.ui.rbtCariDeskrip.isChecked():self.my_info.search_tbl_jurnal(namadb,"transaksi",strDesk)
        if self.ui.rbtCariNilai.isChecked():self.my_info.search_tbl_jurnal(namadb,"harga",strNilai)
        if self.ui.rbtCariDebet.isChecked():self.my_info.search_tbl_jurnal(namadb,"debet",strDebet)
        if self.ui.rbtCariKredit.isChecked():self.my_info.search_tbl_jurnal(namadb,"kredit",strKredit)
        if self.ui.rbtCariTanggal.isChecked():self.my_info.search_tbl_jurnal(namadb,"tanggal",strDate)
    
    def show_one_data(self, dataid):
        namadb=self.ui.cmbDbExisting.currentText()
        odata=self.my_storage.search_tbl_jurnal(namadb, dataid)
        self.ui.dateEditTanggal.setDate(QtCore.QDate.fromString(str(odata[0][1]),"yyyy-MM-dd"))
        self.ui.txtEditDeskrip.setText(odata[0][2])
        self.ui.txtEditNilai.setText(odata[0][3])
        self.ui.cmbEditDebet.setCurrentIndex(self.my_jurnal.int_debet(odata[0][4]))
        self.cmbEditDebet_changed()
