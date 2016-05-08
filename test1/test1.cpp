#include "test1.h"
#include "ui_test1.h"

test1::test1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::test1)
{
    ui->setupUi(this);

    ui->tabMain->setTabText(0,"Database");
}

test1::~test1()
{
    delete ui;
}

//====================================================

void test1::db_create_connection(){
    db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("localhost");
    db.setDatabaseName("hilmi_test");
    db.setUserName("root");
    db.setPassword("");

    if (!db.open()) {
        QMessageBox::critical(this,"Error","Error Opening Database");
        return;
    }
}

//====================================================

void test1::on_actionExit_triggered()
{
    QApplication::quit();
}

void test1::on_actionAboutQt_triggered()
{
    QApplication::aboutQt();
}

void test1::on_pushButton_clicked()
{
    db_create_connection();

}
