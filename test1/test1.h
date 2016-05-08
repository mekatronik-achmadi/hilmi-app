#ifndef TEST1_H
#define TEST1_H

#include <QMainWindow>
#include <QMessageBox>

#include <QtSql>

namespace Ui {
class test1;
}

class test1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit test1(QWidget *parent = 0);
    ~test1();

private slots:

    void db_create_connection(void);

    void on_actionExit_triggered();
    void on_actionAboutQt_triggered();
    void on_pushButton_clicked();

private:
    Ui::test1 *ui;

    QSqlDatabase db;
    QSqlQuery myquery;
    QString dbase;
    QString dtable;
};

#endif // TEST1_H
