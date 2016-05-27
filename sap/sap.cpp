#include "sap.h"
#include "ui_sap.h"

sap::sap(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::sap)
{
    ui->setupUi(this);

    mysql = new sqlsh;
    mysql->delete_default();

    myapp = new app;
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
    myapp->msg_about();
}
