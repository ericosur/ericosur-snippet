/*
   Copyright 2013  Olivier Goffart <ogoffart@woboq.com>
   http://woboq.com/blog/qmap_qhash_benchmark.html
   //http://woboq.com/blog/qmap_qhash_benchmark/benchmark.cc.html
*/

#include <stdio.h>

#include <QtCore>
#include <QMap>
#include <QHash>
#include <QString>
#include <QCryptographicHash>

// http://pastebin.ca/2315791

#if 0
//#define MYCONTAINER QMap
//#define MYCONTAINER_NAME "QMap"
#else
//#define MYCONTAINER QHash
//#define MYCONTAINER_NAME "QHash"
#endif

#define MYCONTAINER QCache
#define MYCONTAINER_NAME "QCache"

QString sha1(const QString& str)
{
    QCryptographicHash hh( QCryptographicHash::Sha1 );
    hh.addData(str.toStdString().c_str(), str.length());
    QString sHash = hh.result().toHex().data();
    return sHash;
}

void test(quint64 num) {
    qDebug() << "num" << num;
    // creates an array of random keys
    QVector<QString> strs(num);
    for (quint64 i=0; i < num; ++i) {
        QByteArray data;
        data.append(qrand());
        data = QCryptographicHash::hash(data, QCryptographicHash::Sha1);
        for (int j = 0; j < 9; j++)
            data.append(QCryptographicHash::hash(data, QCryptographicHash::Sha1));
        strs[i] = data;
        //strs.insert(i, data);
    }

    MYCONTAINER<QString, QString> c;
    c.setMaxCost(num*8);
    for (uint i = 0; i < num; ++i) {
        QString &k = strs[i];
        //c[k] = QString::number(i);
        QString *ps = new QString(QString::number(i));
        c.insert(k, ps);
    }
    qDebug() << "cache size: " << c.size();
    qDebug() << "total cost: " << c.totalCost();

    quint64 it = 0;
    const QString *arr = strs.constData();

    QElapsedTimer t;
    t.start();

    while (t.elapsed() < 1000) {
        const QString &k = arr[(++it)*797%num];
        c[k]; // perform a lookup
    }

    it = it/1000;
    printf("%s,%s,%s\n", MYCONTAINER_NAME,
           QString::number(num).toStdString().c_str(),
           QString::number(it).toStdString().c_str());
}


int main()
{
    quint64 n_size = 15;

    for (quint64 n=1,i=0; i<n_size; n=n*2) {
        test(n);
        i++;
    }

    return 0;
}
