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
    connect(this, SIGNAL(sigGetfolder()), this, SLOT(sltGetfolder()));
}

void FlowControl::start()
{
    qDebug() << Q_FUNC_INFO;

    if (mFileFinished == false) {
        check_shm();
        // issue an IPC to tell "generator" start send data...
        send_msgq(MESGQKEY_MONITOR, MESGQKEY_MESSAGE_TYPE, "start");
        readthead->setReadItemType(AUDIO_ITEM);
        readthead->start();
    }
}

void FlowControl::sltGetfolder()
{
    if (!mFileFinished) {
        qWarning() << "why? file transfer not done...";
        return;
    }
    if (mFolderFinished == false) {
        requestGetfolder();
    }
}

void FlowControl::requestGetfolder()
{
    qDebug() << Q_FUNC_INFO;

    check_shm();
    // issue an IPC to tell "generator" start send data...
    send_msgq(MESGQKEY_MONITOR, MESGQKEY_MESSAGE_TYPE, "getfolder");
    readthead->setReadItemType(FOLDER_ITEM);
    readthead->start();
}

void FlowControl::sltReadFinished()
{
    qDebug() << Q_FUNC_INFO;
    if (mFileFinished == false) {
        mFileFinished = true;
        emit sigGetfolder();
    } else if (mFolderFinished == false) {
        mFolderFinished = true;
    }

    if (mFileFinished && mFolderFinished) {
        emit sigQuitApp();
    }
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
