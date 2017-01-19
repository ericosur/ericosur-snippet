#include "core.h"
#include <QCoreApplication>
//#include <QThread>
#include <QDir>
#include <QImage>
#include <QImageReader>
#include <QDebug>

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

    // connect(poll, SIGNAL(sigUsbDectected()), this, SLOT(sltUsbDetected()));
    // connect(poll, SIGNAL(sigIpodDectected()), this, SLOT(sltIpodDetected()));
    // connect(poll, SIGNAL(finished()), this, SLOT(sltWaitFinished()));
    //connect(this, SIGNAL(sigQuit()), qApp, SLOT(quit()));

    // prepare filters
    foreach (QByteArray format, QImageReader::supportedImageFormats()) {
        filters += "*." + format;
    }
    qDebug() << "filters:" << filters;

}

void Core::start(const QString& startpath)
{
    qDebug() << Q_FUNC_INFO;
    qDebug() << imageSpace(startpath);
    //emit sigQuit();
}

qlonglong Core::imageSpace(const QString &path)
{
    QDir dir(path);
    qlonglong size = 0;

    //qDebug() << /* Q_FUNC_INFO << */ "path:" << path;

    foreach (QString file, dir.entryList(filters, QDir::Files)) {
        size += QFileInfo(dir, file).size();
    }

    foreach (QString subDir, dir.entryList(QDir::Dirs
                                           | QDir::NoDotAndDotDot)) {
        size += imageSpace(path + QDir::separator() + subDir);
    }

    return size;
}

