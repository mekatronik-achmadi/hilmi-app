#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class TableView(QtGui.QTableWidget):
    def __init__(self,kas_tangan, kas_bank,peralatan, aset, modal, pinjaman,kewajiban, *args):
        QtGui.QTableWidget.__init__(self, *args)
        
        tabellabel=QtCore.QStringList()
        tabellabel.append("Deksripsi")
        tabellabel.append("Nilai")
        
        self.column_number=tabellabel.count()
        self.setColumnCount(self.column_number)

        self.setColumnWidth(0,150)
        self.setColumnWidth(1,100)
        
        self.setFixedWidth(300)
        self.setFixedHeight(350)
        
        self.setHorizontalHeaderLabels(tabellabel)
        self.setWindowTitle("Neraca")
        
        self.view_data(kas_tangan, kas_bank,peralatan, aset, modal, pinjaman,kewajiban)
        
    def view_data(self, kas_tangan, kas_bank,peralatan, aset, modal, pinjaman,kewajiban):
        self.setRowCount(10)
        
        isi = QtGui.QTableWidgetItem("Aset")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(0, 0, isi)
        isi = QtGui.QTableWidgetItem(" ")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(0, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Kas di Tangan")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(1, 0, isi)
        isi = QtGui.QTableWidgetItem(kas_tangan)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(1, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Kas di Bank")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(2, 0, isi)
        isi = QtGui.QTableWidgetItem(kas_bank)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(2, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Peralatan")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(3, 0, isi)
        isi = QtGui.QTableWidgetItem(kas_bank)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(3, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Total Aset")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(4, 0, isi)
        isi = QtGui.QTableWidgetItem(aset)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(4, 1, isi)
        
        isi = QtGui.QTableWidgetItem(" ")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(5, 0, isi)
        isi = QtGui.QTableWidgetItem(" ")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(5, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Kewajiban")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(6, 0, isi)
        isi = QtGui.QTableWidgetItem(" ")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(6, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Modal")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(7, 0, isi)
        isi = QtGui.QTableWidgetItem(modal)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(7, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Pinjaman")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(8, 0, isi)
        isi = QtGui.QTableWidgetItem(pinjaman)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(8, 1, isi)
        
        isi = QtGui.QTableWidgetItem("Total Kewajiban")
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(9, 0, isi)
        isi = QtGui.QTableWidgetItem(kewajiban)
        isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
        self.setItem(9, 1, isi)
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app =TableView(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    my_app.show()
    sys.exit(app.exec_())
