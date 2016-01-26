#include "mythreads.h"

#include <QObject>
#include <QThread>
#include <QString>
#include <QDebug>
#include <QCryptographicHash>

//const int MAX_TEST_REPEAT = 750;
//const int MAX_HASH_REPEAT = 20;

const int MAX_TEST_REPEAT = 25;
const int MAX_HASH_REPEAT = 200;

QString sha256sum(const QString s)
{
    QByteArray data;

    data.append(s);
    for (int i=0; i<MAX_HASH_REPEAT; ++i) {
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        for (int j=0; j<MAX_HASH_REPEAT*2; ++j) {
            data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        }
    }
    return data.toHex().data();
}

QString sha384sum(const QString s)
{
    QByteArray data;

    data.append(s);
    for (int i=0; i<MAX_HASH_REPEAT; ++i) {
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha256);
        for (int j=0; j<MAX_HASH_REPEAT; ++j) {
            data = QCryptographicHash::hash(data, QCryptographicHash::Sha384);
        }
    }
    return data.toHex().data();
}


MyEmptyThread::MyEmptyThread(QSettings *set)
    : m_setting(set)
    , m_result("")
    , m_count(0)
{
}

/////////////////////////////////////////////////////////////////////
///
///
/// \brief ThreadFoo::ThreadFoo
///
///
/////////////////////////////////////////////////////////////////////
ThreadFoo::ThreadFoo(QSettings* set) :
    MyEmptyThread(set)
{
}

void ThreadFoo::run()
{
    //m_setting->beginGroup("foo");
    qsrand(qrand());
    for (int i = 0; i < MAX_TEST_REPEAT; i++) {
        m_setting->setValue("foo/index", i);
        m_count = i;
        int rnd = qrand();
        m_setting->setValue(QString("foo/seed") + QString::number(i), rnd);
        e.start();
        m_result = sha256sum(QString::number(rnd));
        m_setting->setValue(QString("foo/sum") + QString::number(i), m_result);
        m_setting->setValue(QString("foo/epoch") + QString::number(i), e.elapsed());
    }

    //m_setting->endGroup();
}

/////////////////////////////////////////////////////////////////////
///
///
/// \brief ThreadBar::ThreadBar
///
///
/////////////////////////////////////////////////////////////////////
ThreadBar::ThreadBar(QSettings* set) :
    MyEmptyThread(set)
{
}

void ThreadBar::run()
{
    QString res;
    QString key_index = "bar/index";
    QString key_initnum = "bar/initnum";
    QString key_shasum = "bar/sha384sum";

    for (int i = 0; i < MAX_TEST_REPEAT; i++) {
        m_setting->setValue(key_index, i);
        int rnd = qrand();
        m_setting->setValue(key_initnum + QString::number(i), rnd);
        e.start();
        res = sha384sum(QString::number(rnd));
        m_setting->setValue(QString("bar/elapse")+QString::number(i), e.elapsed());
        m_setting->setValue(key_shasum + QString::number(i), res);
    }
}
