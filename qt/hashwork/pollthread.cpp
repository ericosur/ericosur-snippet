#include <QDebug>
#include <QThread>
#include <QCryptographicHash>
#include <QDateTime>

#include "pollthread.h"

#define DEFAULT_BUFFER_SIZE     (1024)

PollThread::PollThread()
{
    qDebug() << Q_FUNC_INFO << "created...";
}

void PollThread::run()
{
    qDebug() << Q_FUNC_INFO << "running..." << QThread::currentThreadId();
    do_hard_work();
    qDebug() << Q_FUNC_INFO << "finished...";
}

QByteArray PollThread::fill_buffer(const int size)
{
    qsrand(QDateTime::currentMSecsSinceEpoch() / 1000);
    QByteArray arr;
    for (int i = 0; i < size; i++) {
        arr.append( char(qrand() % 255 + 1) );
    }
    return arr;
}

void PollThread::do_hard_work()
{
    //qDebug() << Q_FUNC_INFO << "starts...";

    const int REP = 280;
    QByteArray data = fill_buffer(DEFAULT_BUFFER_SIZE);

    for (int i=0; i<REP; ++i) {
        data.append(qrand());
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        for (int j=0; j<REP; j++) {
            data.append(qrand());
            data.append(QCryptographicHash::hash(data, QCryptographicHash::Sha256));
        }
    }

    QByteArray res = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
    mAnswer = res.toHex().data();
    qDebug() << Q_FUNC_INFO << "answer:" << mAnswer;
    //qDebug() << "doHardWork() finished, emit finished()";
}
