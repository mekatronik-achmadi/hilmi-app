#include "app.h"

app::app(QWidget *parent) : QMainWindow(parent)
{
    mysql = new sqlsh;
}

void app::msg_about(){
    QString qtver= QT_VERSION_STR;
    QString mysqlver = mysql->procSqlVersion();

    QString aboutmsg;

    aboutmsg += "Simple Accounting Program \n";
    aboutmsg += "\n";

    aboutmsg += "Credit: \n";
    aboutmsg += "Accounting Scheme written by Hilmi F. \n";
    aboutmsg += "GUI Program written by Achmadi \n";
    aboutmsg += "\n";

    aboutmsg += "Using: \n";
    aboutmsg += "Qt version " + qtver + "\n";
    aboutmsg += "MySQL version " + mysqlver;

#if (defined (Q_OS_LINUX))
    QString bashver = mysql->procCmdVersion();
    aboutmsg += "Bash version " + bashver;

    QString osver = mysql->procOsVersion();
    aboutmsg += "Linux version " + osver;

    aboutmsg += "\n";
#elif (defined (Q_OS_WIN))
    QString osver = mysql->procOsVersion();
    aboutmsg += "OS version " + osver;

    aboutmsg += "\n";
#endif

    QMessageBox::information(this,"About Me",aboutmsg);
}
