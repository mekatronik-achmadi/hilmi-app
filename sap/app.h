#ifndef APP_H
#define APP_H

#include <QMainWindow>
#include "inclusion.h"

class app : public QMainWindow
{
    Q_OBJECT
public:
    explicit app(QWidget *parent = 0);

signals:

public slots:
    void msg_about(void);

private:
    sqlsh *mysql;
};

#endif // APP_H
