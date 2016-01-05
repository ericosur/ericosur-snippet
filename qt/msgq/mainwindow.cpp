#include <QDebug>

#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "yosemsg.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    YoseMsg *msg = new YoseMsg;

    connect(ui->actionHello, SIGNAL(triggered(bool)), this, SLOT(doNothing(bool)));
    connect(msg, SIGNAL(sigReceived(QString)), this, SLOT(gotMessage(QString)));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::gotMessage(const QString& s)
{
    if (s == "") {
        ui->textEdit->setText("null");
    } else {
        ui->textEdit->setText(s);
    }
}

void MainWindow::doNothing(bool b)
{
    qDebug() << "doNothing():" << b;
}
