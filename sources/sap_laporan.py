# -*- coding: utf-8 -*-

import platform
from PyQt4 import QtCore
from sap_storage import SAP_storage

# available accessible variable
# self.penjualan
# self.total_biaya
# self.laba
# self.str_laba
# self.invest 
# self.modal_akhir
# self.kas_in
# self.kas_akhir
# self.kas_tangan
# self.kas_bank
# self.peralatan
# self.aset
# self.pinjaman
# self.kewajiban

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
        
        tblreport=QtCore.QProcess()
        tblreportarg=QtCore.QStringList()
    
        if platform.system() == "Linux":
            tblreportarg.append(str(self.penjualan))
            tblreportarg.append(str(self.total_biaya))
            tblreportarg.append(str(self.laba))
            tblreportarg.append(self.str_laba)
            tblreport.startDetached("./tblreport/pendapatan.py",tblreportarg)
        elif platform.system() == "Windows":
            tblreportarg.append("tblreport\pendapatan.py")
            tblreportarg.append(str(self.penjualan))
            tblreportarg.append(str(self.total_biaya))
            tblreportarg.append(str(self.laba))
            tblreportarg.append(self.str_laba)
            tblreport.startDetached("pythonw",tblreportarg)
            
#======================================================================================================

    def modal(self, dbname):
        self.pendapatan(dbname)
        
        str_invest = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "kredit", "nama","modal")
        self.invest = long(str_invest)
        
        self.modal_akhir = self.invest + self.laba
        
    def view_modal(self, dbname):
        self.modal(dbname)
        
        tblreport=QtCore.QProcess()
        tblreportarg=QtCore.QStringList()
        
        if platform.system() == "Linux":
            tblreportarg.append(str(self.invest))
            tblreportarg.append(str(self.laba))
            tblreportarg.append(str(self.modal_akhir))
            tblreport.startDetached("./tblreport/modal.py",tblreportarg)
        elif platform.system() == "Windows":
            tblreportarg.append("tblreport\modal.py")
            tblreportarg.append(str(self.invest))
            tblreportarg.append(str(self.laba))
            tblreportarg.append(str(self.modal_akhir))
            tblreport.startDetached("pythonw",tblreportarg)

#======================================================================================================

    def kas(self, dbname):
        self.modal(dbname)
        
        self.kas_in = self.penjualan + self.invest
        self.kas_akhir = self.laba + self.invest
        
    def view_kas(self, dbname):
        self.kas(dbname)
        
        tblreport=QtCore.QProcess()
        tblreportarg=QtCore.QStringList()
        
        if platform.system() == "Linux":
            tblreportarg.append(str(self.invest))
            tblreportarg.append(str(self.penjualan))
            tblreportarg.append(str(self.kas_in))
            
            tblreportarg.append(str(self.total_biaya))
                        
            tblreportarg.append(str(self.laba))
            tblreportarg.append(str(self.kas_akhir))
            
            tblreport.startDetached("./tblreport/kas.py",tblreportarg)
        elif platform.system() == "Windows":
            tblreportarg.append("tblreport\kas.py")
            
            tblreportarg.append(str(self.invest))
            tblreportarg.append(str(self.penjualan))
            tblreportarg.append(str(self.kas_in))
            
            tblreportarg.append(str(self.total_biaya))
                        
            tblreportarg.append(str(self.laba))
            tblreportarg.append(str(self.kas_akhir))
            
            tblreport.startDetached("pythonw",tblreportarg)
        
#======================================================================================================

    def neraca(self, dbname):
        self.kas(dbname)
        
        str_kas_tangan = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "saldo", "nama","kas di tangan")
        str_kas_bank = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "saldo", "nama","kas di bank")
        str_peralatan= "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "saldo", "nama","peralatan")
        
        self.kas_tangan = long(str_kas_tangan)
        self.kas_bank = long(str_kas_bank)
        self.peralatan = long(str_peralatan)
        
        self.aset = self.kas_tangan + self.kas_bank + self.peralatan
        
        str_pinjaman = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "saldo", "nama","pinjaman")
        self.pinjaman = long(str_pinjaman)
        
        self.kewajiban = self.pinjaman + self.modal_akhir
        
    def view_neraca(self, dbname):
        self.neraca(dbname)
        
        tblreport=QtCore.QProcess()
        tblreportarg=QtCore.QStringList()
        
        if platform.system() == "Linux":
            tblreportarg.append(str(self.kas_tangan))
            tblreportarg.append(str(self.kas_bank))
            tblreportarg.append(str(self.peralatan))
            tblreportarg.append(str(self.aset))
            
            tblreportarg.append(str(self.modal_akhir))
            tblreportarg.append(str(self.pinjaman))
            tblreportarg.append(str(self.kewajiban))
            
            tblreport.startDetached("./tblreport/neraca.py",tblreportarg)
        elif platform.system() == "Windows":
            tblreportarg.append("tblreport\\neraca.py")
            
            tblreportarg.append(str(self.kas_tangan))
            tblreportarg.append(str(self.kas_bank))
            tblreportarg.append(str(self.peralatan))
            tblreportarg.append(str(self.aset))
            
            tblreportarg.append(str(self.modal_akhir))
            tblreportarg.append(str(self.pinjaman))
            tblreportarg.append(str(self.kewajiban))
            
            tblreport.startDetached("pythonw",tblreportarg)
