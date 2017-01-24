#include "core.h"
#include <QCoreApplication>
#include <QThread>
#include <QDebug>

#ifdef USE_YOSETARGET
#include <libmsgq.h>
#include <libhu_system.h>
#else
#define svc_dispatch(m,n,p,q)  \
    qDebug() << "svc_dispatch() debug mode..."
#endif

Core* Core::_instance = NULL;
Core* Core::getInstance()
{
    if (_instance == NULL) {
        _instance = new Core();
    }
    return _instance;
}

Core::Core()
{
    qDebug() << Q_FUNC_INFO << "created...";

    // thread to receive msgq
    if (poll == NULL) {
        poll = new PollThread();
    }
    if (worker == NULL) {
        worker = new Worker();
    }

    connect(poll, SIGNAL(finished()), this, SLOT(sltWaitFinished()));
    connect(this, SIGNAL(sigQuit()), qApp, SLOT(quit()));
    connect(this, SIGNAL(sigWork()), worker, SLOT(sltWork()));
}

void Core::sltWaitFinished()
{
    qDebug() << "poll thread is finished... and exit...";
    emit sigQuit();
}

void Core::start()
{
    if (poll == NULL) {
        qWarning() << "poll thread is NULL, failed to run...";
    } else {
        emit sigWork();
        poll->start();
    }
}
