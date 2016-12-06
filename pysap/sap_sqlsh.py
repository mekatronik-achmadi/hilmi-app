# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore, QtGui

class SQLsh(object):
    def __init__ (self):
        
        self.txtProcOutput=QtGui.QPlainTextEdit()
        self.sqlProc=QtCore.QProcess()
        self.sqlArgs=QtCore.QStringList()
        
        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("readyReadStandardOutput()"), self.processOnGoing)
#        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("finished(int, QProcess::ExitStatus)"), self.processFinished)
#        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("error(QProcess::ProcessError)"), self.processError)
         
    def processOnGoing(self):
        newData= QtCore.QByteArray()
        newData= self.sqlProc.readAllStandardOutput()
        self.txtProcOutput.appendPlainText(QtCore.QString.fromLocal8Bit(newData))
        
#    def processFinished(self, exitCode,  exitStatus):
#        if exitStatus == QtCore.QProcess.CrashExit:
#            msg = QtGui.QMessageBox(self)
#            msg.setStandardButtons(QtGui.QMessageBox.Ok)
#            msg.setIcon(QtGui.QMessageBox.Crititcal)
#            msg.setWindowTitle("Crash")
#            msg.setText("Database Service Crashed")
#            msg.show()
#        
#    def processError(self, error):
#        if error == QtCore.QProcess.FailedToStart:
#            msg = QtGui.QMessageBox(self)
#            msg.setStandardButtons(QtGui.QMessageBox.Ok)
#            msg.setIcon(QtGui.QMessageBox.Crititcal)
#            msg.setWindowTitle("Not Found")
#            msg.setText("Database Service not found")
#            msg.show()
            
#======================================================================================================
            
    def procArgs(self):
        self.txtProcOutput.clear()
        self.sqlArgs.clear()
        
        self.sqlArgs.append("-BN")
        self.sqlArgs.append("-uroot")
        self.sqlArgs.append( "-e")
        
    def procExec(self):
        self.sqlProc.start("mysql",self.sqlArgs)
        self.sqlProc.waitForFinished()
        
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
        
#======================================================================================================
            
    def create_database(self, dbname):
        self.procArgs()
        
        dbargs=QtCore.QString()
        dbargs += "create database "
        dbargs += dbname
        
        self.sqlArgs.append(dbargs)
        self.procExec()
        
    def delete_database(self, dbname):
        self.procArgs()
        
        dbargs=QtCore.QString()
        dbargs += "drop database "
        dbargs += dbname
        
        self.sqlArgs.append(dbargs)
        self.procExec()
        
    def export_database(self, dbname, filedest):
        sqldumpproc=QtCore.QProcess()
        
        if platform.system() == "Linux":
            sqldumpproc.start("bash -c \"mysqldump -uroot " + dbname + " > " + filedest + "\"")
            
        elif platform.system() == "Windows":
            sqldumpprocargs=QtCore.QStringList()
            
            sqldumpprocargs.append("/c")
            sqldumpprocargs.append("mysqldump")
            sqldumpprocargs.append("-uroot")
            sqldumpprocargs.append(dbname)
            sqldumpprocargs.append(">")
            sqldumpprocargs.append(filedest)
            
            sqldumpproc.start("cmd",sqldumpprocargs)
        
        sqldumpproc.waitForFinished()
        
    def import_database(self, dbname, filesrc):
        sqlimportproc=QtCore.QProcess()
        
        if platform.system() == "Linux":
            sqlimportproc.start("bash -c \"mysql -uroot " + dbname + " < " + filesrc + "\"")
        
        elif platform.system() == "Windows":
            sqlimportprocargs=QtCore.QStringList()
            sqlimportprocargs.append("/c")
            sqlimportprocargs.append("mysqldump")
            sqlimportprocargs.append("-uroot")
            sqlimportprocargs.append(dbname)
            sqlimportprocargs.append("<")
            sqlimportprocargs.append(filesrc)
            sqlimportproc.start("cmd",sqlimportprocargs)
            
        sqlimportproc.waitForFinished()
        
    def list_database(self):
        self.procArgs()
        
        self.sqlArgs.append("show databases;")
        self.procExec()
        
        result=QtCore.QStringList()
        result=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
        return result
        
    def delete_default(self):
        self.delete_database("performance_schema")
        self.delete_database("mysql")
        self.delete_database("test")
        
    def create_table(self, dbname):
        self.procArgs()
        
        tblargs=QtCore.QString()
        
        tblargs += "use " + dbname +";"
        tblargs +=  "create table main_data("
        tblargs += "id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        tblargs += "tanggal DATE NOT NULL,"
        tblargs += "transaksi VARCHAR(32) NOT NULL,"
        tblargs += "harga VARCHAR(32) NOT NULL,"
        tblargs += "jenis INT NOT NULL,"
        tblargs += "debet INT NOT NULL,"
        tblargs += "kredit INT NOT NULL"
        tblargs += ")"
        
        self.sqlArgs.append(tblargs)
        self.procExec()
        
