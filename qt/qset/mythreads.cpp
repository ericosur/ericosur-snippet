#include "mythreads.h"

#include <QObject>
#include <QThread>
#include <QString>
#include <QDebug>
#include <QCryptographicHash>

MyEmptyThread::MyEmptyThread()
    : m_result("")
    , m_count(0)
{
}

QString MyEmptyThread::doHardWork(const QString& s, int method)
{
    QByteArray data;
    //const int MAX_HASH_REPEAT = 100;
    const int MAX_HASH_REPEAT_METHOD_1 = 55;
    const int MAX_HASH_REPEAT_METHOD_2 = 80;
    const int MAX_HASH_REPEAT_METHOD_3 = 60;

    //qDebug() << "doHardWork()" << s << "," << method;
    data.append(s);
    switch (method) {
    case 0:
    {
        for (int i=0; i<MAX_HASH_REPEAT_METHOD_1; ++i) {
            data.append(qrand());
            for (int j=0; j<MAX_HASH_REPEAT_METHOD_1; ++j) {
                data.append(qrand());
                data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
                for (int k=0; k<MAX_HASH_REPEAT_METHOD_1; ++k) {
                    data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
                    data.append( QCryptographicHash::hash(QByteArray(QString::number(qrand(),16).toUtf8()),
                                                          QCryptographicHash::Sha256) );
                    data.append(qrand());
                }
            }
            data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        }
        //qDebug() << "sha256:" << data.toHex().data();
        break;
    }
    case 1:
    {
        for (int i=0; i<MAX_HASH_REPEAT_METHOD_2; ++i) {
            data.append(qrand());
            for (int j=0; j<MAX_HASH_REPEAT_METHOD_2; ++j) {
                data.append(qrand());
                data = QCryptographicHash::hash(data, QCryptographicHash::Sha384);
                for (int k=0; k<MAX_HASH_REPEAT_METHOD_2; ++k) {
                    data.append(qrand());
                    data = QCryptographicHash::hash(data, QCryptographicHash::Sha384);
                }
            }
            data = QCryptographicHash::hash(data, QCryptographicHash::Sha384);
        }
        //qDebug() << "sha384:" << data.toHex().data();
        break;
    }
    case 2:
    {
        for (int i=0; i<MAX_HASH_REPEAT_METHOD_3; ++i) {
            data.append(qrand());
            for (int j=0; j<MAX_HASH_REPEAT_METHOD_3; ++j) {
                data.append(qrand());
                data = QCryptographicHash::hash(data, QCryptographicHash::Sha3_512);
                for (int k=0; k<MAX_HASH_REPEAT_METHOD_3; ++k) {
                    data.append(qrand());
                    data.append( QCryptographicHash::hash(data, QCryptographicHash::Sha3_512) );
                    data = QCryptographicHash::hash(data, QCryptographicHash::Sha3_512);
                }
            }
            data = QCryptographicHash::hash(data, QCryptographicHash::Sha3_512);
        }
        //qDebug() << "sha3_512:" << data.toHex().data();
        break;
    }
    default:
        qDebug() << "no such method...";
        break;
    }

    return data.toHex().data();
}

/////////////////////////////////////////////////////////////////////
///
///
/// \brief ThreadFoo::ThreadFoo
///
///
/////////////////////////////////////////////////////////////////////
ThreadFoo::ThreadFoo(int method, const QString& str) :
    MyEmptyThread(),
    m_method(method),
    m_str(str)
{
}

void ThreadFoo::run()
{
    const int MAX_TEST_REPEAT = 100;

    for (int i = 0; i < MAX_TEST_REPEAT; ++i) {
        ThreadFoo::doHardWork(m_str, m_method);
    }
}
