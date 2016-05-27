#include "sap.h"
#include "ui_sap.h"

sap::sap(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::sap)
{
    ui->setupUi(this);

    mysql = new sqlsh;
    mydata = new sqldata;

    mysql->delete_default();

    app_refresh_databases();
    app_tab_ability(false);

    app_cmb_jenis();
    app_cmb_debet();
    app_cmb_kredit();

    ui->dateTrsTanggal->setDate(QDate::currentDate());
    ui->dateCariTanggal->setDate(QDate::currentDate());
    ui->dateEditTanggal->setDate(QDate::currentDate());
}

sap::~sap()
{
    delete ui;
}

void sap::on_actionExit_triggered()
{
    QApplication::quit();
}

void sap::on_actionAbout_triggered()
{
    app_msg_about();
}

void sap::on_actionMain_Data_as_Table_triggered()
{
    mydata->view_table(ui->cmbDbExisting->currentText());
}

void sap::on_actionMain_Data_as_PDF_triggered()
{
    mydata->view_pdf(ui->cmbDbExisting->currentText());
}

void sap::on_btnDbExisting_clicked()
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
        app_tab_ability(true);
        ui->cmbDbExisting->setEnabled(false);
        ui->btnDbExisting->setText("Unuse");
    }
    else if(ui->btnDbExisting->text()=="Unuse"){
        app_tab_ability(false);
        ui->cmbDbExisting->setEnabled(true);
        ui->btnDbExisting->setText("Use");
    }
}

void sap::on_btnDbNew_clicked()
{
    QString namadb = ui->txtDbNew->text();
    mysql->create_database(namadb);
    mysql->create_table(namadb);
    app_refresh_databases();
    QMessageBox::information(this,"Sudah tercipta", "Data " + namadb + " tercipta !!");
}

void sap::on_btnDbDelete_clicked()
{
    QString namadb= ui->cmbDbDelete->currentText();

    if(namadb=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain");
        return;
    }

    if(QMessageBox::warning(this,"Yakin?","yakin akan mnghapus data " + namadb + " selamanya ?!!", QMessageBox::Ok | QMessageBox::Cancel)==QMessageBox::Ok){

        mysql->delete_database(namadb);
        app_refresh_databases();
        QMessageBox::information(this,"Terhapus Selamanya", "Data " + namadb + " selamanya !!");
    }
}

void sap::on_btnDbExport_clicked()
{
    if(ui->cmbDbExport->currentText()=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain atau buat baru");
        return;
    }

    QString fileName = QFileDialog::getSaveFileName(this, "Export Database", QString(), "*.sql");
    if(fileName.isEmpty()){return;}
    if (QFileInfo(fileName).suffix().isEmpty()) { fileName.append(".sql"); }

    mysql->export_database(ui->cmbDbExport->currentText(),fileName);
}

void sap::on_btnDbImport_clicked()
{
    if(ui->cmbDbImport->currentText()=="information_schema"){
        QMessageBox::critical(this,"Database Terlarang","silahkan pilih database lain atau buat baru");
        return;
    }

    QString fileName = QFileDialog::getOpenFileName(this, "Import Data", QString(), "*.sql");
    if(fileName.isEmpty()){return;}

    if(QMessageBox::warning(this,"Yakin?","seluruh isi data " + ui->cmbDbImport->currentText() + " akan ditimpa data baru, lanjutkan ?!!", QMessageBox::Ok | QMessageBox::Cancel)==QMessageBox::Ok){
        mysql->import_database(ui->cmbDbImport->currentText(),fileName);
    }
}

void sap::on_btnTrsSave_clicked()
{
    mysql->data_insert( ui->cmbDbExisting->currentText(),
                        ui->dateTrsTanggal->text(),
                        ui->txtTrsDeskrip->text() ,
                        ui->txtTrsNilai->text(),
                        ui->cmbTrsJenis->currentIndex(),
                        mydata->jenis2debet(ui->cmbTrsJenis->currentIndex()),
                        mydata->jenis2kredit(ui->cmbTrsJenis->currentIndex())
                      );

    ui->txtTrsDeskrip->clear();
    ui->txtTrsNilai->clear();
    ui->cmbTrsJenis->setCurrentIndex(0);
}

void sap::on_btnTrsClear_clicked()
{
    ui->txtTrsDeskrip->clear();
    ui->txtTrsNilai->clear();
    ui->cmbTrsJenis->setCurrentIndex(0);
    ui->dateTrsTanggal->setDate(QDate::currentDate());
}

void sap::on_btnTrsNow_clicked()
{
    ui->dateTrsTanggal->setDate(QDate::currentDate());
}
