#include "mycontroller.h"

#include <QCryptographicHash>
#include <QThread>
#include <QTimer>
#include <QDebug>

MyController::MyController(QObject* parent) :
    m_input("cafe")
    , m_result("beef")
{
    m_worker = NULL;
    m_thread = NULL;
}
MyController::~MyController()
{
}
QString MyController::getResult() const
{
    return m_result;
}
void MyController::setResult(const QString &s)
{
    m_result = s;
}
QString MyController::getInput() const
{
    return m_input;
}
void MyController::setInput(const QString &s)
{
    m_input = s;
}
void MyController::errString(const QString &s)
{
    m_error = s;
}

bool MyController::invokeWork()
{
    qDebug() << "invokeWork()";
    m_result = "working...";
    emit resultChanged();

    //m_timer = new QTimer;
    m_thread = new QThread;
    m_worker = new Worker("startup");
    m_worker->moveToThread(m_thread);

    QObject::connect(m_worker, SIGNAL(workError(const QString&)), this, SLOT(errString(const QString&)));
    QObject::connect(m_thread, SIGNAL(started()), m_worker, SLOT(doHardWork()));

    connect(m_worker, SIGNAL(finished()), m_thread, SLOT(quit()));
    connect(m_worker, SIGNAL(finished()), m_worker, SLOT(deleteLater()));
    connect(m_thread, SIGNAL(finished()), m_thread, SLOT(deleteLater()));
    connect(m_worker, SIGNAL(finished()), this, SLOT(onFinished()));
    m_thread->start();

    return true;
}

void MyController::onFinished()
{
    qDebug() << "MyController::onFinished()";
    m_result = m_worker->getResult();
    emit resultChanged();
}
/*
void MyController::onProgress(int m)
{
    qDebug() << "MyController::onProgress(): " << m;
}
*/
Worker::Worker(const QString& s) :
    m_win(s),
    m_wout("")
{
}

void Worker::doHardWork()
{
    qDebug() << "doHardWork()";
    const int REP = 275;
    QByteArray data;

    data.append(m_win);
    for (int i=0; i<REP; ++i) {
        data.append(qrand());
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        for (int j=0; j<REP; j++) {
            data.append(qrand());
            data.append(QCryptographicHash::hash(data, QCryptographicHash::Sha256));
        }
        //emit workProgress(i);
    }
    //qDebug() << "data: " << data;
    QByteArray res = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
    m_wout = res.toHex().data();
    //qDebug() << "m_wout: " << m_wout;
    qDebug() << "doHardWork() finished";
    emit finished();
}

void Worker::workError(const QString& s)
{
    qDebug() << "workError(): " << s;
}
