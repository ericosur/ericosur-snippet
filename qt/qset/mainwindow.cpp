
#include "mainwindow.h"

#include <QSettings>
#include <QTextCodec>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , m_threadcount(0)
    , m_counter(0)
    , m_timer(NULL)
    , m_settings(NULL)
{
    init_settings();
    foo = new ThreadFoo(m_settings);
    bar = new ThreadBar(m_settings);

    connect(foo, SIGNAL(started()), this, SLOT(onStarted()));
    connect(foo, SIGNAL(finished()), this, SLOT(onFinished()));
    connect(bar, SIGNAL(started()), this, SLOT(onStarted()));
    connect(bar, SIGNAL(finished()), this, SLOT(onFinished()));

    m_timer = new QTimer(this);
    connect(m_timer, SIGNAL(timeout()), this, SLOT(onTimeout()));
    m_timer->start(100);

    m_epoch = new QElapsedTimer;
    m_epoch->start();

    foo->start();
    bar->start();
}

MainWindow::~MainWindow()
{
}

void MainWindow::init_settings()
{
    QTextCodec *codec = QTextCodec::codecForName("UTF-8");
    m_settings = new QSettings("/tmp/qset.ini", QSettings::IniFormat);
    m_settings->setIniCodec(codec);

    m_settings->setValue("editor/wrapMargin", 68);
    m_settings->setValue("%U4E2D%U6587", "chinese characters");
    m_settings->setValue("地點/地址", "台北市北投區承德路7段400號");
}

void MainWindow::onStarted()
{
    qDebug() << "onStarted...";
    m_threadcount ++;
}

void MainWindow::onFinished()
{
    qDebug() << "onFinished...";
    m_threadcount --;
    if (m_threadcount <= 0) {
        m_timer->stop();
        this->close();
    }
}

void MainWindow::onTimeout()
{
    m_counter ++;
    quint64 e = m_epoch->elapsed();

    qDebug() << "onTimeout() epoch:" << e << "threads:" << m_threadcount << " timeout:" << m_counter;

}
