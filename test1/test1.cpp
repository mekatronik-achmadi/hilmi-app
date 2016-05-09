#include "test1.h"
#include "ui_test1.h"

test1::test1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::test1)
{
    ui->setupUi(this);
    sqlsh_Init();

    sqlsh_delete_default();

    ui->tabMain->setTabText(0,"Database");
    ui->tabMain->setTabText(1,"Input");

    app_tab_ability(false);

    app_add_jenis();

    ui->dateTrsTanggal->setDate(QDate::currentDate());
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
    ui->btnDbNew->setEnabled(true);

    return;
}

void test1::on_rbDbExisting_clicked()
{
    app_manage_db_disable();
    ui->cmbDbExisting->setEnabled(true);
    ui->btnDbExisting->setEnabled(true);

    ui->cmbDbExisting->clear();
    ui->cmbDbExisting->insertItems(0,sqlsh_list_database());

    return;
}

void test1::on_rbtDbDelete_clicked()
{
    app_manage_db_disable();
    ui->cmbDbDelete->setEnabled(true);
    ui->btnDbDelete->setEnabled(true);

    ui->cmbDbDelete->clear();
    ui->cmbDbDelete->insertItems(0,sqlsh_list_database());

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

        sqlsh_list_database();

        QStringList strlist = ui->txtSqlOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);

        ui->cmbDbDelete->clear();
        ui->cmbDbDelete->insertItems(0,strlist);

        QMessageBox::information(this,"Terhapus Selamanya", "Data " + namadb + " selamanya !!");
    }

}

void test1::on_btnDbNew_clicked()
{
    QString namadb = ui->txtDbNew->text();

    sqlsh_create_database(namadb);
    sqlsh_create_tables(namadb);

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
    for(i=0;i<dattanggal.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattanggal[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,0,isi);
    }

    QStringList dattransaksi = sqlsh_get_main_data_one_column(dbase,"transaksi");
    for(i=0;i<dattransaksi.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(dattransaksi[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,1,isi);;
    }

    QStringList datharga = sqlsh_get_main_data_one_column(dbase,"harga");
    for(i=0;i<datharga.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datharga[i]);
        isi->setFlags(isi->flags() ^ Qt::ItemIsEditable );
        dataview->setItem(i,2,isi);
    }

    QStringList datjenis = sqlsh_get_main_data_one_column(dbase,"jenis");
    for(i=0;i<datjenis.count();i++){
        QTableWidgetItem *isi = new QTableWidgetItem(datjenis[i]);
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
