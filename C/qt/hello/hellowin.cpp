#include "hellowin.h"
#include "ui_hellowin.h"

#include <windows.h>

HelloWin::HelloWin(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::HelloWin)
{
    ui->setupUi(this);


}

HelloWin::~HelloWin()
{
    delete ui;
}

void HelloWin::on_pushButton_clicked()
{
    //ui->textEdit->setText("Hello");
    DWORD dw = GetTickCount();
    QString msg;
    msg.setNum((ulong)dw);
    ui->textEdit->append(msg);
}

void HelloWin::on_clearButton_clicked()
{
    ui->textEdit->clear();
}
