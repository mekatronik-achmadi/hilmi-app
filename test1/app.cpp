#include "test1.h"
#include "ui_test1.h"

QString test1::app_cmdver(){
    ui->txtSqlOutput->clear();

#if (defined (Q_OS_LINUX))
    sqlProc.start("bash -c \"echo $BASH_VERSION\"");
#elif (defined (Q_OS_WIN))
#endif

    sqlProc.waitForFinished();

    QString result = ui->txtSqlOutput->toPlainText();
    return result;
}

QString test1::app_osver(){
    ui->txtSqlOutput->clear();

#if (defined (Q_OS_LINUX))
    sqlProc.start("bash -c \"uname -r\"");
#elif (defined (Q_OS_WIN))
#endif

    sqlProc.waitForFinished();

    QString result = ui->txtSqlOutput->toPlainText();
    return result;
}

void test1::app_table_maindata(){
    int i;

    QTableWidget *dataview = new QTableWidget;
    dataview->setColumnCount(7);

    QStringList datid = sqlsh_get_main_data_one_column(dbase,"id");
    dataview->setRowCount(datid.count());
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datid[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,0,isi);
    }

    QStringList dattanggal = sqlsh_get_main_data_one_column(dbase,"tanggal");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattanggal[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,1,isi);
    }

    QStringList dattransaksi = sqlsh_get_main_data_one_column(dbase,"transaksi");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattransaksi[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,2,isi);;
    }

    QStringList datharga = sqlsh_get_main_data_one_column(dbase,"harga");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datharga[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,3,isi);
    }

    QStringList datjenis = sqlsh_get_main_data_one_column(dbase,"jenis");
    for(i=0;i<datid.count();i++){
        QString jenis_num = datjenis[i];
        QTableWidgetItem *isi = new QTableWidgetItem(app_text_jenis(jenis_num.toInt()));
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,4,isi);
    }

    QStringList datdebet = sqlsh_get_main_data_one_column(dbase,"debet");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datdebet[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,5,isi);
    }

    QStringList datkredit = sqlsh_get_main_data_one_column(dbase,"kredit");
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

