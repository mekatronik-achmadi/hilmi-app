# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sap.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_sap(object):
    def setupUi(self, sap):
        sap.setObjectName(_fromUtf8("sap"))
        sap.resize(586, 457)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sap.sizePolicy().hasHeightForWidth())
        sap.setSizePolicy(sizePolicy)
        self.centralWidget = QtGui.QWidget(sap)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabMain = QtGui.QTabWidget(self.centralWidget)
        self.tabMain.setEnabled(True)
        self.tabMain.setGeometry(QtCore.QRect(10, 0, 571, 391))
        self.tabMain.setObjectName(_fromUtf8("tabMain"))
        self.tabDatabase = QtGui.QWidget()
        self.tabDatabase.setObjectName(_fromUtf8("tabDatabase"))
        self.grpDatabase = QtGui.QGroupBox(self.tabDatabase)
        self.grpDatabase.setGeometry(QtCore.QRect(0, 70, 311, 111))
        self.grpDatabase.setObjectName(_fromUtf8("grpDatabase"))
        self.txtDbNew = QtGui.QLineEdit(self.grpDatabase)
        self.txtDbNew.setEnabled(True)
        self.txtDbNew.setGeometry(QtCore.QRect(100, 30, 113, 23))
        self.txtDbNew.setObjectName(_fromUtf8("txtDbNew"))
        self.btnDbNew = QtGui.QPushButton(self.grpDatabase)
        self.btnDbNew.setEnabled(True)
        self.btnDbNew.setGeometry(QtCore.QRect(230, 30, 61, 26))
        self.btnDbNew.setObjectName(_fromUtf8("btnDbNew"))
        self.cmbDbDelete = QtGui.QComboBox(self.grpDatabase)
        self.cmbDbDelete.setEnabled(True)
        self.cmbDbDelete.setGeometry(QtCore.QRect(100, 70, 111, 24))
        self.cmbDbDelete.setObjectName(_fromUtf8("cmbDbDelete"))
        self.btnDbDelete = QtGui.QPushButton(self.grpDatabase)
        self.btnDbDelete.setEnabled(True)
        self.btnDbDelete.setGeometry(QtCore.QRect(230, 70, 61, 26))
        self.btnDbDelete.setObjectName(_fromUtf8("btnDbDelete"))
        self.label_11 = QtGui.QLabel(self.grpDatabase)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.grpDatabase)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.grpExportImport = QtGui.QGroupBox(self.tabDatabase)
        self.grpExportImport.setGeometry(QtCore.QRect(0, 190, 311, 101))
        self.grpExportImport.setObjectName(_fromUtf8("grpExportImport"))
        self.cmbDbExport = QtGui.QComboBox(self.grpExportImport)
        self.cmbDbExport.setEnabled(True)
        self.cmbDbExport.setGeometry(QtCore.QRect(100, 20, 111, 24))
        self.cmbDbExport.setObjectName(_fromUtf8("cmbDbExport"))
        self.label_5 = QtGui.QLabel(self.grpExportImport)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.btnDbExport = QtGui.QPushButton(self.grpExportImport)
        self.btnDbExport.setEnabled(True)
        self.btnDbExport.setGeometry(QtCore.QRect(220, 20, 61, 26))
        self.btnDbExport.setObjectName(_fromUtf8("btnDbExport"))
        self.btnDbImport = QtGui.QPushButton(self.grpExportImport)
        self.btnDbImport.setEnabled(True)
        self.btnDbImport.setGeometry(QtCore.QRect(220, 70, 61, 26))
        self.btnDbImport.setObjectName(_fromUtf8("btnDbImport"))
        self.cmbDbImport = QtGui.QComboBox(self.grpExportImport)
        self.cmbDbImport.setEnabled(True)
        self.cmbDbImport.setGeometry(QtCore.QRect(100, 70, 111, 24))
        self.cmbDbImport.setObjectName(_fromUtf8("cmbDbImport"))
        self.label_6 = QtGui.QLabel(self.grpExportImport)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.grpDbSelect = QtGui.QGroupBox(self.tabDatabase)
        self.grpDbSelect.setGeometry(QtCore.QRect(0, 0, 221, 61))
        self.grpDbSelect.setObjectName(_fromUtf8("grpDbSelect"))
        self.btnDbExisting = QtGui.QPushButton(self.grpDbSelect)
        self.btnDbExisting.setEnabled(True)
        self.btnDbExisting.setGeometry(QtCore.QRect(150, 20, 61, 26))
        self.btnDbExisting.setObjectName(_fromUtf8("btnDbExisting"))
        self.cmbDbExisting = QtGui.QComboBox(self.grpDbSelect)
        self.cmbDbExisting.setEnabled(True)
        self.cmbDbExisting.setGeometry(QtCore.QRect(10, 20, 131, 24))
        self.cmbDbExisting.setObjectName(_fromUtf8("cmbDbExisting"))
        self.tabMain.addTab(self.tabDatabase, _fromUtf8(""))
        self.tabInput = QtGui.QWidget()
        self.tabInput.setObjectName(_fromUtf8("tabInput"))
        self.grpInput = QtGui.QGroupBox(self.tabInput)
        self.grpInput.setGeometry(QtCore.QRect(0, 0, 541, 231))
        self.grpInput.setObjectName(_fromUtf8("grpInput"))
        self.label = QtGui.QLabel(self.grpInput)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtTrsDeskrip = QtGui.QLineEdit(self.grpInput)
        self.txtTrsDeskrip.setGeometry(QtCore.QRect(130, 30, 401, 23))
        self.txtTrsDeskrip.setMaxLength(32)
        self.txtTrsDeskrip.setObjectName(_fromUtf8("txtTrsDeskrip"))
        self.cmbTrsDebet = QtGui.QComboBox(self.grpInput)
        self.cmbTrsDebet.setGeometry(QtCore.QRect(130, 90, 401, 24))
        self.cmbTrsDebet.setObjectName(_fromUtf8("cmbTrsDebet"))
        self.label_2 = QtGui.QLabel(self.grpInput)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.grpInput)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtTrsNilai = QtGui.QLineEdit(self.grpInput)
        self.txtTrsNilai.setGeometry(QtCore.QRect(130, 60, 401, 23))
        self.txtTrsNilai.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtTrsNilai.setText(_fromUtf8(""))
        self.txtTrsNilai.setMaxLength(32)
        self.txtTrsNilai.setObjectName(_fromUtf8("txtTrsNilai"))
        self.dateTrsTanggal = QtGui.QDateEdit(self.grpInput)
        self.dateTrsTanggal.setGeometry(QtCore.QRect(130, 160, 110, 23))
        self.dateTrsTanggal.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTrsTanggal.setReadOnly(False)
        self.dateTrsTanggal.setCalendarPopup(True)
        self.dateTrsTanggal.setProperty("showGroupSeparator", False)
        self.dateTrsTanggal.setObjectName(_fromUtf8("dateTrsTanggal"))
        self.label_4 = QtGui.QLabel(self.grpInput)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnTrsSave = QtGui.QPushButton(self.grpInput)
        self.btnTrsSave.setGeometry(QtCore.QRect(20, 200, 85, 26))
        self.btnTrsSave.setObjectName(_fromUtf8("btnTrsSave"))
        self.btnTrsClear = QtGui.QPushButton(self.grpInput)
        self.btnTrsClear.setGeometry(QtCore.QRect(120, 200, 85, 26))
        self.btnTrsClear.setObjectName(_fromUtf8("btnTrsClear"))
        self.btnTrsNow = QtGui.QPushButton(self.grpInput)
        self.btnTrsNow.setGeometry(QtCore.QRect(260, 160, 85, 26))
        self.btnTrsNow.setObjectName(_fromUtf8("btnTrsNow"))
        self.label_14 = QtGui.QLabel(self.grpInput)
        self.label_14.setGeometry(QtCore.QRect(80, 120, 41, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.cmbTrsKredit = QtGui.QComboBox(self.grpInput)
        self.cmbTrsKredit.setGeometry(QtCore.QRect(130, 120, 401, 24))
        self.cmbTrsKredit.setObjectName(_fromUtf8("cmbTrsKredit"))
        self.tabMain.addTab(self.tabInput, _fromUtf8(""))
        self.tabSearch = QtGui.QWidget()
        self.tabSearch.setObjectName(_fromUtf8("tabSearch"))
        self.grpCari = QtGui.QGroupBox(self.tabSearch)
        self.grpCari.setGeometry(QtCore.QRect(0, 0, 541, 291))
        self.grpCari.setObjectName(_fromUtf8("grpCari"))
        self.txtCariDeskrip = QtGui.QLineEdit(self.grpCari)
        self.txtCariDeskrip.setGeometry(QtCore.QRect(130, 30, 371, 23))
        self.txtCariDeskrip.setMaxLength(32)
        self.txtCariDeskrip.setObjectName(_fromUtf8("txtCariDeskrip"))
        self.txtCariNilai = QtGui.QLineEdit(self.grpCari)
        self.txtCariNilai.setEnabled(False)
        self.txtCariNilai.setGeometry(QtCore.QRect(130, 60, 371, 23))
        self.txtCariNilai.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtCariNilai.setText(_fromUtf8(""))
        self.txtCariNilai.setMaxLength(32)
        self.txtCariNilai.setObjectName(_fromUtf8("txtCariNilai"))
        self.dateCariTanggal = QtGui.QDateEdit(self.grpCari)
        self.dateCariTanggal.setEnabled(False)
        self.dateCariTanggal.setGeometry(QtCore.QRect(130, 150, 110, 23))
        self.dateCariTanggal.setAlignment(QtCore.Qt.AlignCenter)
        self.dateCariTanggal.setReadOnly(False)
        self.dateCariTanggal.setCalendarPopup(True)
        self.dateCariTanggal.setProperty("showGroupSeparator", False)
        self.dateCariTanggal.setObjectName(_fromUtf8("dateCariTanggal"))
        self.btnCari = QtGui.QPushButton(self.grpCari)
        self.btnCari.setGeometry(QtCore.QRect(20, 190, 85, 26))
        self.btnCari.setObjectName(_fromUtf8("btnCari"))
        self.btnCariClear = QtGui.QPushButton(self.grpCari)
        self.btnCariClear.setGeometry(QtCore.QRect(120, 190, 85, 26))
        self.btnCariClear.setObjectName(_fromUtf8("btnCariClear"))
        self.btnCariNow = QtGui.QPushButton(self.grpCari)
        self.btnCariNow.setGeometry(QtCore.QRect(260, 150, 85, 26))
        self.btnCariNow.setObjectName(_fromUtf8("btnCariNow"))
        self.rbtCariDeskrip = QtGui.QRadioButton(self.grpCari)
        self.rbtCariDeskrip.setGeometry(QtCore.QRect(10, 30, 97, 20))
        self.rbtCariDeskrip.setChecked(True)
        self.rbtCariDeskrip.setObjectName(_fromUtf8("rbtCariDeskrip"))
        self.rbtCariNilai = QtGui.QRadioButton(self.grpCari)
        self.rbtCariNilai.setGeometry(QtCore.QRect(10, 60, 97, 20))
        self.rbtCariNilai.setObjectName(_fromUtf8("rbtCariNilai"))
        self.rbtCariTanggal = QtGui.QRadioButton(self.grpCari)
        self.rbtCariTanggal.setGeometry(QtCore.QRect(10, 150, 97, 20))
        self.rbtCariTanggal.setObjectName(_fromUtf8("rbtCariTanggal"))
        self.cmbCariDebet = QtGui.QComboBox(self.grpCari)
        self.cmbCariDebet.setEnabled(False)
        self.cmbCariDebet.setGeometry(QtCore.QRect(130, 90, 371, 24))
        self.cmbCariDebet.setObjectName(_fromUtf8("cmbCariDebet"))
        self.rbtCariDebet = QtGui.QRadioButton(self.grpCari)
        self.rbtCariDebet.setGeometry(QtCore.QRect(10, 90, 97, 20))
        self.rbtCariDebet.setObjectName(_fromUtf8("rbtCariDebet"))
        self.cmbCariKredit = QtGui.QComboBox(self.grpCari)
        self.cmbCariKredit.setEnabled(False)
        self.cmbCariKredit.setGeometry(QtCore.QRect(130, 120, 371, 24))
        self.cmbCariKredit.setObjectName(_fromUtf8("cmbCariKredit"))
        self.rbtCariKredit = QtGui.QRadioButton(self.grpCari)
        self.rbtCariKredit.setGeometry(QtCore.QRect(10, 120, 97, 20))
        self.rbtCariKredit.setObjectName(_fromUtf8("rbtCariKredit"))
        self.tabMain.addTab(self.tabSearch, _fromUtf8(""))
        self.tabEdit = QtGui.QWidget()
        self.tabEdit.setObjectName(_fromUtf8("tabEdit"))
        self.grpEdit = QtGui.QGroupBox(self.tabEdit)
        self.grpEdit.setGeometry(QtCore.QRect(0, 0, 541, 271))
        self.grpEdit.setObjectName(_fromUtf8("grpEdit"))
        self.label_7 = QtGui.QLabel(self.grpEdit)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txtEditDeskrip = QtGui.QLineEdit(self.grpEdit)
        self.txtEditDeskrip.setGeometry(QtCore.QRect(130, 70, 401, 23))
        self.txtEditDeskrip.setMaxLength(32)
        self.txtEditDeskrip.setObjectName(_fromUtf8("txtEditDeskrip"))
        self.cmbEditDebet = QtGui.QComboBox(self.grpEdit)
        self.cmbEditDebet.setGeometry(QtCore.QRect(130, 130, 401, 24))
        self.cmbEditDebet.setObjectName(_fromUtf8("cmbEditDebet"))
        self.label_8 = QtGui.QLabel(self.grpEdit)
        self.label_8.setGeometry(QtCore.QRect(80, 130, 31, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.grpEdit)
        self.label_9.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txtEditNilai = QtGui.QLineEdit(self.grpEdit)
        self.txtEditNilai.setGeometry(QtCore.QRect(130, 100, 401, 23))
        self.txtEditNilai.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.txtEditNilai.setText(_fromUtf8(""))
        self.txtEditNilai.setMaxLength(32)
        self.txtEditNilai.setObjectName(_fromUtf8("txtEditNilai"))
        self.dateEditTanggal = QtGui.QDateEdit(self.grpEdit)
        self.dateEditTanggal.setGeometry(QtCore.QRect(130, 200, 110, 23))
        self.dateEditTanggal.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditTanggal.setReadOnly(False)
        self.dateEditTanggal.setCalendarPopup(True)
        self.dateEditTanggal.setProperty("showGroupSeparator", False)
        self.dateEditTanggal.setObjectName(_fromUtf8("dateEditTanggal"))
        self.label_10 = QtGui.QLabel(self.grpEdit)
        self.label_10.setGeometry(QtCore.QRect(10, 200, 101, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.btnEditChange = QtGui.QPushButton(self.grpEdit)
        self.btnEditChange.setEnabled(True)
        self.btnEditChange.setGeometry(QtCore.QRect(20, 240, 85, 26))
        self.btnEditChange.setObjectName(_fromUtf8("btnEditChange"))
        self.btnEditNow = QtGui.QPushButton(self.grpEdit)
        self.btnEditNow.setGeometry(QtCore.QRect(260, 200, 85, 26))
        self.btnEditNow.setObjectName(_fromUtf8("btnEditNow"))
        self.label_13 = QtGui.QLabel(self.grpEdit)
        self.label_13.setGeometry(QtCore.QRect(70, 20, 51, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.txtEditID = QtGui.QLineEdit(self.grpEdit)
        self.txtEditID.setGeometry(QtCore.QRect(130, 20, 181, 23))
        self.txtEditID.setMaxLength(32)
        self.txtEditID.setObjectName(_fromUtf8("txtEditID"))
        self.btnEditShow = QtGui.QPushButton(self.grpEdit)
        self.btnEditShow.setGeometry(QtCore.QRect(320, 20, 85, 26))
        self.btnEditShow.setObjectName(_fromUtf8("btnEditShow"))
        self.btnEditDelete = QtGui.QPushButton(self.grpEdit)
        self.btnEditDelete.setEnabled(True)
        self.btnEditDelete.setGeometry(QtCore.QRect(120, 240, 85, 26))
        self.btnEditDelete.setObjectName(_fromUtf8("btnEditDelete"))
        self.label_15 = QtGui.QLabel(self.grpEdit)
        self.label_15.setGeometry(QtCore.QRect(80, 160, 41, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.cmbEditKredit = QtGui.QComboBox(self.grpEdit)
        self.cmbEditKredit.setGeometry(QtCore.QRect(130, 160, 401, 24))
        self.cmbEditKredit.setObjectName(_fromUtf8("cmbEditKredit"))
        self.tabMain.addTab(self.tabEdit, _fromUtf8(""))
        sap.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(sap)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        sap.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(sap)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        sap.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(sap)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 586, 19))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        sap.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(sap)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(sap)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionTableJurnal = QtGui.QAction(sap)
        self.actionTableJurnal.setObjectName(_fromUtf8("actionTableJurnal"))
        self.actionTableAkun = QtGui.QAction(sap)
        self.actionTableAkun.setObjectName(_fromUtf8("actionTableAkun"))
        self.actionLaporanPendapatan = QtGui.QAction(sap)
        self.actionLaporanPendapatan.setObjectName(_fromUtf8("actionLaporanPendapatan"))
        self.actionLaporanModal = QtGui.QAction(sap)
        self.actionLaporanModal.setObjectName(_fromUtf8("actionLaporanModal"))
        self.actionLaporanKas = QtGui.QAction(sap)
        self.actionLaporanKas.setObjectName(_fromUtf8("actionLaporanKas"))
        self.actionLaporanNeraca = QtGui.QAction(sap)
        self.actionLaporanNeraca.setObjectName(_fromUtf8("actionLaporanNeraca"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAbout)
        self.menuView.addAction(self.actionTableJurnal)
        self.menuView.addAction(self.actionTableAkun)
        self.menuView.addAction(self.actionLaporanPendapatan)
        self.menuView.addAction(self.actionLaporanModal)
        self.menuView.addAction(self.actionLaporanKas)
        self.menuView.addAction(self.actionLaporanNeraca)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(sap)
        self.tabMain.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(sap)

    def retranslateUi(self, sap):
        sap.setWindowTitle(_translate("sap", "Simple Accounting Program", None))
        self.grpDatabase.setTitle(_translate("sap", "Manage Databases", None))
        self.btnDbNew.setText(_translate("sap", "Create", None))
        self.btnDbDelete.setText(_translate("sap", "Delete", None))
        self.label_11.setText(_translate("sap", "Create Data", None))
        self.label_12.setText(_translate("sap", "Delete Data", None))
        self.grpExportImport.setTitle(_translate("sap", "Export/Import Data", None))
        self.label_5.setText(_translate("sap", "Data to Export", None))
        self.btnDbExport.setText(_translate("sap", "Export", None))
        self.btnDbImport.setText(_translate("sap", "Import", None))
        self.label_6.setText(_translate("sap", "Import to Data", None))
        self.grpDbSelect.setTitle(_translate("sap", "Select Data ", None))
        self.btnDbExisting.setText(_translate("sap", "Use", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabDatabase), _translate("sap", "Database", None))
        self.grpInput.setTitle(_translate("sap", "Input Transaksi", None))
        self.label.setText(_translate("sap", "Deksripsi Transaksi", None))
        self.label_2.setText(_translate("sap", "Debit", None))
        self.label_3.setText(_translate("sap", "Nilai Transaksi", None))
        self.dateTrsTanggal.setDisplayFormat(_translate("sap", "yyyy-M-d", None))
        self.label_4.setText(_translate("sap", "Tanggal Transaksi", None))
        self.btnTrsSave.setText(_translate("sap", "Save", None))
        self.btnTrsClear.setText(_translate("sap", "Clear", None))
        self.btnTrsNow.setText(_translate("sap", "Now", None))
        self.label_14.setText(_translate("sap", "Kredit", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabInput), _translate("sap", "Input", None))
        self.grpCari.setTitle(_translate("sap", "Cari Data", None))
        self.dateCariTanggal.setDisplayFormat(_translate("sap", "yyyy-M-d", None))
        self.btnCari.setText(_translate("sap", "Search", None))
        self.btnCariClear.setText(_translate("sap", "Clear", None))
        self.btnCariNow.setText(_translate("sap", "Now", None))
        self.rbtCariDeskrip.setText(_translate("sap", "Deskripsi", None))
        self.rbtCariNilai.setText(_translate("sap", "Nilai", None))
        self.rbtCariTanggal.setText(_translate("sap", "Tanggal", None))
        self.rbtCariDebet.setText(_translate("sap", "Debet", None))
        self.rbtCariKredit.setText(_translate("sap", "Kredit", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabSearch), _translate("sap", "Search", None))
        self.grpEdit.setTitle(_translate("sap", "Edit Transaksi", None))
        self.label_7.setText(_translate("sap", "Deksripsi Transaksi", None))
        self.label_8.setText(_translate("sap", "Debit", None))
        self.label_9.setText(_translate("sap", "Nilai Transaksi", None))
        self.dateEditTanggal.setDisplayFormat(_translate("sap", "yyyy-M-d", None))
        self.label_10.setText(_translate("sap", "Tanggal Transaksi", None))
        self.btnEditChange.setText(_translate("sap", "Update", None))
        self.btnEditNow.setText(_translate("sap", "Now", None))
        self.label_13.setText(_translate("sap", "Data ID", None))
        self.btnEditShow.setText(_translate("sap", "Show", None))
        self.btnEditDelete.setText(_translate("sap", "Delete", None))
        self.label_15.setText(_translate("sap", "Kredit", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabEdit), _translate("sap", "Edit", None))
        self.menuFile.setTitle(_translate("sap", "File", None))
        self.menuView.setTitle(_translate("sap", "View", None))
        self.actionExit.setText(_translate("sap", "Exit", None))
        self.actionAbout.setText(_translate("sap", "About", None))
        self.actionTableJurnal.setText(_translate("sap", "Table Jurnal", None))
        self.actionTableAkun.setText(_translate("sap", "Table Akun", None))
        self.actionLaporanPendapatan.setText(_translate("sap", "Laporan Pendapatan", None))
        self.actionLaporanModal.setText(_translate("sap", "Laporan Modal", None))
        self.actionLaporanKas.setText(_translate("sap", "Laporan Kas", None))
        self.actionLaporanNeraca.setText(_translate("sap", "Laporan Neraca", None))

