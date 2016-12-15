#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class TableView(QtGui.QTableWidget):
    def __init__(self, penjualan,biaya, laba, str_laba,  *args):
        QtGui.QTableWidget.__init__(self, *args)
        
        tabellabel=QtCore.QStringList()
        tabellabel.append("Deksripsi")
        tabellabel.append("Nilai")
        
        self.column_number=tabellabel.count()
        self.setColumnCount(self.column_number)

        self.setColumnWidth(0,200)
        self.setColumnWidth(1,100)
        
        self.setFixedWidth(300)
        self.setFixedHeight(180)
        
        self.setHorizontalHeaderLabels(tabellabel)
        self.setWindowTitle("Laporan Pendapatan")
        
        self.view_data(penjualan,biaya, laba, str_laba)
        
    def view_data(self, penjualan,biaya, laba, str_laba):
        self.setRowCount(4)
        
        isi = QtGui.QTableWidgetItem("Penjualan")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(0, 0, isi)
        
        isi = QtGui.QTableWidgetItem(penjualan)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(0, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Biaya")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(1, 0, isi)
        
        isi = QtGui.QTableWidgetItem(biaya)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(1, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Laba")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(2, 0, isi)
        
        isi = QtGui.QTableWidgetItem(laba)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(2, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Hasil")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(3, 0, isi)
        
        isi = QtGui.QTableWidgetItem(str_laba)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(3, 1, isi)
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app =TableView(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    my_app.show()
    sys.exit(app.exec_())
