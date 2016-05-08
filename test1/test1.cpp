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

void test1::on_actionExit_triggered()
{
    QApplication::quit();
}

void test1::on_actionAboutQt_triggered()
{
    QApplication::aboutQt();
}
