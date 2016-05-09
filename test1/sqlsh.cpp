#include "test1.h"
#include "ui_test1.h"

void test1::sqlsh_Init(){

    QObject::connect(&sqlProc, SIGNAL(readyReadStandardOutput()),this, SLOT(sqlProcessOnGoing()));
    QObject::connect(&sqlProc, SIGNAL(finished(int, QProcess::ExitStatus)),this,SLOT(sqlProcessFinished(int, QProcess::ExitStatus)));
    QObject::connect(&sqlProc, SIGNAL(error(QProcess::ProcessError)),this,SLOT(sqlProcessError(QProcess::ProcessError)));
}

void test1::sqlProcessOnGoing(){
    QByteArray newData = sqlProc.readAllStandardOutput();
    ui->txtSqlOutput->appendPlainText(QString::fromLocal8Bit(newData));

    return;
}

void test1::sqlProcessFinished(int exitCode, QProcess::ExitStatus exitStatus){
    (void) exitCode;

    if (exitStatus == QProcess::CrashExit) {
        QMessageBox::critical(this,"Crashed","Database Driver Crashed");
    }

    return;
}

void test1::sqlProcessError(QProcess::ProcessError error){

    if (error == QProcess::FailedToStart) {
        QMessageBox::critical(this,"Not Found","Database Driver not found");
    }

    return;
}

void test1::sqlsh_Args(){
    ui->txtSqlOutput->clear();
    sqlArgs.clear();

    sqlArgs << "-BN";
    sqlArgs << "-uroot";
    sqlArgs << "-e";

    return;
}

void test1::sqlsh_Exec(){
    sqlProc.start("mysql",sqlArgs);

    return;
}

QStringList test1::sqlsh_list_database(){
    sqlsh_Args();

    sqlArgs << "show databases;";

    sqlsh_Exec();

    sqlProc.waitForFinished();

    QStringList result = ui->txtSqlOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);
    return result;
}

void test1::sqlsh_delete_database(QString dbname){
    sqlsh_Args();

    QString dbargs;
    dbargs += "drop database ";
    dbargs += dbname;

    sqlArgs << dbargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    return;
}

void test1::sqlsh_delete_default(){
    sqlsh_delete_database("performance_schema");
    sqlsh_delete_database("mysql");
    sqlsh_delete_database("test");
}

void test1::sqlsh_create_database(QString dbname){
    sqlsh_Args();

    QString dbargs;
    dbargs += "create database ";
    dbargs += dbname;

    sqlArgs << dbargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    return;
}

void test1::sqlsh_create_tables(QString dbname){
    sqlsh_Args();

    QString tblargs;
    tblargs += "use " + dbname +";";
    tblargs +=  "create table main_data(";
    tblargs += "id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,";
    tblargs += "tanggal DATE NOT NULL,";
    tblargs += "transaksi VARCHAR(32) NOT NULL,";
    tblargs += "harga VARCHAR(32) NOT NULL,";
    tblargs += "jenis INT NOT NULL";
    tblargs += ")";

    sqlArgs << tblargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    return;
}

void test1::sqlsh_insert_data(QString dbname, QString deskrip, QString nilai, int jenis, QString tanggal){
    sqlsh_Args();

    QString insargs;
    insargs += "use " + dbname +";";
    insargs += "insert into `main_data` (`id`,`tanggal`,`transaksi`,`harga`,`jenis`) VALUES (NULL,";
    insargs += "\"" + tanggal + "\"" + ",";
    insargs += "\"" + deskrip + "\"" + ",";
    insargs += "\"" + nilai + "\"" + ",";
    insargs += "\"" + QString::number(jenis) + "\"" + ")";

    sqlArgs << insargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    return;

}

QStringList test1::sqlsh_get_main_data_one_column(QString dbname,QString field){
    sqlsh_Args();

    QString getargs;
    getargs += "use " + dbname +";";
    getargs += "select " + field + " from main_data";

    sqlArgs << getargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    QStringList result = ui->txtSqlOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);
    return result;
}
