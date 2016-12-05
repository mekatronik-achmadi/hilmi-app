# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui

from sap_ui import Ui_sap
from sap_sqlsh import SQLsh
from sap_app import App

class Sap(QtGui.QMainWindow):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_sap()
        self.ui.setupUi(self)
        
        self.mysql= SQLsh()
        self.myapp=App()
        
        self.ui.dateTrsTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateCariTanggal.setDate(QtCore.QDate.currentDate ())
        self.ui.dateEditTanggal.setDate(QtCore.QDate.currentDate ())
        
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.actionAbout_triggered)
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.actionExit_triggered)
        
    def actionAbout_triggered(self):
        self.myapp.msg_about()
        
    def actionExit_triggered(self):
        QtGui.QApplication.quit()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app = Sap()
    my_app.show()
    sys.exit(app.exec_())
