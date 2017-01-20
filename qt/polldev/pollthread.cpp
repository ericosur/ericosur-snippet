#include <QDebug>
#include <QThread>

#include "pollthread.h"

#define SLEEP_DURING_POLLING    (750)

PollThread::PollThread()
{
    qDebug() << Q_FUNC_INFO << "created";
}

void PollThread::run()
{
    qDebug() << Q_FUNC_INFO << "running...";
    while ( true ) {
        if ( status_get_dev(DEV_USB) ) {
            // usb exists...
            emit sigUsbDectected();
            qDebug() << "and break...";
            break;
        }
        if ( status_get_dev(DEV_IPOD) ) {
            // iPod detected
            emit sigIpodDectected();
            qDebug() << "and break...";
            break;
        }
        QThread::msleep(SLEEP_DURING_POLLING);
    }
    qDebug() << Q_FUNC_INFO << "finished...";
}
