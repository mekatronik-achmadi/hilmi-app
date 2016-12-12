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
            
#======================================================================================================
            
    def view_tbl_jurnal(self, dbase,):
        tblview=QtCore.QProcess()
        tblviewarg=QtCore.QStringList()
    
        if platform.system() == "Linux":
            tblviewarg.append(dbase)
            tblview.startDetached("./tblview/jurnal.py",tblviewarg)
        elif platform.system() == "Windows":
            tblviewarg.append("tblview\jurnal.py")
            tblviewarg.append(dbase)
            tblview.startDetached("pythonw",tblviewarg)
            
    def search_tbl_jurnal(self,  dbase, search_field, search_string):
        tblsearch=QtCore.QProcess()
        tblsearcharg=QtCore.QStringList()
        
        if platform.system() == "Linux":
            tblsearcharg.append(dbase)
            tblsearcharg.append(search_field)
            tblsearcharg.append(search_string)
            tblsearch.startDetached("./tblsearch/jurnal.py",tblsearcharg)
        elif platform.system() == "Windows":
            tblsearcharg.append("tblsearch\jurnal.py")
            tblsearcharg.append(dbase)
            tblsearcharg.append(search_field)
            tblsearcharg.append(search_string)
            tblsearch.startDetached("pythonw",tblsearcharg)
