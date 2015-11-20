#include "jobcontrol.h"

#include <QDebug>
#include <QCryptographicHash>

//////////////////////////////////////////////////////////////////////////////
JobWorker::JobWorker()
{
    // nothing here
    m_working = false;
}


#if 0
void doSomeEncryption()
{
    const int REP = 300;
    QByteArray data;

    //qDebug() << "signalsBlocked()? " << (signalsBlocked() ? "yes" : "no");
    data.append("Job start...");

    for (int i=0; i<REP; ++i) {
        data.append(qrand());
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        for (int j=0; j<REP; j++) {
            data.append(qrand());
            data.append(QCryptographicHash::hash(data, QCryptographicHash::Sha256));
        }
    }

    QByteArray res = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
    QString strData = res.toHex().data();
}
#endif


void JobWorker::doJobWork(const QString& cmd)
{
    qDebug() << "doJobWork() start...";
    runCommand(cmd);
    //qDebug() << "doJobWork() finished, emit JobFinished() " << strData;
    endJobWork();
}

void JobWorker::endJobWork()
{
    //qDebug() << "endJobWork";
    emit sigJobFinished();
}

void JobWorker::runCommand(const QString& cmd)
{
    connect(&m_process, SIGNAL(finished(int)), this, SLOT(slotFinished(int)));
    connect(&m_process, SIGNAL(readyReadStandardOutput()), this, SLOT(slotReadStdout()));

    m_process.start(cmd);
    m_process.waitForFinished(-1); // will wait forever until finished
}

void JobWorker::slotFinished(int i)
{
    qDebug() << "slotFinished(): " << i;
    disconnect(&m_process, SIGNAL(finished(int)), 0, 0);
    disconnect(&m_process, SIGNAL(readyReadStandardOutput()), 0, 0);
    disconnect(&m_process, SIGNAL(readyReadStandardError()), 0, 0);
}

void JobWorker::slotReadStdout()
{
    qDebug() << "slotReadStdout";
//    char stdbuf[DEFAULT_BUFFER_SIZE];
//    qint64 len = m_process.readLine(stdbuf, DEFAULT_BUFFER_SIZE);
//    if (len != -1) {
//        // the line is available in buf
//        addline(QString::fromUtf8(stdbuf));
//    }

    QByteArray arr = m_process.read(DEFAULT_BUFFER_SIZE);
    // the line is available in buf
    addline(QString::fromUtf8(arr));

}

void JobWorker::slotReadStderr()
{
    qDebug() << "slotReadStderr";
    QByteArray arr = m_process.read(DEFAULT_BUFFER_SIZE);
    // the line is available in buf
    //addline(QString::fromUtf8(arr));
    emit sigOutputChanged(arr);
}


//////////////////////////////////////////////////////////////////////////////

JobControl::JobControl()
{
    m_cmd = "";
    m_worker = new JobWorker();
    m_thread = new QThread;
    m_worker->moveToThread( m_thread );

    // Init connection
    connect(this, SIGNAL(sigHasJob()), m_worker, SLOT(doJobWork(const QString&)));
    connect(m_worker, SIGNAL(sigJobFinished()), this, SLOT(onFinishWork()));
    connect(m_worker, SIGNAL(sigOutputChanged(const QByteArray&)), this, SLOT(onOutputChanged(const QByteArray&)));
    connect(this, SIGNAL(sigIssueCleanup()), m_thread, SLOT(quit()));
    connect(m_thread, SIGNAL(finished()), this, SLOT(onFinished()) );

    m_thread->start();
}

JobControl::~JobControl()
{
    delete m_worker;
    //delete m_thread;
    emit issueCleanup();
}

void JobControl::startJob()
{
    //qDebug() << "startJob()..." << receivers(SIGNAL(Job));

    emit hasJob();
}

void JobControl::finishJob()
{
    emit issueCleanup();
}

void JobControl::onFinishWork()
{
    emit sigResultChanged();
}

void JobControl::onFinished()
{
    //qDebug() << "Get signal 'Finished'.";
    exit(0);
}

void JobControl::onOutputChanged(const QByteArray& array)
{
    m_array = array;
}

//////////////////////////////////////////////////////////////////////////////
