#include "sap.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    sap w;
    w.show();

    return a.exec();
}
