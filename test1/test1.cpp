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

    app_refresh_database();

    app_tab_ability(false);

    app_cmb_jenis();
    app_cmb_debet();
    app_cmb_kredit();

    ui->dateTrsTanggal->setDate(QDate::currentDate());
    ui->dateCariTanggal->setDate(QDate::currentDate());
    ui->dateEditTanggal->setDate(QDate::currentDate());
}

test1::~test1()
{
    delete ui;
}

//======================================================================================================

void test1::on_actionExit_triggered()
{
    QApplication::quit();
}

void test1::on_actionAbout_triggered()
{
    QString qtver= QT_VERSION_STR;
    QString mysqlver = sqlsh_sqlVer();

    QString aboutmsg;
    aboutmsg += "using: \n";
    aboutmsg += "Qt version " + qtver + "\n";
    aboutmsg += "MySQL version " + mysqlver;

#if (defined (Q_OS_LINUX))
    QString bashver = app_cmdver();
    aboutmsg += "BASH version " + bashver;

    QString osver = app_osver();
    aboutmsg += "Linux version " + osver;

    aboutmsg += "\n";
#elif (defined (Q_OS_WIN))
#endif

    QMessageBox::information(this,"About Me",aboutmsg);
}

void test1::on_actionMain_Data_as_Table_triggered()
{
    app_table_maindata();
}

void test1::on_actionMain_Data_as_PDF_triggered()
{
    app_pdf_maindata();
}

//======================================================================================================

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
        ui->cmbDbExisting->setEnabled(false);
        ui->btnDbExisting->setText("Unuse");
    }
    else if(ui->btnDbExisting->text()=="Unuse"){
        dbase = "";
        app_tab_ability(false);
        ui->cmbDbExisting->setEnabled(true);
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

//======================================================================================================

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
                      ui->dateTrsTanggal->text(),
                      ui->txtTrsDeskrip->text() ,
                      ui->txtTrsNilai->text(),
                      ui->cmbTrsJenis->currentIndex(),
                      app_jenis_debet(ui->cmbTrsJenis->currentIndex()),
                      app_jenis_kredit(ui->cmbTrsJenis->currentIndex())
                      );

    ui->txtTrsDeskrip->clear();
    ui->txtTrsNilai->clear();
    ui->cmbTrsJenis->setCurrentIndex(0);

}

void test1::on_btnTrsNow_clicked()
{
    ui->dateTrsTanggal->setDate(QDate::currentDate());
}

//======================================================================================================

void test1::on_rbtCariDeskrip_clicked()
{
    app_cari_disable();
    ui->txtCariDeskrip->setEnabled(true);
}

void test1::on_rbtCariNilai_clicked()
{
    app_cari_disable();
    ui->txtCariNilai->setEnabled(true);
}

void test1::on_rbtCariJenis_clicked()
{
    app_cari_disable();
    ui->cmbCariJenis->setEnabled(true);
}

void test1::on_rbtCariDebet_clicked()
{
    app_cari_disable();
    ui->cmbCariDebet->setEnabled(true);
}

void test1::on_rbtCariKredit_clicked()
{
    app_cari_disable();
    ui->cmbCariKredit->setEnabled(true);
}

void test1::on_rbtCariTanggal_clicked()
{
    app_cari_disable();
    ui->dateCariTanggal->setEnabled(true);
}

void test1::on_btnCariNow_clicked()
{
    ui->dateCariTanggal->setDate(QDate::currentDate());
}

void test1::on_btnCariClear_clicked()
{
    ui->txtCariDeskrip->clear();
    ui->txtCariNilai->clear();
    ui->cmbCariJenis->setCurrentIndex(0);
    ui->dateTrsTanggal->setDate(QDate::currentDate());
}
