# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore, QtGui

class SAP_info(object):
    def __init__ (self):
        self.txtProcOutput=QtGui.QPlainTextEdit()
        self.sqlProc=QtCore.QProcess()
        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("readyReadStandardOutput()"), self.processOnGoing)
        
    def processOnGoing(self):
        newData= QtCore.QByteArray()
        newData= self.sqlProc.readAllStandardOutput()
        self.txtProcOutput.appendPlainText(QtCore.QString.fromLocal8Bit(newData))
        
#======================================================================================================
        
    def procCmdVersion(self):
        self.txtProcOutput.clear()
        self.sqlProc.start("bash -c \"echo $BASH_VERSION\"")
        self.sqlProc.waitForFinished()
        
        result=self.txtProcOutput.toPlainText()
        return result
        
    def procOsVersion(self):
        self.txtProcOutput.clear()
        
        if platform.system() == "Linux":
            self.sqlProc.start("bash -c \"uname -r\"")
            self.sqlProc.waitForFinished()
            result_linux = self.txtProcOutput.toPlainText()
            return result_linux
            
        elif platform.system() == "Windows":
            self.sqlProc.start("cmd /c ver")
            self.sqlProc.waitForFinished()
            result_win=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
            return result_win[0]
            
        else:
            result = "Unknown Operating System"
            return result
