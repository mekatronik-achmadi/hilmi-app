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

    sqlArgs << "-N";
    sqlArgs << "-B";
    sqlArgs << "-uroot";
    sqlArgs << "-e";

    return;
}

void test1::sqlsh_Exec(){
    sqlProc.start("mysql",sqlArgs);

    return;
}

void test1::sqlsh_list_database(){
    sqlsh_Args();

    sqlArgs << "show databases;";

    sqlsh_Exec();

    sqlProc.waitForFinished();

    return;
}
