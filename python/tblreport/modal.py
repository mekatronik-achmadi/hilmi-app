#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class TableView(QtGui.QTableWidget):
    def __init__(self, invest, laba, akhir, *args):
        QtGui.QTableWidget.__init__(self, *args)
        
        tabellabel=QtCore.QStringList()
        tabellabel.append("Deksripsi")
        tabellabel.append("Nilai")
        
        self.column_number=tabellabel.count()
        self.setColumnCount(self.column_number)

        self.setColumnWidth(0,150)
        self.setColumnWidth(1,100)
        
        self.setFixedWidth(300)
        self.setFixedHeight(120)
        
        self.setHorizontalHeaderLabels(tabellabel)
        self.setWindowTitle("Laporan Modal")
        
        self.view_data(invest, laba, akhir)
        
    def view_data(self, invest, laba, akhir):
        self.setRowCount(3)
        
        isi = QtGui.QTableWidgetItem("Investasi")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(0, 0, isi)
        
        isi = QtGui.QTableWidgetItem(invest)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(0, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Laba")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(1, 0, isi)
        
        isi = QtGui.QTableWidgetItem(laba)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(1, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Modal Akhir")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(2, 0, isi)
        
        isi = QtGui.QTableWidgetItem(akhir)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(2, 1, isi)
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app =TableView(sys.argv[1], sys.argv[2], sys.argv[3])
    my_app.show()
    sys.exit(app.exec_())
