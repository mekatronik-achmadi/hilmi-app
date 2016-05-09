#ifndef TEST1_H
#define TEST1_H

#include <QMainWindow>
#include <QMessageBox>

#include <QtSql>

#include <QProcess>

#include <QFileDialog>
#include <QTextDocument>
#include <QtPrintSupport/QPrinter>

#include <QTableWidget>

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

    QStringList sqlsh_list_database(void);
    void sqlsh_delete_database(QString dbname);
    void sqlsh_delete_default();
    void sqlsh_create_database(QString dbname);
    void sqlsh_create_tables(QString dbname);

    void sqlsh_insert_data(QString dbname, QString deskrip, QString nilai, int jenis, QString tanggal);
    QStringList sqlsh_get_main_data_one_column(QString dbname,QString field);

    void db_open_database(void);
    void db_export_pdf(void);

    void app_manage_db_disable(void);
    void app_tab_ability(bool ability);
    void app_add_jenis(void);

    void on_actionExit_triggered();
    void on_actionAboutQt_triggered();

    void on_rbDbNew_clicked();
    void on_rbDbExisting_clicked();
    void on_rbtDbDelete_clicked();
    void on_btnDbDelete_clicked();
    void on_btnDbNew_clicked();
    void on_btnDbExisting_clicked();

    void on_btnTrsClear_clicked();
    void on_btnTrsSave_clicked();
    void on_btnTrsNow_clicked();

    void on_btnTrsView_clicked();

private:
    Ui::test1 *ui;

    QProcess sqlProc;
    QStringList sqlArgs;

    QSqlDatabase db;
    QSqlQuery dbquery;
    QString dbase;
    QString dtable;

    QTableView *view;
};

#endif // TEST1_H
