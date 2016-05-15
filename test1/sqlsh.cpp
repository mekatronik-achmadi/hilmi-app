#include "test1.h"
#include "ui_test1.h"

//======================================================================================================

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

//======================================================================================================

void test1::sqlsh_Init(){

    QObject::connect(&sqlProc, SIGNAL(readyReadStandardOutput()),this, SLOT(sqlProcessOnGoing()));
    QObject::connect(&sqlProc, SIGNAL(finished(int, QProcess::ExitStatus)),this,SLOT(sqlProcessFinished(int, QProcess::ExitStatus)));
    QObject::connect(&sqlProc, SIGNAL(error(QProcess::ProcessError)),this,SLOT(sqlProcessError(QProcess::ProcessError)));

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

QString test1::sqlsh_sqlVer(){
    sqlsh_Args();

    QString verargs;
    verargs += "select version()";

    sqlArgs << verargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    QString result = ui->txtSqlOutput->toPlainText();
    return result;
}

//======================================================================================================

QStringList test1::sqlsh_list_database(){
    sqlsh_Args();

    sqlArgs << "show databases;";

    sqlsh_Exec();

    sqlProc.waitForFinished();

    QStringList result = ui->txtSqlOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);
    return result;
}

void test1::sqlsh_delete_default(){
    sqlsh_delete_database("performance_schema");
    sqlsh_delete_database("mysql");
    sqlsh_delete_database("test");
    return;
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

void test1::sqlsh_export_database(QString dbname, QString filedest){

    QProcess sqldumproc;

#if (defined (Q_OS_UNIX))
    sqldumproc.start("bash -c \"mysqldump -uroot " + dbname + " > " + filedest + "\"");
#elif (defined (Q_OS_WIN))
    QStringList sqldumprocargs;

    sqldumprocargs << "/c";
    sqldumprocargs << "mysqldump";
    sqldumprocargs << "-uroot";
    sqldumprocargs << dbname;
    sqldumprocargs << ">";
    sqldumprocargs << filedest;

    sqldumproc.start("cmd",sqldumprocargs);
#endif

    sqldumproc.waitForFinished();
    return;
}

void test1::sqlsh_import_database(QString dbname, QString filesrc){
    QProcess sqlimportproc;

#if (defined (Q_OS_UNIX))
    sqlimportproc.start("bash -c \"mysql -uroot " + dbname + " < " + filesrc + "\"");
#elif (defined (Q_OS_WIN))
    QStringList sqlimportprocargs;

    sqlimportprocargs <<  "/c";
    sqlimportprocargs <<  "mysql";
    sqlimportprocargs <<  "-uroot";
    sqlimportprocargs <<  dbname;
    sqlimportprocargs <<  "<";
    sqlimportprocargs <<  filesrc;

    sqlimportproc.start("cmd",sqlimportprocargs);
#endif

    sqlimportproc.waitForFinished();
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
    tblargs += "debet INT NOT NULL";
    tblargs += "kredit INT NOT NULL";
    tblargs += ")";

    sqlArgs << tblargs;

    sqlsh_Exec();

    sqlProc.waitForFinished();

    return;
}

//======================================================================================================

void test1::sqlsh_insert_data(QString dbname, QString tanggal, QString deskrip, QString nilai, int jenis, int debet, int kredit){
    sqlsh_Args();

    QString insargs;
    insargs += "use " + dbname +";";
    insargs += "insert into `main_data` (`id`,`tanggal`,`transaksi`,`harga`,`jenis`,`debet`,`kredit`) VALUES (NULL,";
    insargs += "\"" + tanggal + "\"" + ",";
    insargs += "\"" + deskrip + "\"" + ",";
    insargs += "\"" + nilai + "\"" + ",";
    insargs += "\"" + QString::number(jenis) + "\"" + ")";
    insargs += "\"" + QString::number(debet) + "\"" + ",";
    insargs += "\"" + QString::number(kredit) + "\"" + ",";

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