#======================================================================================================

    def data_insert(self, dbname, tanggal, deskrip, nilai, jenis, debet,kredit):
        self.procArgs()
        
        insargs=QtCore.QString()
        insargs += "use " + dbname +";"
        insargs += "insert into `main_data` (`id`,`tanggal`,`transaksi`,`harga`,`jenis`,`debet`,`kredit`) VALUES (NULL,"
        insargs += "\"" + tanggal + "\"" + ","
        insargs += "\"" + deskrip + "\"" + ","
        insargs += "\"" + nilai + "\"" + ","
        insargs += "\"" + QtCore.QString.number(jenis) + "\"" + ","
        insargs += "\"" + QtCore.QString.number(debet) + "\"" + ","
        insargs += "\"" + QtCore.QString.number(kredit) + "\"" + ")"
        
        self.sqlArgs.append(insargs)
        self.procExec()
        
    def data_update(self, dbname, dataid, tanggal, deskrip, nilai, jenis, debet, kredit):
        self.procArgs()
        
        updargs=QtCore.QString()
        updargs += "use " + dbname +";"
        updargs += "update main_data set "
        updargs += "tanggal=\"" + tanggal + "\"" + ","
        updargs += "transaksi=\"" + deskrip + "\"" + ","
        updargs += "harga=\"" + nilai + "\"" + ","
        updargs += "jenis=\"" + QtCore.QString.number(jenis) + "\"" + ","
        updargs += "debet=\"" + QtCore.QString.number(debet) + "\"" + ","
        updargs += "kredit=\"" + QtCore.QString.number(kredit) + "\"" + " "
        updargs += "where id=\"" + dataid  + "\""
        
        self.sqlArgs.append(updargs)
        self.procExec()
        
    def data_delete(self, dbname, dataid):
        self.procArgs()
        
        delargs=QtCore.QString()
        delargs += "use " + dbname +";"
        delargs += "delete from main_data "
        delargs += "where id=\"" + dataid  + "\""
        
        self.sqlArgs.append(delargs)
        self.procExec()
        
#======================================================================================================

    def data_get_one_column(self, dbname, field):
        self.procArgs()
        
        getargs=QtCore.QString()
        getargs += "use " + dbname +";"
        getargs += "select " + field + " from main_data"
        
        self.sqlArgs.append(getargs)
        self.procExec()
        
        result=QtCore.QStringList()
        result=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
        return result
        
    def data_get_one_column_search(self,  dbname,field,search_field,search_string):
        self.procArgs()
        
        searchargs=QtCore.QString()
        searchargs += "use " + dbname +";"
        searchargs += "select " + field + " from main_data where " + search_field + " like " + "\"%" + search_string + "%\"";
        
        self.sqlArgs.append(searchargs)
        self.procExec()
        
        result=QtCore.QStringList()
        result=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
        return result
        
    def data_get_one(self, dbname, field, dataid):
        self.procArgs()
        
        getargs=QtCore.QString()
        getargs += "use " + dbname +";"
        getargs += "select " + field + " from main_data where id=" + "\"" + dataid + "\""
        
        self.sqlArgs.append(getargs)
        self.procExec()

        result_sum=QtCore.QStringList()
        result=QtCore.QString()
        result_sum=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)

        result=result_sum[0]        
        return result
