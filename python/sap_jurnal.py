# -*- coding: utf-8 -*-

from PyQt4 import QtCore

class SAP_jurnal(object):
    def __init__ (self):
        pass
        
    def txtlst_debet(self):
        debet=QtCore.QStringList()
        debet.append("-- pilih salah satu --")
        debet.append("kas di tangan")
        debet.append("peralatan")
        debet.append("biaya listrik")
        debet.append("biaya telepon")
        debet.append("biaya gaji")
        debet.append("kas di bank")
        return debet
        
    def txtlst_kredit(self):
        kredit=QtCore.QStringList()
        kredit.append("-- pilih salah satu --")
        kredit.append("modal")
        kredit.append("penjualan")
        kredit.append("kas di tangan")
        kredit.append("pinjaman")
        return kredit
        
    def txtlst_kredit_debet(self, debet):
        kredit=QtCore.QStringList()
        
        if debet == "-- pilih salah satu --":
            kredit.append("-- pilih salah satu debet --")
        elif debet == "kas di tangan":
            kredit.append("modal")
            kredit.append("penjualan")
        elif debet == "peralatan":
            kredit.append("kas di tangan")
        elif debet == "biaya listrik":
            kredit.append("kas di tangan")
        elif debet == "biaya telepon":
            kredit.append("kas di tangan")
        elif debet == "biaya gaji":
            kredit.append("kas di tangan")
        elif debet == "kas di bank":
            kredit.append("kas di tangan")
            kredit.append("pinjaman")
        
        return kredit
        
#======================================================================================================

    def int_debet(self, debet):
        if debet == "kas di tangan":
            result = 1
        elif debet == "peralatan":
            result = 2
        elif debet == "biaya listrik":
            result = 3
        elif debet == "biaya telepon":
            result = 4
        elif debet == "biaya gaji":
            result = 5
        elif debet == "kas di bank":
            result = 6
        return result
        
    def int_kredit(self, kredit):
        if kredit == "modal":
            result=1
        elif kredit == "penjualan":
            result=2
        elif kredit == "kas di tangan":
            result=3
        elif kredit == "pinjaman":
            result=4
        return result
        