void test1::app_pdf_maindata(){
    QString fileName = QFileDialog::getSaveFileName(this, "Export PDF", QString(), "*.pdf");
    if(fileName.isEmpty()){return;}
    if (QFileInfo(fileName).suffix().isEmpty()) { fileName.append(".pdf"); }

    QStringList datid = sqlsh_get_main_data_one_column(dbase,"id");
    QStringList dattanggal = sqlsh_get_main_data_one_column(dbase,"tanggal");
    QStringList dattransaksi = sqlsh_get_main_data_one_column(dbase,"transaksi");
    QStringList datharga = sqlsh_get_main_data_one_column(dbase,"harga");
    QStringList datjenis = sqlsh_get_main_data_one_column(dbase,"jenis");
    QStringList datdebet = sqlsh_get_main_data_one_column(dbase,"debet");
    QStringList datkredit = sqlsh_get_main_data_one_column(dbase,"kredit");

    int i;
    QString textdata;
    for(i=0;i<datid.count();i++){
        QString jenis_num = datjenis[i];
        textdata +=     dattanggal[i] + " | " +
                        dattransaksi[i] + " | " +
                        datharga[i] + " | " +
                        app_text_jenis(jenis_num.toInt()) + " | " +
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

//======================================================================================================

void test1::app_tab_ability(bool ability){
    ui->tabMain->setTabEnabled(1,ability);
    ui->tabMain->setTabEnabled(2,ability);
    ui->tabMain->setTabEnabled(3,ability);
    ui->actionMain_Data_as_Table->setEnabled(ability);
    ui->actionMain_Data_as_PDF->setEnabled(ability);
}

void test1::app_refresh_database(){
    ui->cmbDbDelete->clear();
    ui->cmbDbDelete->insertItems(0,sqlsh_list_database());
    ui->cmbDbExisting->clear();
    ui->cmbDbExisting->insertItems(0,sqlsh_list_database());
    ui->cmbDbExport->clear();
    ui->cmbDbExport->insertItems(0,sqlsh_list_database());
    ui->cmbDbImport->clear();
    ui->cmbDbImport->insertItems(0,sqlsh_list_database());
}

void test1::app_cari_disable(){
    ui->txtCariDeskrip->setEnabled(false);
    ui->txtCariNilai->setEnabled(false);
    ui->cmbCariJenis->setEnabled(false);
    ui->cmbCariDebet->setEnabled(false);
    ui->cmbCariKredit->setEnabled(false);
    ui->dateCariTanggal->setEnabled(false);
}

//======================================================================================================

void test1::app_cmb_jenis(){
    QStringList jenis;

    jenis << "PEMBELIAN BAHAN BAKU TUNAI";
    jenis << "PEMBELIAN BAHAN BAKU KREDIT";
    jenis << "RETUR PEMBELIAN TUNAI";
    jenis << "RETUR PEMBELIAN KREDIT";
    jenis << "PENJUALAN TUNAI";
    jenis << "PENJUALAN KREDIT";
    jenis << "RETUR PENJUALAN TUNAI";
    jenis << "RETUR PENJUALAN KREDIT";
    jenis << "PEMBAYARAN GAJI";
    jenis << "PEMBAYARAN TELP, AIR & LISTRIK";
    jenis << "PEMBAYARAN UTANG MELALUI KAS DI TANGAN";
    jenis << "PEMBAYARAN TRANSPORTASI";
    jenis << "DISETOR MODAL TUNAI";
    jenis << "PENYETORAN TUNAI KE BANK";
    jenis << "PINJAMAN DARI BANK";
    jenis << "PEMBAYARAN UTANG MELALUI BANK";
    jenis << "DITERIMA PEMBAYARAN PIUTANG";
    jenis << "DIBELI PERALATAN";
    jenis << "DEPRESIASI PERALATAN";
    jenis << "SEWA BANGUNAN DIBAYAR DIMUKA";
    jenis << "PEMBAYARAN SEWA BANGUNAN";
    jenis << "BEBAN GARANSI ESTIMASI";
    jenis << "BEBAN GARANSI REALISASI";
    jenis << "BEBAN GARANSI TAK TEREALISASI";

    ui->cmbTrsJenis->clear();
    ui->cmbTrsJenis->insertItems(0,jenis);
    ui->cmbEditJenis->clear();
    ui->cmbEditJenis->insertItems(0,jenis);
    ui->cmbCariJenis->clear();
    ui->cmbCariJenis->insertItems(0,jenis);
}

void test1::app_cmb_debet(){
    QStringList debet;

    debet << "PEMBELIAN";
    debet << "KAS DI TANGAN";
    debet << "UTANG USAHA";
    debet << "PIUTANG USAHA";
    debet << "RETUR PENJUALAN";
    debet << "BEBAN GAJI";
    debet << "BEBAN TELP, AIR & LISTRIK";
    debet << "BEBAN TRANSPORTASI";
    debet << "KAS DI BANK";
    debet << "PERALATAN";
    debet << "BEBAN PENYUSUTAN PERALATAN";
    debet << "SEWA BANGUNAN DI BAYAR DIMUKA";
    debet << "BEBAN SEWA BANGUNAN";
    debet << "BEBAN GARANSI";
    debet << "CADANGAN GARANSI";

    ui->cmbCariDebet->clear();
    ui->cmbCariDebet->insertItems(0,debet);

}

void test1::app_cmb_kredit(){
    QStringList kredit;

    kredit << "KAS DI TANGAN";
    kredit << "UTANG USAHA";
    kredit << "RETUR PEMBELIAN";
    kredit << "PENJUALAN";
    kredit << "PIUTANG USAHA";
    kredit << "MODAL PEMILIK";
    kredit << "KAS DI BANK";
    kredit << "AKUMULASI PENYUSUTAN PERALATAN";
    kredit << "SEWA BANGUNAN DIBAYAR DI MUKA";
    kredit << "CADANGAN GARANSI";

    ui->cmbCariKredit->clear();
    ui->cmbCariKredit->insertItems(0,kredit);
}

int test1::app_jenis_debet(int num_jenis){
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

int test1::app_jenis_kredit(int num_jenis){
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

QString test1::app_text_jenis(int num_jenis){
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
