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
        
    def create_tabel(self, dbname):
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
        
        tblargs = """create table tabel_akun(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        kode VARCHAR(32) NOT NULL,
                        nama VARCHAR(32) NOT NULL,
                        debet VARCHAR(32) NOT NULL,
                        kredit VARCHAR(32) NOT NULL,
                        saldo VARCHAR(32) NOT NULL
                        )"""
        cur.execute(tblargs)
        
        cur.close()
        db.close()
        
    def reset_tabel(self, dbname, tblname):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        rstargs = "truncate %s" % tblname
        cur.execute(rstargs)
        
        cur.close()
        db.close()
        
#======================================================================================================
        
    def tabel_column(self, dbname, tblname, str_field, str_column,  str_search):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        getargs= "select %s from %s where %s='%s'" % (str_field,  tblname,  str_column,  str_search)
        cur.execute(getargs)
        
        result = cur.fetchall()
        
        cur.close()
        db.close()
        
        return result
        
    def tabel_row(self, dbname, tblname, str_field, str_column,  str_search):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        getargs= "select %s from %s where %s='%s'" % (str_field,  tblname,  str_column,  str_search)
        cur.execute(getargs)
        
        result = cur.fetchone()
        
        cur.close()
        db.close()
        
        return result
        
#======================================================================================================
        
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
        
    def insert_tbl_akun(self, dbname, kode, nama, debet,kredit, saldo):
        db = MySQLdb.connect("localhost","root","", str(dbname))
        cur = db.cursor()
        
        insargs = "insert into tabel_akun (id,kode,nama,debet,kredit,saldo) values (NULL,'%s','%s','%s','%s','%s')" % (
            kode, 
            nama, 
            debet, 
            kredit, 
            saldo)
        cur.execute(insargs)
        db.commit()
        
        cur.close()
        db.close()
        
#======================================================================================================
        
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
