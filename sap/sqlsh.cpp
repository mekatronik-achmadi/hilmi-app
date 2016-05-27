#include "sqlsh.h"

sqlsh::sqlsh(QWidget *parent) : QMainWindow(parent)
{
    txtProcOutput = new QPlainTextEdit;

    QObject::connect(&sqlProc, SIGNAL(readyReadStandardOutput()),this, SLOT(processOnGoing()));
    QObject::connect(&sqlProc, SIGNAL(finished(int, QProcess::ExitStatus)),this,SLOT(processFinished(int, QProcess::ExitStatus)));
    QObject::connect(&sqlProc, SIGNAL(error(QProcess::ProcessError)),this,SLOT(processError(QProcess::ProcessError)));
}

//======================================================================================================

void sqlsh::processOnGoing(){
    QByteArray newData = sqlProc.readAllStandardOutput();
    txtProcOutput->appendPlainText(QString::fromLocal8Bit(newData));

    return;
}

void sqlsh::processFinished(int exitCode, QProcess::ExitStatus exitStatus){
    (void) exitCode;

    if (exitStatus == QProcess::CrashExit) {
        QMessageBox::critical(this,"Crashed","Database Driver Crashed");
    }

    return;
}

void sqlsh::processError(QProcess::ProcessError error){

    if (error == QProcess::FailedToStart) {
        QMessageBox::critical(this,"Not Found","Database Driver not found");
    }

    return;
}

//======================================================================================================

void sqlsh::procArgs(){
    txtProcOutput->clear();
    sqlArgs.clear();

    sqlArgs << "-BN";
    sqlArgs << "-uroot";
    sqlArgs << "-e";

    return;
}

void sqlsh::procExec(){
    sqlProc.start("mysql",sqlArgs);
    sqlProc.waitForFinished();
    return;
}

//======================================================================================================

QString sqlsh::procSqlVersion(){
    procArgs();

    QString verargs;
    verargs += "select version()";

    sqlArgs << verargs;
    procExec();

    QString result = txtProcOutput->toPlainText();
    return result;
}

QString sqlsh::procCmdVersion(){
    txtProcOutput->clear();

    sqlProc.start("bash -c \"echo $BASH_VERSION\"");

    sqlProc.waitForFinished();

    QString result = txtProcOutput->toPlainText();
    return result;
}

QString sqlsh::procOsVersion(){
    QString result;

    txtProcOutput->clear();

#if (defined (Q_OS_LINUX))
    sqlProc.start("bash -c \"uname -r\"");

    sqlProc.waitForFinished();

    QString result_linux = txtProcOutput->toPlainText();

    result = result_linux;
#elif (defined (Q_OS_WIN))

    sqlProc.start("cmd /c ver");

    sqlProc.waitForFinished();

    QStringList result_win = txtProcOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);;

    result = result_win[0];
#endif

    return result;
}

//======================================================================================================

void sqlsh::create_database(QString dbname){
    procArgs();

    QString dbargs;
    dbargs += "create database ";
    dbargs += dbname;

    sqlArgs << dbargs;

    procExec();

    return;
}

void sqlsh::delete_database(QString dbname){
    procArgs();

    QString dbargs;
    dbargs += "drop database ";
    dbargs += dbname;

    sqlArgs << dbargs;

    procExec();

    return;
}

void sqlsh::export_database(QString dbname, QString filedest){

    QProcess sqldumpproc;

#if (defined (Q_OS_LINUX))
    sqldumpproc.start("bash -c \"mysqldump -uroot " + dbname + " > " + filedest + "\"");
#elif (defined (Q_OS_WIN))
    QStringList sqldumpprocargs;

    sqldumpprocargs << "/c";
    sqldumpprocargs << "mysqldump";
    sqldumpprocargs << "-uroot";
    sqldumpprocargs << dbname;
    sqldumpprocargs << ">";
    sqldumpprocargs << filedest;

    sqldumpproc.start("cmd",sqldumpprocargs);
#endif

    sqldumpproc.waitForFinished();
    return;
}

void sqlsh::import_database(QString dbname, QString filesrc){
    QProcess sqlimportproc;

#if (defined (Q_OS_LINUX))
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

QStringList sqlsh::list_database(){
    procArgs();

    sqlArgs << "show databases;";

    procExec();

    QStringList result = txtProcOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);
    return result;
}

void sqlsh::delete_default(){
    delete_database("performance_schema");
    delete_database("mysql");
    delete_database("test");
    return;
}

void sqlsh::create_table(QString dbname){
    procArgs();

    QString tblargs;
    tblargs += "use " + dbname +";";
    tblargs +=  "create table main_data(";
    tblargs += "id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,";
    tblargs += "tanggal DATE NOT NULL,";
    tblargs += "transaksi VARCHAR(32) NOT NULL,";
    tblargs += "harga VARCHAR(32) NOT NULL,";
    tblargs += "jenis INT NOT NULL,";
    tblargs += "debet INT NOT NULL,";
    tblargs += "kredit INT NOT NULL";
    tblargs += ")";

    sqlArgs << tblargs;

    procExec();

    return;
}

//======================================================================================================

void sqlsh::data_insert(QString dbname, QString tanggal, QString deskrip, QString nilai, int jenis, int debet, int kredit){
    procArgs();

    QString insargs;
    insargs += "use " + dbname +";";
    insargs += "insert into `main_data` (`id`,`tanggal`,`transaksi`,`harga`,`jenis`,`debet`,`kredit`) VALUES (NULL,";
    insargs += "\"" + tanggal + "\"" + ",";
    insargs += "\"" + deskrip + "\"" + ",";
    insargs += "\"" + nilai + "\"" + ",";
    insargs += "\"" + QString::number(jenis) + "\"" + ",";
    insargs += "\"" + QString::number(debet) + "\"" + ",";
    insargs += "\"" + QString::number(kredit) + "\"" + ")";

    sqlArgs << insargs;

    procExec();

    return;
}

QStringList sqlsh::data_get_one_column(QString dbname, QString field){
    procArgs();

    QString getargs;
    getargs += "use " + dbname +";";
    getargs += "select " + field + " from main_data";

    sqlArgs << getargs;

    procExec();

    QStringList result = txtProcOutput->toPlainText().split(QRegExp("\n"),QString::SkipEmptyParts);
    return result;
}

