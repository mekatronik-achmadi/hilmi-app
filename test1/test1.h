#ifndef TEST1_H
#define TEST1_H

#include <QMainWindow>
#include <QMessageBox>

#include <QtSql>

#include <QProcess>

#include <QFileDialog>
#include <QTextDocument>
#include <QtPrintSupport/QPrinter>

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

    void sqlProcessOnGoing(void);
    void sqlProcessFinished(int exitCode, QProcess::ExitStatus exitStatus);
    void sqlProcessError(QProcess::ProcessError error);

    void sqlsh_Init(void);
    void sqlsh_Args(void);
    void sqlsh_Exec(void);

    void sqlsh_list_database(void);

    void db_open_database(void);
    void db_export_pdf(void);

    void on_actionExit_triggered();
    void on_actionAboutQt_triggered();

    void on_rbDbNew_clicked();

    void on_rbDbExisting_clicked();

private:
    Ui::test1 *ui;

    QProcess sqlProc;
    QStringList sqlArgs;

    QSqlDatabase db;
    QSqlQuery dbquery;
    QString dbase;
    QString dtable;
};

#endif // TEST1_H
