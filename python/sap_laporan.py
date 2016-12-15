# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore
from sap_storage import SAP_storage

class SAP_laporan(object):
    def __init__ (self):
        self.my_storage = SAP_storage()
        
    def pendapatan(self, dbname):
        str_penjualan = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "kredit", "nama","penjualan")
        self.penjualan = long(str_penjualan)
        
        str_biaya_listrik = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya listrik")
        str_biaya_telepon = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya telepon")
        str_biaya_gaji = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya gaji")
        self.total_biaya = long(str_biaya_listrik) + long(str_biaya_telepon) + long(str_biaya_gaji)
        
        if self.penjualan > self.total_biaya:
            self.laba = self.penjualan - self.total_biaya
            self.str_laba = "Untung"
        elif self.penjualan < self.total_biaya:
            self.laba = self.total_biaya - self.penjualan
            self.str_laba = "Rugi"
        else:
            self.laba = 0
            self.str_laba = "Impas"
            
    def view_pendapatan(self, dbname):
        self.pendapatan(dbname)
        
        tblview=QtCore.QProcess()
        tblviewarg=QtCore.QStringList()
    
        if platform.system() == "Linux":
            tblviewarg.append(str(self.penjualan))
            tblviewarg.append(str(self.total_biaya))
            tblviewarg.append(str(self.laba))
            tblviewarg.append(self.str_laba)
            tblview.startDetached("./tblview/pendapatan.py",tblviewarg)
        elif platform.system() == "Windows":
            tblviewarg.append("tblview\pendapatan.py")
            tblviewarg.append(str(self.penjualan))
            tblviewarg.append(str(self.total_biaya))
            tblviewarg.append(str(self.laba))
            tblviewarg.append(self.str_laba)
            tblview.startDetached("pythonw",tblviewarg)
            
#======================================================================================================

    def modal(self, dbname):
        self.pendapatan(dbname)
        
        str_invest = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "kredit", "nama","modal")
        self.invest = long(str_invest)
        
    def view_modal(self, dbname):
        self.modal(dbname)
        
        tblview=QtCore.QProcess()
        tblviewarg=QtCore.QStringList()
        
        if platform.system() == "Linux":
            tblviewarg.append(str(self.invest))
            tblviewarg.append(str(self.laba))
            tblview.startDetached("./tblview/modal.py",tblviewarg)
        elif platform.system() == "Windows":
            tblviewarg.append("tblview\modal.py")
            tblviewarg.append(str(self.invest))
            tblviewarg.append(str(self.laba))
            tblview.startDetached("pythonw",tblviewarg)
