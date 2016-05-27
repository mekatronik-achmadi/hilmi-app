#ifndef SAP_H
#define SAP_H

#include <QMainWindow>
#include "inclusion.h"

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
    void on_actionExit_triggered();

    void on_actionAbout_triggered();

private:
    Ui::sap *ui;

    sqlsh *mysql;
    app *myapp;
};

#endif // SAP_H
