#include <QCoreApplication>
#include "flowctrl.h"

FlowControl* FlowControl::_instance = NULL;
FlowControl* FlowControl::getInstance()
{
    if (_instance == NULL) {
        _instance = new FlowControl();
    }
    return _instance;
}

FlowControl::FlowControl()
{
    if (readthead == NULL) {
        readthead = new ReadThread();
    }
    connect(readthead, SIGNAL(finished()), this, SLOT(sltReadFinished()));
    connect(this, SIGNAL(sigQuitApp()), qApp, SLOT(quit()));
}

void FlowControl::start()
{
    qDebug() << Q_FUNC_INFO;

    check_shm();

    // issue an IPC to tell "generator" start send data...
    send_msgq(MESGQKEY_MONITOR, MESGQKEY_MESSAGE_TYPE, "start");

    readthead->start();
}

void FlowControl::sltReadFinished()
{
    qDebug() << Q_FUNC_INFO;
    emit sigQuitApp();
}

void FlowControl::check_shm()
{
    // fill all zero into 0xff
    FileItem _fi;
    memset(&_fi, 0, sizeof(FileItem));
    if (util_shm_write(LOCAL_SHM_KEY, sizeof(FileItem), &_fi) < 0) {
        qWarning() << "shm write failed";
    }

}
