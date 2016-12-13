# -*- coding: utf-8 -*-

import platform
import MySQLdb
from MySQLdb.release import __version__
from PyQt4 import QtCore

class SAP_storage(object):
    def __init__ (self):
        self.driver_version = __version__
        
#======================================================================================================
        
    def sql_version(self):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        cur.execute("select version()")
        data = cur.fetchone()
        
        cur.close()
        db.close()
        result = "%s" % data
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

    def show_databases(self):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        dbargs = "show databases"
        cur.execute(dbargs)
        result=cur.fetchall()
                
        cur.close()
        db.close()
        
        return result
        
    def create_database(self, dbname):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        dbargs = "create database %s" % dbname
        cur.execute(dbargs)
        
        cur.close()
        db.close()
        
    def drop_database(self, dbname):
        db = MySQLdb.connect("localhost","root","")
        cur = db.cursor()
        
        dbargs = "drop database %s" % dbname
        cur.execute(dbargs)
        
        cur.close()
        db.close()
        
#======================================================================================================
        
    def create_tbl_jurnal(self, dbname):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        tblargs = """create table tabel_jurnal(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        tanggal DATE NOT NULL,
                        transaksi VARCHAR(32) NOT NULL,
                        harga VARCHAR(32) NOT NULL,
                        debet VARCHAR(32) NOT NULL,
                        kredit VARCHAR(32) NOT NULL
                        )"""
        cur.execute(tblargs)
        
        cur.close()
        db.close()
        
    def insert_tbl_jurnal(self, dbname, tanggal, deskrip, nilai, debet,kredit):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        insargs = "insert into tabel_jurnal (id,tanggal,transaksi,harga,debet,kredit) values (NULL,'%s','%s','%s','%s','%s')" % (
            tanggal,
            deskrip, 
            nilai, 
            debet, 
            kredit)
        cur.execute(insargs)
        db.commit()
        
        cur.close()
        db.close()
        
    def update_tbl_jurnal(self, dbname, dataid, tanggal, deskrip, nilai, debet,kredit):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        updargs = "update tabel_jurnal set tanggal= '%s',transaksi='%s',harga='%s',debet='%s',kredit='%s' where id='%s'" % (
            tanggal, 
            deskrip, 
            nilai, 
            debet, 
            kredit, 
            dataid)
        cur.execute(updargs)
        db.commit()
        
        cur.close()
        db.close()
        
    def delete_tbl_jurnal(self, dbname, dataid):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        delargs = "delete from tabel_jurnal where id='%s'" % dataid
        cur.execute(delargs)
        db.commit()
        
        cur.close()
        db.close()
        
    def search_tbl_jurnal(self, dbname, dataid):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        getargs = "select * from tabel_jurnal where id='%s'" % dataid
        cur.execute(getargs)
        result=cur.fetchall()

        return result

#======================================================================================================

    def create_tbl_akun(self, dbname):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        tblargs = """create table tabel_akun(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        kode VARCHAR(32) NOT NULL,
                        nama VARCHAR(32) NOT NULL,
                        debet VARCHAR(32) NOT NULL,
                        kredit VARCHAR(32) NOT NULL
                        )"""
        cur.execute(tblargs)
        
        cur.close()
        db.close()
        
    def reset_tbl_akun(self, dbname):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        rstargs = "truncate tabel_akun"
        cur.execute(rstargs)
        
        cur.close()
        db.close()
        
    def column_harga_jurnal(self, dbname, str_debkre,  str_search):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        getargs= "select harga from tabel_jurnal where %s='%s'" % (str_debkre,  str_search)
        cur.execute(getargs)
        
        result = cur.fetchall()
        
        cur.close()
        db.close()
        
        return result
            
        
        
        
