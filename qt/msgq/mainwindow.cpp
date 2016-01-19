#include <QDebug>
#include <QFile>

#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "yosemsg.h"
#include "simplenotify.h"

const QString watch_file = "/home/rasmus/watchfile";

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

    connect(ui->actionHello, SIGNAL(triggered(bool)), this, SLOT(testNotify(bool)));

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

void MainWindow::testNotify(bool b)
{
    (void)b;
    qDebug() << "testNotify():";

    QFile f(watch_file);
    f.open(QIODevice::WriteOnly);
    f.write(QByteArray("test"));
    f.close();

    addline(QString("watch file: ") + watch_file);
    m_sn = new SimpleNotify(watch_file);

    connect(m_sn, SIGNAL(finished()), this, SLOT(showFinished()));
    connect(m_sn, SIGNAL(sigNotify()), this, SLOT(getNotified()));
    m_sn->start();
}

void MainWindow::showStarted()
{
    qDebug() << "started";
}

void MainWindow::getNotified()
{
    disconnect(m_sn, SIGNAL(sigNotify()), this, SLOT(getNotified()));
    addline("MainWindow::getNotified: watch_file is modified");
    delete m_sn;
}

void MainWindow::showFinished()
{
    qDebug() << "showFinished";
}
