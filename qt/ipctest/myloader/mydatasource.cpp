/// file: mydatasource.cpp

#include "mydatasource.h"

#include <QString>
#include <QDebug>
#include <QBuffer>
#include <QFile>
#include <QDataStream>

const QString sharedkey = "carpediam";
const int shared_size = 4096;

myDataSource::myDataSource()
{
    m_shared = new QSharedMemory(sharedkey, this);
}

void myDataSource::loadAction()
{
    qDebug() << Q_FUNC_INFO;
}

void myDataSource::checkAction()
{
    qDebug() << Q_FUNC_INFO;
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

    QBuffer buffer;
    //QDataStream in(&buffer);

    m_shared->lock();

    buffer.setData(static_cast<const char *>(m_shared->constData()), m_shared->size());
    buffer.open(QBuffer::ReadWrite);

    m_arr = new QByteArray( buffer.readAll() );

    m_shared->unlock();
    m_shared->detach();

    qDebug() << m_arr->data();
}

void myDataSource::writeToShared()
{
    if (m_shared->isAttached()) {
        m_shared->detach();
    }

    qDebug() << Q_FUNC_INFO;

    QFile f("/etc/hosts");
    if (!f.open(QIODevice::ReadOnly)) {
        qWarning("Couldn't open file.");
        return;
    }

    QByteArray buffer = f.readAll();
    int size = buffer.size();
    qDebug() << "size: " << size;
    if (!m_shared->create(size)) {
        qDebug() << Q_FUNC_INFO << "sharedmem create error: " << m_shared->errorString();
    }
    else {
        m_shared->lock();
        char *to = static_cast<char *>(m_shared->data());
        const char *from = buffer.constData();
        memcpy(to, from, qMin(size, m_shared->size()));
        qDebug() << "m_shared->size: " << m_shared->size();
        m_shared->unlock();
    }

}
