/// file: mydatasource.cpp

#include "mydatasource.h"

#include <QString>
#include <QDebug>
#include <QBuffer>
#include <QFile>
#include <QDataStream>

#include "../yoseshm.h"

myDataSource::myDataSource()
{
}

void myDataSource::loadAction()
{
    qDebug() << Q_FUNC_INFO;
}

void myDataSource::checkAction()
{
    qDebug() << Q_FUNC_INFO;
}

void myDataSource::quitAction()
{
    qDebug() << Q_FUNC_INFO;
    emit sigAskQuit();
}

void myDataSource::sltRead(const QString &s)
{
    qDebug() << Q_FUNC_INFO << s;
    readFromShared();
}

void myDataSource::sltMd5sum(const QString &s)
{
    qDebug() << Q_FUNC_INFO << s;
}

void myDataSource::sltWrite()
{
    qDebug() << Q_FUNC_INFO;
    writeToShared();
}

void myDataSource::readFromShared()
{
    qDebug() << Q_FUNC_INFO;
    const int MAX_BUFFER_SIZE = 4096;
    char* buffer = new char[MAX_BUFFER_SIZE];
    uint32_t size = 0;
    myShm::readFromShm(size, buffer);
    qDebug() << "size: " << size;
    QByteArray ar(buffer);
    qDebug() << "ar: " << ar;
}

void myDataSource::writeToShared()
{
    qDebug() << Q_FUNC_INFO;
    QFile f("/etc/hosts");
    if (!f.open(QIODevice::ReadOnly)) {
        qWarning("Couldn't open file.");
        return;
    }
    QByteArray buffer = f.readAll();
    int size = buffer.size();
    qDebug() << "size: " << size;
    myShm::saveToShm(size, buffer.constData());
}
