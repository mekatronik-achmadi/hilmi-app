# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore, QtGui

class SQLsh(object):
    def __init__ (self):
        
        self.txtProcOutput=QtGui.QPlainTextEdit()
        self.sqlProc=QtCore.QProcess()
        self.sqlArgs=QtCore.QStringList()
        
        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("readyReadStandardOutput()"), self.processOnGoing)
        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("finished(int, QProcess::ExitStatus)"), self.processFinished)
        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("error(QProcess::ProcessError)"), self.processError)
        
#======================================================================================================
         
    def processOnGoing(self):
        newData= QtCore.QByteArray()
        newData= self.sqlProc.readAllStandardOutput()
        self.txtProcOutput.appendPlainText(QtCore.QString.fromLocal8Bit(newData))
        
    def processFinished(self, exitCode,  exitStatus):
        if exitStatus == QtCore.QProcess.CrashExit:
            msg = QtGui.QMessageBox(self)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setIcon(QtGui.QMessageBox.Crititcal)
            msg.setWindowTitle("Crash")
            msg.setText("Database Service Crashed")
            msg.show()
        
    def processError(self, error):
        if error == QtCore.QProcess.FailedToStart:
            msg = QtGui.QMessageBox(self)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.setIcon(QtGui.QMessageBox.Crititcal)
            msg.setWindowTitle("Not Found")
            msg.setText("Database Service not found")
            msg.show()
            
#======================================================================================================
            
    def procArgs(self):
        self.txtProcOutput.clear()
        self.sqlArgs.clear()
        
        self.sqlArgs.append("-BN")
        self.sqlArgs.append("-uroot")
        self.sqlArgs.append( "-e")
        
    def procExec(self):
        self.sqlProc.start("mysql",self.sqlArgs);
        self.sqlProc.waitForFinished();
        
#======================================================================================================

    def procSqlVersion(self):
        self.procArgs()
        
        verargs=QtCore.QString()
        verargs+= "select version()"
        
        self.sqlArgs.append(verargs)
        self.procExec()
        
        result=QtCore.QString()
        result=self.txtProcOutput.toPlainText()
        return result
        
    def procCmdVersion(self):
        self.txtProcOutput.clear()
        self.sqlProc.start("bash -c \"echo $BASH_VERSION\"")
        self.sqlProc.waitForFinished()
        
        result=QtCore.QString()
        result=self.txtProcOutput.toPlainText()
        return result
        
    def procOsVersion(self):
        result=QtCore.QString()
        self.txtProcOutput.clear()
        
        if platform.system() == "Linux":
            self.sqlProc.start("bash -c \"uname -r\"")
            self.sqlProc.waitForFinished()
            result_linux=QtCore.QString()
            result_linux = self.txtProcOutput.toPlainText()
            result = result_linux
        elif platform.system() == "Windows":
            self.sqlProc.start("cmd /c ver")
            self.sqlProc.waitForFinished()
            result_win=QtCore.QStringList()
            result_win=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
            result = result_win[0]
        else:
            result = "Unknown Operating System"
        
        return result
            
            
