#ifndef SQLDATA_H
#define SQLDATA_H

#include <QMainWindow>
#include <QTableWidget>
#include <QFileDialog>
#include <QTextDocument>
#include <QtPrintSupport/QPrinter>

#include "sqlsh.h"

class sqldata : public QMainWindow
{
    Q_OBJECT
public:
    explicit sqldata(QWidget *parent = 0);

signals:

public slots:
    int jenis2debet(int num_jenis);
    int jenis2kredit(int num_jenis);

    QString jenis2text(int num_jenis);
    QString debet2text(int num_jenis);
    QString kredit2text(int num_jenis);

    void view_table(QString dbase);
    void view_pdf(QString dbase);

private:
    sqlsh *mysql;
};

#endif // SQLDATA_H
