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
