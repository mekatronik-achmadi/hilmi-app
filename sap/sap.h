#ifndef SAP_H
#define SAP_H

#include <QMainWindow>
#include <QFileDialog>

#include "sqlsh.h"
#include "sqldata.h"

namespace Ui {
class sap;
}

class sap : public QMainWindow
{
    Q_OBJECT

public:
    explicit sap(QWidget *parent = 0);
    ~sap();

private slots:
    void app_msg_about(void);
    void app_refresh_databases(void);
    void app_tab_ability(bool ability);

    void app_cmb_jenis(void);
    void app_cmb_debet(void);
    void app_cmb_kredit(void);

    void on_actionExit_triggered();
    void on_actionAbout_triggered();
    void on_actionMain_Data_as_Table_triggered();
    void on_actionMain_Data_as_PDF_triggered();

    void on_btnDbExisting_clicked();
    void on_btnDbNew_clicked();
    void on_btnDbDelete_clicked();
    void on_btnDbExport_clicked();
    void on_btnDbImport_clicked();

    void on_btnTrsSave_clicked();

    void on_btnTrsClear_clicked();

    void on_btnTrsNow_clicked();

private:
    Ui::sap *ui;
    sqlsh *mysql;
    sqldata *mydata;
};

#endif // SAP_H
