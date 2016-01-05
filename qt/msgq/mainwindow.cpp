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

//    QObject::connect(&thread, SIGNAL(finished()), qApp, SLOT(quit()));
//    QObject::connect(&thread, SIGNAL(received(QString)), &thread, SLOT(print(QString)));
//    thread.start();

    connect(msg, SIGNAL(finished()), this, SLOT(close()));
    connect(msg, SIGNAL(sigReceived(QString)), this, SLOT(gotMessage(QString)));
    connect(msg, SIGNAL(started()), this, SLOT(showStarted()));

    connect(ui->actionHello, SIGNAL(triggered(bool)), this, SLOT(doNothing(bool)));

    msg->start();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::addline(const QString& s)
{
    ui->textEdit->append(s);
}

void MainWindow::gotMessage(const QString& s)
{
    if (s == "") {
        addline("null");
    } else {
        addline(s);
    }
}

void MainWindow::doNothing(bool b)
{
    qDebug() << "doNothing():" << b;
}

void MainWindow::showStarted()
{
    qDebug() << "started";
}
