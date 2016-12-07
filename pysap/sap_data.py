# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from sql_driver import SQL_driver

class SAP_data(object):
    def __init__ (self):
        self.mysql=SQL_driver()
        
    def jenis2debet(self, num_jenis):
        result=0
        if num_jenis == 0:result=0
        elif num_jenis == 1:result=0
        elif num_jenis == 2:result=1
        elif num_jenis == 3:result=2
        elif num_jenis == 4:result=1
        elif num_jenis == 5:result=3
        elif num_jenis == 6:result=4
        elif num_jenis == 7:result=4
        elif num_jenis == 8:result=5
        elif num_jenis == 9:result=6
        elif num_jenis == 10:result=2
        elif num_jenis == 11:result=7
        elif num_jenis == 12:result=1
        elif num_jenis == 13:result=8
        elif num_jenis == 14:result=1
        elif num_jenis == 15:result=2
        elif num_jenis == 16:result=1
        elif num_jenis == 17:result=9
        elif num_jenis == 18:result=10
        elif num_jenis == 19:result=11
        elif num_jenis == 20:result=12
        elif num_jenis == 21:result=13
        elif num_jenis == 22:result=14
        elif num_jenis == 23:result=14
        return result
        
    def jenis2kredit(self, num_jenis):
        result=0
        if num_jenis == 0:result=0
        elif num_jenis == 1:result=1
        elif num_jenis == 2:result=2
        elif num_jenis == 3:result=2
        elif num_jenis == 4:result=3
        elif num_jenis == 5:result=3
        elif num_jenis == 6:result=0
        elif num_jenis == 7:result=4
        elif num_jenis == 8:result=0
        elif num_jenis == 9:result=0
        elif num_jenis == 10:result=0
        elif num_jenis == 11:result=0
        elif num_jenis == 12:result=5
        elif num_jenis == 13:result=0
        elif num_jenis == 14:result=1
        elif num_jenis == 15:result=6
        elif num_jenis == 16:result=4
        elif num_jenis == 17:result=0
        elif num_jenis == 18:result=7
        elif num_jenis == 19:result=0
        elif num_jenis == 20:result=8
        elif num_jenis == 21:result=9
        elif num_jenis == 22:result=0
        elif num_jenis == 23:result=3
        return result
        
#======================================================================================================

    def jenis2text(self, num_jenis):
        result=QtCore.QString()
        if num_jenis == 0:result="PEMBELIAN BAHAN BAKU TUNAI"
        elif num_jenis == 1:result="PEMBELIAN BAHAN BAKU KREDIT"
        elif num_jenis == 2:result="RETUR PEMBELIAN TUNAI"
        elif num_jenis == 3:result="RETUR PEMBELIAN KREDIT"
        elif num_jenis == 4:result="PENJUALAN TUNAI"
        elif num_jenis == 5:result="PENJUALAN KREDIT"
        elif num_jenis == 6:result="RETUR PENJUALAN TUNAI"
        elif num_jenis == 7:result="RETUR PENJUALAN KREDIT"
        elif num_jenis == 8:result="PEMBAYARAN GAJI"
        elif num_jenis == 9:result="PEMBAYARAN TELP, AIR & LISTRIK"
        elif num_jenis == 10:result="PEMBAYARAN UTANG MELALUI KAS DI TANGAN"
        elif num_jenis == 11:result="PEMBAYARAN TRANSPORTASI"
        elif num_jenis == 12:result="DISETOR MODAL TUNAI"
        elif num_jenis == 13:result="PENYETORAN TUNAI KE BANK"
        elif num_jenis == 14:result="PINJAMAN DARI BANK"
        elif num_jenis == 15:result="PEMBAYARAN UTANG MELALUI BANK"
        elif num_jenis == 16:result="DITERIMA PEMBAYARAN PIUTANG"
        elif num_jenis == 17:result="DIBELI PERALATAN"
        elif num_jenis == 18:result="DEPRESIASI PERALATAN"
        elif num_jenis == 19:result="SEWA BANGUNAN DIBAYAR DIMUKA"
        elif num_jenis == 20:result="PEMBAYARAN SEWA BANGUNAN"
        elif num_jenis == 21:result="BEBAN GARANSI ESTIMASI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "
        elif num_jenis == 22:result="BEBAN GARANSI REALISASI"
        elif num_jenis == 23:result="BEBAN GARANSI TAK TEREALISASI"
        return result

    def debet2text(self,  num_debet):
        result=QtCore.QString()
        if num_debet == 0:result="PEMBELIAN"
        elif num_debet == 1:result="KAS DI TANGAN"
        elif num_debet == 2:result="UTANG USAHA"
        elif num_debet == 3:result="PIUTANG USAHA"
        elif num_debet == 4:result="RETUR PENJUALAN"
        elif num_debet == 5:result="BEBAN GAJI"
        elif num_debet == 6:result="BEBAN TELP, AIR & LISTRIK"
        elif num_debet == 7:result="BEBAN TRANSPORTASI"
        elif num_debet == 8:result="KAS DI BANK"
        elif num_debet == 9:result="PERALATAN"
        elif num_debet == 10:result="BEBAN PENYUSUTAN PERALATAN"
        elif num_debet == 11:result="SEWA BANGUNAN DI BAYAR DIMUKA"
        elif num_debet == 12:result="BEBAN SEWA BANGUNAN"
        elif num_debet == 13:result="BEBAN GARANSI"
        elif num_debet == 14:result="CADANGAN GARANSI"
        return result
    
    def kredit2text(self,  num_kredit):
        result=QtCore.QString()
        if num_kredit == 0:result="KAS DI TANGAN"
        elif num_kredit == 1:result="UTANG USAHA "
        elif num_kredit == 2:result="RETUR PEMBELIAN "
        elif num_kredit == 3:result="PENJUALAN "
        elif num_kredit == 4:result="PIUTANG USAHA"
        elif num_kredit == 5:result="MODAL PEMILIK "
        elif num_kredit == 6:result="KAS DI BANK"
        elif num_kredit == 7:result="AKUMULASI PENYUSUTAN PERALATAN"
        elif num_kredit == 8:result="SEWA BANGUNAN DIBAYAR DI MUKA"
        elif num_kredit == 9:result="CADANGAN GARANSI"
        return result
        
