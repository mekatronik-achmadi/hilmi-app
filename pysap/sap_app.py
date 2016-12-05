# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore, QtGui
from sap_sqlsh import SQLsh

class App(QtGui.QMainWindow):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.mysql=SQLsh()
        
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
