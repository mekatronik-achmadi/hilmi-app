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
    QString debet2text(int num_debet);
    QString kredit2text(int num_kredit);

    void view_table(QString dbase);
    void view_pdf(QString dbase);
    void view_search(QString dbase, QString search_field, QString search_string);

private:
    sqlsh *mysql;
};

#endif // SQLDATA_H