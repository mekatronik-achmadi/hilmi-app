# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore
from sap_storage import SAP_storage

class SAP_laporan(object):
    def __init__ (self):
        self.my_storage = SAP_storage()
        
    def pendapatan(self, dbname):
        str_penjualan = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "kredit", "nama","penjualan")
        penjualan = long(str_penjualan)
        
        str_biaya_listrik = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya listrik")
        str_biaya_telepon = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya telepon")
        str_biaya_gaji = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya gaji")
        total_biaya = long(str_biaya_listrik) + long(str_biaya_telepon) + long(str_biaya_gaji)
        
        
        if penjualan > total_biaya:
            laba = penjualan - total_biaya
            str_laba = "Untung"
        elif penjualan < total_biaya:
            laba = total_biaya - penjualan
            str_laba = "Rugi"
        else:
            laba = 0
            str_laba = "Impas"
            
        self.view_pendapatan(penjualan, total_biaya, laba, str_laba)
            
    def view_pendapatan(self, penjualan, biaya, laba, str_laba):
        tblview=QtCore.QProcess()
        tblviewarg=QtCore.QStringList()
    
        if platform.system() == "Linux":
            tblviewarg.append(str(penjualan))
            tblviewarg.append(str(biaya))
            tblviewarg.append(str(laba))
            tblviewarg.append(str_laba)
            tblview.startDetached("./tblview/pendapatan.py",tblviewarg)
        elif platform.system() == "Windows":
            tblviewarg.append(str(penjualan))
            tblviewarg.append(str(biaya))
            tblviewarg.append(str(laba))
            tblviewarg.append(str_laba)
            tblview.startDetached("pythonw",tblviewarg)
