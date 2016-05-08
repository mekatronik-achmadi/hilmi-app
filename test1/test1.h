#ifndef TEST1_H
#define TEST1_H

#include <QMainWindow>

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
    void on_actionExit_triggered();

    void on_actionAboutQt_triggered();

private:
    Ui::test1 *ui;
};

#endif // TEST1_H
