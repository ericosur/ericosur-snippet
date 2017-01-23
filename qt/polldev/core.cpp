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

    connect(poll, SIGNAL(sigUsbDectected()), this, SLOT(sltUsbDetected()));
    connect(poll, SIGNAL(sigIpodDectected()), this, SLOT(sltIpodDetected()));
    connect(poll, SIGNAL(finished()), this, SLOT(sltWaitFinished()));
    connect(this, SIGNAL(sigQuit()), qApp, SLOT(quit()));
}

void Core::launchIpod()
{
    qDebug() << Q_FUNC_INFO;
    svc_dispatch(ZONE_FRONT, SVC_HMI_IPOD, ACT_ON, NULL);
}

void Core::launchMedia()
{
    qDebug() << Q_FUNC_INFO;
    svc_dispatch(ZONE_FRONT, SVC_HMI_USB, ACT_ON, NULL);
}

void Core::sltUsbDetected()
{
    qDebug() << "USB detected...";
    launchMedia();

    QThread::msleep(1000);
    qDebug() << "and quit...";
    emit sigQuit();
}

void Core::sltIpodDetected()
{
    qDebug() << "iPod detected...";
    launchIpod();

    QThread::msleep(1000);
    qDebug() << "and quit...";
    emit sigQuit();
}

void Core::sltWaitFinished()
{
    qDebug() << "poll thread is finished...";
}

void Core::start()
{
    if (poll == NULL) {
        qWarning() << "poll thread is NULL, failed to run...";
    } else {
        poll->start();
    }
}
