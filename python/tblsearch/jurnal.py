#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import MySQLdb
from PyQt4 import QtCore, QtGui

class TableSearch(QtGui.QTableWidget):
    def __init__(self, dbase, search_field, search_string, *args):
        QtGui.QTableWidget.__init__(self, *args)
        
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
        
        self.column_number=tabellabel.count()
        self.setColumnCount(self.column_number)

        self.setColumnWidth(0,50)
        self.setColumnWidth(1,100)
        self.setColumnWidth(2,200)
        self.setColumnWidth(3,100)
        self.setColumnWidth(4,200)
        self.setColumnWidth(5,150)
        self.setColumnWidth(6,150)
        
        self.setFixedWidth(1000)
        self.setFixedHeight(500)
        
        self.sqlquery = "select * from tabel_jurnal where %s like '%%%s%%'" % (search_field,search_string)
        self.get_data(dbase)
        self.view_data()
        
    def get_data(self, dbase):
        db = MySQLdb.connect("localhost","root","",str(dbase) )
        cur = db.cursor()
        cur.execute(self.sqlquery)
        self.result = cur.fetchall()
        self.row_number=cur.rowcount
        cur.close()
        db.close()
        
    def view_data(self):
        self.setRowCount(self.row_number)
        for i in range(0, self.row_number):
            for j in range(0, self.column_number):
                isi = QtGui.QTableWidgetItem(str(self.result[i][j]))
                isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable )
                self.setItem(i,j,isi)
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app =TableSearch(sys.argv[1], sys.argv[2], sys.argv[3])
    my_app.show()
    sys.exit(app.exec_())
