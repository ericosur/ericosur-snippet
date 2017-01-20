#include "core.h"
#include "travelthread.h"

#include <stdio.h>

#define FLIST  "/tmp/flist.txt"
#define PLIST  "/tmp/plist.txt"

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

    if (mTravel == NULL) {
        mTravel = new TravelThread();
    }
    // connect(poll, SIGNAL(sigUsbDectected()), this, SLOT(sltUsbDetected()));
    // connect(poll, SIGNAL(sigIpodDectected()), this, SLOT(sltIpodDetected()));
    connect(mTravel, SIGNAL(finished()), this, SLOT(sltWaitFinished()));
    connect(this, SIGNAL(sigQuit()), qApp, SLOT(quit()));

}

void Core::start(const QString& startpath)
{
    qDebug() << Q_FUNC_INFO << startpath;
    if (mTravel == NULL) {
        qWarning() << "travel thread is NULL, exit...";
        return;
    }
    mTravel->setStartPath(startpath);
    mTravel->start();
}

void Core::sltWaitFinished()
{
    qDebug() << Q_FUNC_INFO << "thread finished";
    dumpList(mTravel->getFilelist(), FLIST);
    dumpList(mTravel->getPathlist(), PLIST);
    //mTravel->dumpFolderList();
    mTravel->dumpFolderHash();
    mTravel->clearFolderHash();

    emit sigQuit();
}

void Core::dumpList(const QStringList& list, const QString& fn)
{
    qDebug() << "dumpList(): size:" << list.size()
        << "to file:" << fn;
    FILE* fptr = fopen(fn.toUtf8().constData(), "w");
    if (fptr == NULL) {
        qWarning() << "cannot output to file:" << fn;
        return;
    }
    QStringList::const_iterator constIterator;
    for (constIterator = list.constBegin(); constIterator != list.constEnd();
           ++constIterator) {
        //qDebug() << (*constIterator).toLocal8Bit().constData();
        //
        fprintf(fptr, "%s\n", (*constIterator).toUtf8().constData());
    }
}
