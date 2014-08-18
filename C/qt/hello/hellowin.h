#ifndef HELLOWIN_H
#define HELLOWIN_H

#include <QtGui/QMainWindow>

#include "ui_hellowin.h"

namespace Ui
{
    class HelloWin;
}

class HelloWin : public QMainWindow
{
    Q_OBJECT

public:
    HelloWin(QWidget *parent = 0);
    ~HelloWin();

private slots:
    void on_pushButton_clicked();
    void on_clearButton_clicked();

private:
    Ui::HelloWin *ui;
};

#endif // HELLOWIN_H
