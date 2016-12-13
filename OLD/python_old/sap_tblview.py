#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from sql_handler import SQL_handler
from sap_data import SAP_data

class Table_View(QtGui.QTableWidget):
    def __init__(self, dbase, *args):
        QtGui.QTableWidget.__init__(self, *args)
        
        self.mysql= SQL_handler()
        self.mydata=SAP_data()
        
        self.setColumnCount(7)

        self.setColumnWidth(0,50)
        self.setColumnWidth(1,100)
        self.setColumnWidth(2,200)
        self.setColumnWidth(3,100)
        self.setColumnWidth(4,200)
        self.setColumnWidth(5,150)
        self.setColumnWidth(6,150)
        
        self.setFixedWidth(1000)
        self.setFixedHeight(500)
        
        tabellabel=QtCore.QStringList()
        tabellabel.append("ID")
        tabellabel.append("Tanggal")
        tabellabel.append("Transaksi")
        tabellabel.append("Harga")
        tabellabel.append("Jenis")
        tabellabel.append("Debet")
        tabellabel.append("Kredit")
        
        self.setHorizontalHeaderLabels(tabellabel)
        self.setWindowTitle("Rekap Data")
        
        self.setsqldata(dbase)
        
    def setsqldata(self, dbase):
        datid=self.mysql.data_get_one_column(dbase,"id")        
        self.setRowCount(datid.count())
        for i in range(0, datid.count()):
            isi = QtGui.QTableWidgetItem(datid[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,0,isi)
        
        dattanggal=self.mysql.data_get_one_column(dbase,"tanggal")
        for i in range(0,datid.count()):
            isi = QtGui.QTableWidgetItem(dattanggal[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,1,isi)
            
        dattransaksi=self.mysql.data_get_one_column(dbase,"transaksi")
        for i in range(0, datid.count()):
            isi = QtGui.QTableWidgetItem(dattransaksi[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,2,isi)
        
        datharga=self.mysql.data_get_one_column(dbase,"harga")
        for i in range(0, datid.count()):
            isi = QtGui.QTableWidgetItem(datharga[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,3,isi)
        
        datjenis=self.mysql.data_get_one_column(dbase,"jenis")
        for i in range(0, datid.count()):
            jenis_num = datjenis[i]
            isi = QtGui.QTableWidgetItem(self.mydata.jenis2text(jenis_num.toInt()[0]))
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,4,isi)
            
        datdebet=self.mysql.data_get_one_column(dbase,"debet")
        for i in range(0, datid.count()):
            debet_num = datdebet[i]
            isi = QtGui.QTableWidgetItem(self.mydata.debet2text(debet_num.toInt()[0]))
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,5,isi)
            
        datkredit=self.mysql.data_get_one_column(dbase,"kredit")
        for i in range(0, datid.count()):
            kredit_num = datkredit[i]
            isi = QtGui.QTableWidgetItem(self.mydata.kredit2text(kredit_num.toInt()[0]))
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
            self.setItem(i,6,isi)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    tabelview =Table_View(sys.argv[1])
    tabelview.show()
    sys.exit(app.exec_())
