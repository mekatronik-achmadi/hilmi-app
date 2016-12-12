# -*- coding: utf-8 -*-

import platform
import MySQLdb
from MySQLdb.release import __version__ as MySQLdbVer
from PyQt4 import QtCore, QtGui

class SQL_handler(object):
    def __init__ (self):
        
        self.txtProcOutput=QtGui.QPlainTextEdit()
        self.sqlProc=QtCore.QProcess()
        QtCore.QObject.connect(self.sqlProc, QtCore.SIGNAL("readyReadStandardOutput()"), self.processOnGoing)
         
    def processOnGoing(self):
        newData= QtCore.QByteArray()
        newData= self.sqlProc.readAllStandardOutput()
        self.txtProcOutput.appendPlainText(QtCore.QString.fromLocal8Bit(newData))
        
#======================================================================================================

    def procSqlVersion(self):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        cur.execute("select version()")
        data = cur.fetchone()
        
        cur.close()
        db.close()
        result = "%s" % data
        return result
        
    def procDriverVersion(self):
        result = MySQLdbVer
        return result
        
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
            sqlimportprocargs.append("mysql")
            sqlimportprocargs.append("-uroot")
            sqlimportprocargs.append(dbname)
            sqlimportprocargs.append("<")
            sqlimportprocargs.append(filesrc)
            sqlimportproc.start("cmd",sqlimportprocargs)
            
        sqlimportproc.waitForFinished()
        
#======================================================================================================
            
    def create_database(self, dbname):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        dbargs = "create database %s" % dbname
        cur.execute(dbargs)
        
        cur.close()
        db.close()
        
    def delete_database(self, dbname):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        dbargs = "drop database %s" % dbname
        cur.execute(dbargs)
        
        cur.close()
        db.close()
        
#======================================================================================================
        
    def list_database(self):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        dbargs = "show databases"
        cur.execute(dbargs)
        
        result_all=cur.fetchall()
        
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
                result.append(rowdata[0])
                
        cur.close()
        db.close()
        
        return result
        
    def create_table(self, dbname):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        tblargs = """create table main_data(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        tanggal DATE NOT NULL,
                        transaksi VARCHAR(32) NOT NULL,
                        harga VARCHAR(32) NOT NULL,
                        jenis INT NOT NULL,
                        debet INT NOT NULL,
                        kredit INT NOT NULL
                        )"""
        cur.execute(tblargs)
        
        cur.close()
        db.close()
        
#======================================================================================================

    def data_insert(self, dbname, tanggal, deskrip, nilai, jenis, debet,kredit):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        insargs = "insert into main_data (id,tanggal,transaksi,harga,jenis,debet,kredit) values (NULL,'%s','%s','%s','%s','%s','%s')" % (
            tanggal,
            deskrip, 
            nilai, 
            QtCore.QString.number(jenis), 
            QtCore.QString.number(debet), 
            QtCore.QString.number(kredit))
        cur.execute(insargs)
        db.commit()
        
        cur.close()
        db.close()
        
    def data_update(self, dbname, dataid, tanggal, deskrip, nilai, jenis, debet, kredit):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        updargs = "update main_data set tanggal= '%s',transaksi='%s',harga='%s',jenis='%s',debet='%s',kredit='%s' where id='%s'" % (
            tanggal, 
            deskrip, 
            nilai, 
            QtCore.QString.number(jenis), 
            QtCore.QString.number(debet), 
            QtCore.QString.number(kredit), 
            dataid)
        cur.execute(updargs)
        db.commit()
        
        cur.close()
        db.close()
        
    def data_delete(self, dbname, dataid):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        delargs = "delete from main_data where id='%s'" % dataid
        cur.execute(delargs)
        db.commit()
        
        cur.close()
        db.close()
        
#======================================================================================================

    def data_get_one_column(self, dbname, field):
        self.procArgs()
        
        getargs = "use " + dbname +";"
        getargs += "select " + field + " from main_data"
        
        self.sqlArgs.append(getargs)
        self.procExec()
        
        result=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
        return result
        
    def data_get_one_column_search(self,  dbname,field,search_field,search_string):
        self.procArgs()
        
        searchargs = "use " + dbname +";"
        searchargs += "select " + field + " from main_data where " + search_field + " like " + "\"%" + search_string + "%\"";
        
        self.sqlArgs.append(searchargs)
        self.procExec()
        
        result=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)
        return result
        
    def data_get_one(self, dbname, field, dataid):
        self.procArgs()
        
        getargs = "use " + dbname +";"
        getargs += "select " + field + " from main_data where id=" + "\"" + dataid + "\""
        
        self.sqlArgs.append(getargs)
        self.procExec()

        result_sum=self.txtProcOutput.toPlainText().split(QtCore.QRegExp("\n"),QtCore.QString.SkipEmptyParts)

        result=result_sum[0]        
        return result
