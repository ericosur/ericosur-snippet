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

    mTravel->dumpId();

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

quint32 Core::make3(quint8 lhs, quint8 mid, quint8 rhs)
{
    return ((lhs << 16) | (mid << 8) | rhs);
}

// show 3-byte integer as binary
// will mask out left-hand-side 8bit from u
void Core::show3(quint32 u)
{
    qDebug() << QString("%1").arg(QString::number(u, 2), 32, QChar('0'));
}

quint32 Core::clean3(quint32 u)
{
    if (u & 0xff000000) {
        qWarning() << "not zero at left-hand-side 8bit!";
    }
    return (u & 0x00ffffff);
}

void Core::test3()
{
    quint32 r = make3(0b00110011, 0b01010101, 0b10101010);
    show3(r);

    r = 0x0defc0de;
    show3(r);
    r = clean3(r);
    show3(r);

    show3(0b001111111111111111111111);
    show3(0x3fffff);
    // so id from 1 to 0x3fffff
    // left-most 2bit are using as type id: 0b00, 0b01, 0b10, 0b11
}
