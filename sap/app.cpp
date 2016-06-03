#include "sap.h"
#include "ui_sap.h"

void sap::app_msg_about(){
    QString qtver= QT_VERSION_STR;
    QString mysqlver = mysql->procSqlVersion();

    QString aboutmsg;

    aboutmsg += "Simple Accounting Program \n";
    aboutmsg += "\n";

    aboutmsg += "Credit: \n";
    aboutmsg += "Accounting Scheme written by Hilmi F. \n";
    aboutmsg += "GUI Program written by Achmadi \n";
    aboutmsg += "\n";

    aboutmsg += "Using: \n";
    aboutmsg += "Qt version " + qtver + "\n";
    aboutmsg += "MySQL version " + mysqlver;

#if (defined (Q_OS_LINUX))
    QString bashver = mysql->procCmdVersion();
    aboutmsg += "Bash version " + bashver;

    QString osver = mysql->procOsVersion();
    aboutmsg += "Linux version " + osver;

    aboutmsg += "\n";
#elif (defined (Q_OS_WIN))
    QString osver = mysql->procOsVersion();
    aboutmsg += "OS version " + osver;

    aboutmsg += "\n";
#endif

    QMessageBox::information(this,"About Me",aboutmsg);
}

void sap::app_refresh_databases(){

    ui->cmbDbDelete->clear();
    ui->cmbDbDelete->insertItems(0,mysql->list_database());

    ui->cmbDbExisting->clear();
    ui->cmbDbExisting->insertItems(0,mysql->list_database());

    ui->cmbDbExport->clear();
    ui->cmbDbExport->insertItems(0,mysql->list_database());

    ui->cmbDbImport->clear();
    ui->cmbDbImport->insertItems(0,mysql->list_database());
}

void sap::app_tab_ability(bool ability){
    ui->tabMain->setTabEnabled(1,ability);
    ui->tabMain->setTabEnabled(2,ability);
    ui->tabMain->setTabEnabled(3,ability);
    ui->actionMain_Data_as_Table->setEnabled(ability);
    ui->actionMain_Data_as_PDF->setEnabled(ability);
}

void sap::app_cmb_jenis(){
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

void sap::app_cmb_debet(){
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

void sap::app_cmb_kredit(){
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

void sap::app_cari_disable(){
    ui->txtCariDeskrip->setEnabled(false);
    ui->txtCariNilai->setEnabled(false);
    ui->cmbCariJenis->setEnabled(false);
    ui->cmbCariDebet->setEnabled(false);
    ui->cmbCariKredit->setEnabled(false);
    ui->dateCariTanggal->setEnabled(false);
    ui->btnCariNow->setEnabled(false);
}

void sap::app_cari_data(){

    if(ui->rbtCariDeskrip->isChecked()){
        mydata->view_search(ui->cmbDbExisting->currentText(),"transaksi",ui->txtCariDeskrip->text());
    }

    if(ui->rbtCariNilai->isChecked()){
        mydata->view_search(ui->cmbDbExisting->currentText(),"harga",ui->txtCariNilai->text());
    }

    if(ui->rbtCariJenis->isChecked()){
        mydata->view_search(ui->cmbDbExisting->currentText(),"jenis",QString::number(ui->cmbCariJenis->currentIndex()));
    }

    if(ui->rbtCariDebet->isChecked()){
        mydata->view_search(ui->cmbDbExisting->currentText(),"debet",QString::number(ui->cmbCariDebet->currentIndex()));
    }

    if(ui->rbtCariKredit->isChecked()){
        mydata->view_search(ui->cmbDbExisting->currentText(),"kredit",QString::number(ui->cmbCariKredit->currentIndex()));
    }

    if(ui->rbtCariTanggal->isChecked()){
        mydata->view_search(ui->cmbDbExisting->currentText(),"tanggal",ui->dateCariTanggal->text());
    }
}

void sap::app_show_one_data(QString dataid){
    ui->txtEditDeskrip->setText(mysql->data_get_one(ui->cmbDbExisting->currentText(),"transaksi",dataid));
    ui->txtEditNilai->setText(mysql->data_get_one(ui->cmbDbExisting->currentText(),"harga",dataid));
    ui->cmbEditJenis->setCurrentIndex(mysql->data_get_one(ui->cmbDbExisting->currentText(),"jenis",dataid).toInt());
    ui->dateEditTanggal->setDate(QDate::fromString(mysql->data_get_one(ui->cmbDbExisting->currentText(),"tanggal",dataid),"yyyy-MM-dd"));
}

void sap::app_edit_ability(bool ability){
    ui->txtEditDeskrip->setEnabled(ability);
    ui->txtEditNilai->setEnabled(ability);
    ui->cmbEditJenis->setEnabled(ability);
    ui->dateEditTanggal->setEnabled(ability);

    ui->btnEditNow->setEnabled(ability);
    ui->btnEditChange->setEnabled(ability);
    ui->btnEditDelete->setEnabled(ability);
}
