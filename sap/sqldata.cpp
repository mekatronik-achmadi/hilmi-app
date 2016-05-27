#include "sqldata.h"

sqldata::sqldata(QWidget *parent) : QMainWindow(parent)
{
    mysql = new sqlsh;
}

int sqldata::jenis2debet(int num_jenis){
    int result=0;

    switch(num_jenis){
    case 0: result=0;break;
    case 1: result=0;break;
    case 2: result=1;break;
    case 3: result=2;break;
    case 4: result=1;break;
    case 5: result=3;break;
    case 6: result=4;break;
    case 7: result=4;break;
    case 8: result=5;break;
    case 9: result=6;break;
    case 10: result=2;break;
    case 11: result=7;break;
    case 12: result=1;break;
    case 13: result=8;break;
    case 14: result=1;break;
    case 15: result=2;break;
    case 16: result=1;break;
    case 17: result=9;break;
    case 18: result=10;break;
    case 19: result=11;break;
    case 20: result=12;break;
    case 21: result=13;break;
    case 22: result=14;break;
    case 23: result=14;break;
    }
    return result;
}

int sqldata::jenis2kredit(int num_jenis){
    int result=0;

    switch(num_jenis){
    case 0: result=0;break;
    case 1: result=1;break;
    case 2: result=2;break;
    case 3: result=2;break;
    case 4: result=3;break;
    case 5: result=3;break;
    case 6: result=0;break;
    case 7: result=4;break;
    case 8: result=0;break;
    case 9: result=0;break;
    case 10: result=0;break;
    case 11: result=0;break;
    case 12: result=5;break;
    case 13: result=0;break;
    case 14: result=1;break;
    case 15: result=6;break;
    case 16: result=4;break;
    case 17: result=0;break;
    case 18: result=7;break;
    case 19: result=0;break;
    case 20: result=8;break;
    case 21: result=9;break;
    case 22: result=0;break;
    case 23: result=3;break;
    }
    return result;
}

//======================================================================================================

QString sqldata::jenis2text(int num_jenis){
    QString result;

    switch(num_jenis){
    case 0: result="PEMBELIAN BAHAN BAKU TUNAI";break;
    case 1: result="PEMBELIAN BAHAN BAKU KREDIT";break;
    case 2: result="RETUR PEMBELIAN TUNAI";break;
    case 3: result="RETUR PEMBELIAN KREDIT";break;
    case 4: result="PENJUALAN TUNAI";break;
    case 5: result="PENJUALAN KREDIT";break;
    case 6: result="RETUR PENJUALAN TUNAI";break;
    case 7: result="RETUR PENJUALAN KREDIT";break;
    case 8: result="PEMBAYARAN GAJI";break;
    case 9: result="PEMBAYARAN TELP, AIR & LISTRIK";break;
    case 10: result="PEMBAYARAN UTANG MELALUI KAS DI TANGAN";break;
    case 11: result="PEMBAYARAN TRANSPORTASI";break;
    case 12: result="DISETOR MODAL TUNAI";break;
    case 13: result="PENYETORAN TUNAI KE BANK";break;
    case 14: result="PINJAMAN DARI BANK";break;
    case 15: result="PEMBAYARAN UTANG MELALUI BANK";break;
    case 16: result="DITERIMA PEMBAYARAN PIUTANG";break;
    case 17: result="DIBELI PERALATAN";break;
    case 18: result="DEPRESIASI PERALATAN";break;
    case 19: result="SEWA BANGUNAN DIBAYAR DIMUKA";break;
    case 20: result="PEMBAYARAN SEWA BANGUNAN";break;
    case 21: result="BEBAN GARANSI ESTIMASI";break;
    case 22: result="BEBAN GARANSI REALISASI";break;
    case 23: result="BEBAN GARANSI TAK TEREALISASI";break;
    }
    return result;
}

//======================================================================================================

void sqldata::view_table(QString dbase){
    int i;

    QTableWidget *dataview = new QTableWidget;
    dataview->setColumnCount(7);

    QStringList datid = mysql->data_get_one_column(dbase,"id");
    dataview->setRowCount(datid.count());
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datid[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,0,isi);
    }

    QStringList dattanggal = mysql->data_get_one_column(dbase,"tanggal");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattanggal[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,1,isi);
    }

    QStringList dattransaksi = mysql->data_get_one_column(dbase,"transaksi");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattransaksi[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,2,isi);;
    }

    QStringList datharga = mysql->data_get_one_column(dbase,"harga");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datharga[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,3,isi);
    }

    QStringList datjenis = mysql->data_get_one_column(dbase,"jenis");
    for(i=0;i<datid.count();i++){
        QString jenis_num = datjenis[i];
        QTableWidgetItem *isi = new QTableWidgetItem(jenis2text(jenis_num.toInt()));
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,4,isi);
    }

    QStringList datdebet = mysql->data_get_one_column(dbase,"debet");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datdebet[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,5,isi);
    }

    QStringList datkredit = mysql->data_get_one_column(dbase,"kredit");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datkredit[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,6,isi);
    }

    QStringList tabellabel;
    tabellabel << "Data ID";
    tabellabel << "Tanggal";
    tabellabel << "Transaksi";
    tabellabel << "Harga";
    tabellabel << "Jenis";
    tabellabel << "Debet";
    tabellabel << "Kredit";
    dataview->setHorizontalHeaderLabels(tabellabel);
    dataview->setWindowTitle("Rekap Data");
    dataview->setFixedWidth(720);
    dataview->setFixedHeight(200);
    dataview->show();
}

void sqldata::view_pdf(QString dbase){
    QString fileName = QFileDialog::getSaveFileName(this, "Export PDF", QString(), "*.pdf");
    if(fileName.isEmpty()){return;}
    if (QFileInfo(fileName).suffix().isEmpty()) { fileName.append(".pdf"); }

    QStringList datid = mysql->data_get_one_column(dbase,"id");
    QStringList dattanggal = mysql->data_get_one_column(dbase,"tanggal");
    QStringList dattransaksi = mysql->data_get_one_column(dbase,"transaksi");
    QStringList datharga = mysql->data_get_one_column(dbase,"harga");
    QStringList datjenis = mysql->data_get_one_column(dbase,"jenis");
    QStringList datdebet = mysql->data_get_one_column(dbase,"debet");
    QStringList datkredit = mysql->data_get_one_column(dbase,"kredit");

    int i;
    QString textdata;
    for(i=0;i<datid.count();i++){
        QString jenis_num = datjenis[i];
        textdata +=     dattanggal[i] + " | " +
                        dattransaksi[i] + " | " +
                        datharga[i] + " | " +
                        jenis2text(jenis_num.toInt()) + " | " +
                        datdebet[i] + " | " +
                        datkredit[i] + "\n";
    }


    QPrinter printer(QPrinter::PrinterResolution);
    printer.setOutputFormat(QPrinter::PdfFormat);
    printer.setPaperSize(QPrinter::A4);
    printer.setOutputFileName(fileName);

    QTextDocument doc;
    doc.setPlainText(textdata);
    doc.setPageSize(printer.pageRect().size()); // This is necessary if you want to hide the page number
    doc.print(&printer);
}
