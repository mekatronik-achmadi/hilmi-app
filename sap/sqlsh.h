#ifndef H
#define H

#include <QMainWindow>
#include <QPlainTextEdit>
#include <QMessageBox>
#include <QProcess>

class sqlsh : public QMainWindow
{
    Q_OBJECT
public:
    explicit sqlsh(QWidget *parent = 0);

signals:

public slots:
    void processOnGoing(void);
    void processFinished(int exitCode, QProcess::ExitStatus exitStatus);
    void processError(QProcess::ProcessError error);

    void procArgs(void);
    void procExec(void);

    QString procSqlVersion(void);
    QString procCmdVersion(void);
    QString procOsVersion(void);

    void create_database(QString dbname);
    void delete_database(QString dbname);
    void export_database(QString dbname,QString filedest);
    void import_database(QString dbname,QString filesrc);
    QStringList list_database(void);
    void delete_default();
    void create_table(QString dbname);

    void data_insert(QString dbname, QString tanggal, QString deskrip, QString nilai, int jenis, int debet, int kredit);
    QStringList data_get_one_column(QString dbname,QString field);


private:
    QPlainTextEdit *txtProcOutput;
    QProcess sqlProc;
    QStringList sqlArgs;
};

#endif // H
