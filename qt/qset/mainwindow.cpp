
#include "mainwindow.h"

#include <QSettings>
#include <QTextCodec>
#include <QDebug>

#define QSET_INI    "/tmp/qset.ini"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , m_threadcount(0)
    , m_counter(0)
    , m_timer(NULL)
    , m_setting(NULL)
{
    init_settings();
    qsrand(qrand());

    foo1 = new ThreadFoo(0, QString::number(qrand(), 16));
    foo2 = new ThreadFoo(1, QString::number(qrand(), 16));
    foo3 = new ThreadFoo(2, QString::number(qrand(), 16));

    connect(foo1, SIGNAL(started()), this, SLOT(onStarted()));
    connect(foo2, SIGNAL(started()), this, SLOT(onStarted()));
    connect(foo3, SIGNAL(started()), this, SLOT(onStarted()));
    connect(foo1, SIGNAL(finished()), this, SLOT(onFinished1()));
    connect(foo2, SIGNAL(finished()), this, SLOT(onFinished2()));
    connect(foo3, SIGNAL(finished()), this, SLOT(onFinished3()));

    m_timer = new QTimer(this);
    connect(m_timer, SIGNAL(timeout()), this, SLOT(onTimeout()));
    m_timer->start(1000);

    m_epoch = new QElapsedTimer;
    m_epoch->start();

    foo1->start();
    foo2->start();
    foo3->start();
}

MainWindow::~MainWindow()
{
}
void MainWindow::init_settings()
{
    QTextCodec *codec = QTextCodec::codecForName("UTF-8");
    m_setting = new QSettings(QSET_INI, QSettings::IniFormat);
    m_setting->setIniCodec(codec);

    //m_setting->setValue("editor/wrapMargin", 68);
    //m_setting->setValue("%U4E2D%U6587", "chinese characters");
    //m_setting->setValue("地點/地址", "台北市北投區承德路7段400號");
    qDebug() << "ini path: " << QSET_INI;
}

void MainWindow::onStarted()
{
    qDebug() << "onStarted...";
    m_threadcount ++;
    m_setting->setValue(QString("start_") + QString::number(m_threadcount), m_epoch->elapsed());
}

void MainWindow::onFinished1()
{
    quint64 e = m_epoch->elapsed();
    qDebug() << "onFinished 1... @" << e;
    m_threadcount --;
    m_setting->setValue(QString("finish_1"), e);
    if (m_threadcount <= 0) {
        m_timer->stop();
        this->close();
    }
}
void MainWindow::onFinished2()
{
    quint64 e = m_epoch->elapsed();
    qDebug() << "onFinished 2... @" << e;
    m_threadcount --;
    m_setting->setValue(QString("finish_2"), e);
    if (m_threadcount <= 0) {
        m_timer->stop();
        this->close();
    }
}
void MainWindow::onFinished3()
{
    quint64 e = m_epoch->elapsed();
    qDebug() << "onFinished 3... @" << e;
    m_threadcount --;
    m_setting->setValue(QString("finish_3"), e);
    if (m_threadcount <= 0) {
        m_timer->stop();
        this->close();
    }
}

void MainWindow::onTimeout()
{
    m_counter ++;
    quint64 e = m_epoch->elapsed();
    m_setting->setValue(QString("timeout_") + QString::number(m_counter), m_epoch->elapsed());
    qDebug() << "onTimeout() epoch:" << e << "threads:" << m_threadcount << " timeout:" << m_counter;
}
