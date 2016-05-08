#include "test1.h"
#include "ui_test1.h"

test1::test1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::test1)
{
    ui->setupUi(this);

    ui->tabMain->setTabText(0,"Database");

    sqlsh_Init();
}

test1::~test1()
{
    delete ui;
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
    ui->txtDbNew->setEnabled(true);
    ui->btnDbNew->setEnabled(true);

    ui->cmbDbExisting->setEnabled(false);
    ui->btnDbExisting->setEnabled(false);

    return;
}

void test1::on_rbDbExisting_clicked()
{
    sqlsh_list_database();

    QStringList strlist = ui->txtSqlOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);

    ui->cmbDbExisting->clear();
    ui->cmbDbExisting->insertItems(0,strlist);

    ui->txtDbNew->setEnabled(false);
    ui->btnDbNew->setEnabled(false);

    ui->cmbDbExisting->setEnabled(true);
    ui->btnDbExisting->setEnabled(true);

    return;
}