#======================================================================================================

    def view_table(self, dbase):
        tblview=QtCore.QProcess()
        tblviewarg=QtCore.QStringList()
        
        tblviewarg.append(dbase)
        tblview.startDetached("./sap_tblview.py",tblviewarg)
        
    def view_pdf(self,  dbase):
        fileName=QtCore.QString()
        fileName=QtGui.QFileDialog.getSaveFileName(None,"export PDF",QtCore.QString(),"*.pdf")
        if fileName.isEmpty():
            return
        if QtCore.QFileInfo(fileName).suffix().isEmpty():
            fileName.append(".pdf")
        
        datid = QtCore.QStringList()
        dattanggal = QtCore.QStringList()
        dattransaksi = QtCore.QStringList()
        datharga = QtCore.QStringList()
        datjenis = QtCore.QStringList()
        datdebet = QtCore.QStringList()
        datkredit = QtCore.QStringList()

        datid = self.mysql.data_get_one_column(dbase,"id")
        dattanggal = self.mysql.data_get_one_column(dbase,"tanggal")
        dattransaksi = self.mysql.data_get_one_column(dbase,"transaksi")
        datharga = self.mysql.data_get_one_column(dbase,"harga")
        datjenis = self.mysql.data_get_one_column(dbase,"jenis")
        datdebet = self.mysql.data_get_one_column(dbase,"debet")
        datkredit = self.mysql.data_get_one_column(dbase,"kredit")

        textdata=QtCore.QString()
        for i in range(datid.count()):
            jenis_num = QtCore.QString()
            debet_num = QtCore.QString()
            kredit_num = QtCore.QString()
            
            jenis_num = datjenis[i]
            debet_num = datdebet[i]
            kredit_num = datkredit[i]
            
            textdata +=     dattanggal[i] + " | " + dattransaksi[i] + " | " + datharga[i] + " | " + self.jenis2text(jenis_num.toInt()) + " | " + self.debet2text(debet_num.toInt()) + " | " + self.kredit2text(kredit_num.toInt()) + "\n"
        
        printer=QtGui.QPrinter (QtGui.QPrinter.PrinterResolution)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setPaperSize(QtGui.QPrinter.A4)
        printer.setOutputFileName(fileName)
        
        doc = QtGui.QTextDocument()
        doc.setPlainText(textdata)
        doc.setPageSize(printer.pageRect().size())
        doc.print_(printer)
        
#======================================================================================================

    def view_search(self,  dbase, search_field, search_string):
        dataview = QtGui.QTableWidget()
        dataview.setColumnCount(7)

        dataview.setColumnWidth(0,50)
        dataview.setColumnWidth(1,100)
        dataview.setColumnWidth(2,200)
        dataview.setColumnWidth(3,100)
        dataview.setColumnWidth(4,200)
        dataview.setColumnWidth(5,150)
        dataview.setColumnWidth(6,150)

        dataview.setFixedWidth(1000)
        dataview.setFixedHeight(500)
        
        tabellabel=QtCore.QStringList()
        
        tabellabel.append("ID")
        tabellabel.append("Tanggal")
        tabellabel.append("Transaksi")
        tabellabel.append("Harga")
        tabellabel.append("Jenis")
        tabellabel.append("Debet")
        tabellabel.append("Kredit")
        
        dataview.setHorizontalHeaderLabels(tabellabel)
        dataview.setWindowTitle("Hasil Cari")
        
        datid=QtCore.QStringList()
        datid=self.mysql.data_get_one_column_search(dbase,"id",search_field,search_string)
        dataview.setRowCount(datid.count())
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(datid[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,0,isi)
            
        dattanggal=QtCore.QStringList()
        dattanggal=self.mysql.data_get_one_column_search(dbase,"tanggal",search_field,search_string)
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(dattanggal[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,1,isi)
            
        dattransaksi=QtCore.QStringList()
        dattransaksi=self.mysql.data_get_one_column_search(dbase,"transaksi",search_field,search_string)
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(dattransaksi[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,2,isi)
        
        datharga=QtCore.QStringList()
        datharga=self.mysql.data_get_one_column_search(dbase,"harga",search_field,search_string)
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(datharga[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,3,isi)
            
        datjenis=QtCore.QStringList()
        datjenis=self.mysql.data_get_one_column_search(dbase,"jenis",search_field,search_string)
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(datjenis[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,4,isi)
            
        datdebet=QtCore.QStringList()
        datdebet=self.mysql.data_get_one_column_search(dbase,"debet",search_field,search_string)
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(datdebet[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,5,isi)
            
        datkredit=QtCore.QStringList()
        datkredit=self.mysql.data_get_one_column_search(dbase,"kredit",search_field,search_string)
        for i in range(datid.count()):
            isi = QtGui.QTableWidgetItem(datkredit[i])
            isi.setFlags(isi.flags() ^ QtCore.Qt.ItemIsEditable );
            dataview.setItem(i,6,isi)
