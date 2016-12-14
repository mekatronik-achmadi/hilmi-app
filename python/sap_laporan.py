# -*- coding: utf-8 -*-

from sap_storage import SAP_storage

class SAP_laporan(object):
    def __init__ (self):
        self.my_storage = SAP_storage()
        
    def pendapatan(self, dbname):
        str_penjualan = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "kredit", "nama","penjualan")
        penjualan = long(str_penjualan)
        print "Penjualan = %i" % penjualan
        
        print "======================"
        
        str_biaya_listrik = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya listrik")
        str_biaya_telepon = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya telepon")
        str_biaya_gaji = "%s" % self.my_storage.tabel_row(dbname, "tabel_akun", "debet", "nama","biaya gaji")
        total_biaya = long(str_biaya_listrik) + long(str_biaya_telepon) + long(str_biaya_gaji)
        print "Biaya = %i" % total_biaya
        
        print "======================"
        
        if penjualan > total_biaya:
            laba = penjualan - total_biaya
            print "Untung = %i" % laba
            
        elif penjualan < total_biaya:
            rugi = total_biaya - penjualan
            print "Rugi = %i" % rugi
            
        elif penjualan == total_biaya:
            print "Impas"
        
