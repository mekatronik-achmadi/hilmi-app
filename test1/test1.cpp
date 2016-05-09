#include "test1.h"
#include "ui_test1.h"

test1::test1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::test1)
{
    ui->setupUi(this);
    ui->txtSqlOutput->setVisible(false);
    sqlsh_Init();
    sqlsh_delete_default();

    ui->tabMain->setTabText(0,"Database");
    ui->tabMain->setTabText(1,"Input");
    app_tab_ability(false);
    app_add_jenis();
    ui->dateTrsTanggal->setDate(QDate::currentDate());

    app_refresh_database();
}

test1::~test1()
{
    delete ui;
}

void test1::app_manage_db_disable(){
    ui->txtDbNew->setEnabled(false);
    ui->btnDbNew->setEnabled(false);

    ui->cmbDbExisting->setEnabled(false);
    ui->btnDbExisting->setEnabled(false);

    ui->cmbDbDelete->setEnabled(false);
    ui->btnDbDelete->setEnabled(false);
}

void test1::app_tab_ability(bool ability){

    ui->tabMain->setTabEnabled(1,ability);
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

void test1::app_add_jenis(){
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

void test1::on_actionExit_triggered()
{
    QApplication::quit();
}

void test1::on_actionAboutQt_triggered()
{
    QApplication::aboutQt();
    return;
}

void test1::on_rbDbNew_clicked()
{
    app_manage_db_disable();
    ui->txtDbNew->setEnabled(true);
    ui->txtDbNew->clear();
    ui->btnDbNew->setEnabled(true);

    return;
}

void test1::on_rbDbExisting_clicked()
{
    app_manage_db_disable();
    ui->cmbDbExisting->setEnabled(true);
    ui->btnDbExisting->setEnabled(true);

    return;
}

void test1::on_rbtDbDelete_clicked()
{
    app_manage_db_disable();
    ui->cmbDbDelete->setEnabled(true);
    ui->btnDbDelete->setEnabled(true);

    return;
}

void test1::on_btnDbDelete_clicked()
{

    QString namadb= ui->cmbDbDelete->currentText();

    if(namadb=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain");
        return;
    }

    if(QMessageBox::warning(this,"Yakin?","yakin akan mnghapus data " + namadb + " selamanya ?!!", QMessageBox::Ok | QMessageBox::Cancel)==QMessageBox::Ok){

        sqlsh_delete_database(namadb);

        app_refresh_database();

        QMessageBox::information(this,"Terhapus Selamanya", "Data " + namadb + " selamanya !!");
    }

}

void test1::on_btnDbNew_clicked()
{
    QString namadb = ui->txtDbNew->text();

    sqlsh_create_database(namadb);
    sqlsh_create_tables(namadb);

    app_refresh_database();

    QMessageBox::information(this,"Sudah tercipta", "Data " + namadb + " tercipta !!");
}

void test1::on_btnDbExisting_clicked()
{

    if(ui->cmbDbExisting->currentText()=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain atau buat baru");
        return;
    }

    if(ui->cmbDbExisting->currentText().isEmpty()){
        QMessageBox::critical(this,"Database Tidak ada","Nama Database tidak ada");
        return;
    }

    if(ui->btnDbExisting->text()=="Use"){
        dbase = ui->cmbDbExisting->currentText();
        app_tab_ability(true);
        app_manage_db_disable();
        ui->btnDbExisting->setEnabled(true);
        ui->btnDbExisting->setText("Unuse");
    }
    else if(ui->btnDbExisting->text()=="Unuse"){
        dbase = "";
        app_manage_db_disable();
        app_tab_ability(false);
        ui->cmbDbExisting->setEnabled(true);
        ui->btnDbExisting->setEnabled(true);
        ui->btnDbExisting->setText("Use");
    }
}

void test1::on_btnDbExport_clicked()
{
    if(ui->cmbDbExport->currentText()=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain atau buat baru");
        return;
    }

    QString fileName = QFileDialog::getSaveFileName(this, "Export Database", QString(), "*.sql");
    if(fileName.isEmpty()){return;}
    if (QFileInfo(fileName).suffix().isEmpty()) { fileName.append(".sql"); }

    sqlsh_export_database(ui->cmbDbExport->currentText(),fileName);

}

void test1::on_btnDbImport_clicked()
{
    if(ui->cmbDbImport->currentText()=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain atau buat baru");
        return;
    }

    QString fileName = QFileDialog::getOpenFileName(this, "Import Data", QString(), "*.sql");
    if(fileName.isEmpty()){return;}

    if(QMessageBox::warning(this,"Yakin?","seluruh isi data " + ui->cmbDbImport->currentText() + " akan ditimpa data baru, lanjutkan ?!!", QMessageBox::Ok | QMessageBox::Cancel)==QMessageBox::Ok){
        sqlsh_import_database(ui->cmbDbImport->currentText(),fileName);
    }
}

void test1::on_btnTrsClear_clicked()
{
    ui->txtTrsDeskrip->clear();
    ui->txtTrsNilai->clear();
    ui->cmbTrsJenis->setCurrentIndex(0);
    ui->dateTrsTanggal->setDate(QDate::currentDate());
}

void test1::on_btnTrsSave_clicked()
{

    sqlsh_insert_data(dbase,
                      ui->txtTrsDeskrip->text() ,
                      ui->txtTrsNilai->text(),
                      ui->cmbTrsJenis->currentIndex(),
                      ui->dateTrsTanggal->text()
                      );

    ui->txtTrsDeskrip->clear();
    ui->txtTrsNilai->clear();
    ui->cmbTrsJenis->setCurrentIndex(0);

}

void test1::on_btnTrsNow_clicked()
{
    ui->dateTrsTanggal->setDate(QDate::currentDate());
}

void test1::on_btnTrsView_clicked()
{
    int i;

    QTableWidget *dataview = new QTableWidget;
    dataview->setColumnCount(4);

    QStringList datid = sqlsh_get_main_data_one_column(dbase,"id");
    dataview->setRowCount(datid.count());

    QStringList dattanggal = sqlsh_get_main_data_one_column(dbase,"tanggal");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattanggal[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,0,isi);
    }

    QStringList dattransaksi = sqlsh_get_main_data_one_column(dbase,"transaksi");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattransaksi[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,1,isi);;
    }

    QStringList datharga = sqlsh_get_main_data_one_column(dbase,"harga");
    for(i=0;i<datid.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datharga[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,2,isi);
    }

    QStringList datjenis = sqlsh_get_main_data_one_column(dbase,"jenis");
    for(i=0;i<datid.count();i++){
        QString jenis_num = datjenis[i];
        QTableWidgetItem *isi = new QTableWidgetItem(app_text_jenis(jenis_num.toInt()));
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,3,isi);
    }

    QStringList tabellabel;
    tabellabel << "Tanggal";
    tabellabel << "Transaksi";
    tabellabel << "Harga";
    tabellabel << "Jenis";
    dataview->setHorizontalHeaderLabels(tabellabel);
    dataview->setWindowTitle("Rekap Data");
    dataview->setFixedHeight(200);
    dataview->setFixedWidth(450);
    dataview->show();
}

void test1::on_btnTrsPDF_clicked()
{
    QString fileName = QFileDialog::getSaveFileName(this, "Export PDF", QString(), "*.pdf");
    if(fileName.isEmpty()){return;}
    if (QFileInfo(fileName).suffix().isEmpty()) { fileName.append(".pdf"); }

    QStringList datid = sqlsh_get_main_data_one_column(dbase,"id");
    QStringList dattanggal = sqlsh_get_main_data_one_column(dbase,"tanggal");
    QStringList dattransaksi = sqlsh_get_main_data_one_column(dbase,"transaksi");
    QStringList datharga = sqlsh_get_main_data_one_column(dbase,"harga");
    QStringList datjenis = sqlsh_get_main_data_one_column(dbase,"jenis");

    int i;
    QString textdata;
    for(i=0;i<datid.count();i++){
        QString jenis_num = datjenis[i];
        textdata +=     dattanggal[i] + " | " +
                        dattransaksi[i] + " | " +
                        datharga[i] + " | " +
                        app_text_jenis(jenis_num.toInt()) + "\n";
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
