#include "mycontroller.h"

#include <QCryptographicHash>
#include <QThread>
#include <QTimer>
#include <QDebug>

MyController::MyController() :
    m_input("cafe")
    , m_result("beef")
{
    m_worker = new Worker("Startup");
    m_thread = new QThread;

    m_worker->moveToThread( m_thread );

    // Init connections.
    connect(this, SIGNAL(startWork()), m_worker, SLOT(doHardWork()));
    connect(m_worker, SIGNAL(finished()), this, SLOT(onFinishWork()));
    connect(this, SIGNAL(issueCleanup()), m_thread, SLOT(quit()));
    //connect(this, SIGNAL(issueCleanup()), m_worker, SLOT(deleteLater()));
    //connect(this, SIGNAL(issueCleanup()), m_thread, SLOT(deleteLater()));
    connect(m_thread, SIGNAL(destroyed(QObject*)), this, SLOT(onNotified(QObject*)));
    connect(m_worker, SIGNAL(destroyed(QObject*)), this, SLOT(onNotified(QObject*)));
    //connect(m_worker, SIGNAL(finished()), m_thread, SLOT(quit()));
    //connect(m_worker, SIGNAL(finished()), m_worker, SLOT(deleteLater()));
    //connect(m_thread, SIGNAL(finished()), m_thread, SLOT(deleteLater()));
    connect(m_thread, SIGNAL(finished()), this, SLOT(onFinished()) );

    m_thread->start();
}

MyController::~MyController()
{
    delete m_worker;
    delete m_thread;
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

bool MyController::invokeWork()
{
    qDebug() << "invokeWork() working thread : " << QThread::currentThreadId();

    m_result = "Start working...";
    emit resultChanged();

    if( !m_thread->isFinished() )
    {
        emit startWork();
        return true;
    }
    else
    {
        qDebug() << "Error!! m_thread has been finished.";
        return false;
    }
}

void MyController::onNotified(QObject *obj)
{
    qDebug() << "onNotified()..." << obj;
}

void MyController::onFinishWork()
{
    qDebug() << "MyController::onFinished()";
    m_result = m_worker->getResult();
    //qDebug() << "m_result: " << m_result;

    qDebug() << "emit resultChanged()";
    emit resultChanged();
}

void MyController::finish()
{
    emit issueCleanup();
}

void MyController::onFinished()
{
    qDebug() << "Get signal 'Finished'.";
    exit(0);
}


Worker::Worker(const QString& s) :
    m_win(s),
    m_wout("")
{}

void Worker::doHardWork()
{
    qDebug() << "worker thread id: " << QThread::currentThreadId();
    qDebug() << "doHardWork() start...";

    const int REP = 300;
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
    qDebug() << "doHardWork() finished, emit finished()";
    emit finished();
}
