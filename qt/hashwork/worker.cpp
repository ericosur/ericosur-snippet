/**
 * \file worker.cpp
 */

#include "worker.h"

#include <QCryptographicHash>
#include <QDebug>

Worker::Worker()
{
    qDebug() << Q_FUNC_INFO << "created...";

    mThread = new QThread();
    moveToThread(mThread);
    mThread->start();
}

void Worker::sltWork()
{
    qDebug() << Q_FUNC_INFO << "start..." << QThread::currentThreadId();
    do_something();
    qDebug() << Q_FUNC_INFO << "end...";
}

void Worker::do_something()
{
    const int REP = 250;
    QByteArray data = "start here...";

    for (int i=0; i<REP; ++i) {
        data.append(qrand());
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        for (int j=0; j<REP; j++) {
            data.append(qrand());
            data.append(QCryptographicHash::hash(data, QCryptographicHash::Sha256));
        }
    }

    QByteArray res = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
    QString answer = res.toHex().data();
    qDebug() << Q_FUNC_INFO << "answer:" << answer;
    //qDebug() << "doHardWork() finished, emit finished()";
}
