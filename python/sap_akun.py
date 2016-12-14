# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore
from sap_storage import SAP_storage

class SAP_akun(object):
    def __init__ (self):
        self.my_storage = SAP_storage()
        
        self.nama_akun = QtCore.QStringList()
        self.nama_akun.append("kas di tangan")
        self.nama_akun.append("kas di bank")
        self.nama_akun.append("peralatan")
        self.nama_akun.append("penjualan")
        self.nama_akun.append("biaya listrik")
        self.nama_akun.append("biaya telepon")
        self.nama_akun.append("biaya gaji")
        self.nama_akun.append("modal")
        self.nama_akun.append("pinjaman")
        
        self.kode_akun =  QtCore.QStringList()
        self.kode_akun.append("101")
        self.kode_akun.append("102")
        self.kode_akun.append("201")
        self.kode_akun.append("301")
        self.kode_akun.append("401")
        self.kode_akun.append("402")
        self.kode_akun.append("404")
        self.kode_akun.append("501")
        self.kode_akun.append("505")
        
    def refresh_tbl_akun(self, dbname):
        self.reset_tbl_akun(dbname)
        self.build_tbl_akun(dbname)
        
    def reset_tbl_akun(self, dbname):
        self.my_storage.reset_tabel(dbname,  "tabel_akun")
        
    def build_tbl_akun(self, dbname):
        for i in range(0, self.nama_akun.count()):
            debet_all = self.my_storage.tabel_column(dbname, "tabel_jurnal", "harga", "debet",self.nama_akun[i])
            debet=0
            if all(debet_all):
                for rowdata in debet_all:
                    str_debet = "%s" % rowdata
                    debet = debet + long(str_debet)
            
            kredit_all = self.my_storage.tabel_column(dbname, "tabel_jurnal", "harga", "kredit", self.nama_akun[i])
            kredit=0
            if all(kredit_all):
                for rowdata in kredit_all:
                    str_kredit = "%s" % rowdata
                    kredit = kredit + long(str_kredit)
            
            saldo=0
            if debet > kredit:
                saldo = debet - kredit
            elif kredit > debet:
                saldo = kredit - debet
                
            self.my_storage.insert_tbl_akun(dbname, self.kode_akun[i],self.nama_akun[i], debet,kredit, saldo)
            
    def view_tabel(self, dbase):
        tblview=QtCore.QProcess()
        tblviewarg=QtCore.QStringList()
    
        if platform.system() == "Linux":
            tblviewarg.append(dbase)
            tblview.startDetached("./tblview/akun.py",tblviewarg)
        elif platform.system() == "Windows":
            tblviewarg.append("tblview\akun.py")
            tblviewarg.append(dbase)
            tblview.startDetached("pythonw",tblviewarg)
