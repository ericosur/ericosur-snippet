/**
  * \file mymap.cpp
**/

#include "mymap.h"
#include <QDebug>
#include <QFile>

#define MYMAPFILE "/tmp/mymap.dat"

QDataStream& operator<<(QDataStream& ds, const MyMap& obj)
{
    ds << obj.scannedDevices;
    return ds;
}

QDataStream& operator>>(QDataStream&ds, MyMap& obj)
{
    ds >> obj.scannedDevices;
    return ds;
}

MyMap::MyMap()
{
    qDebug() << "mymap created";
}

void MyMap::init()
{
    int i = 0;
    //for (int i=0; i < LENGTH_LIST; ++i) {
        QVariantMap device;
        QString name = "iPhone " + QString::number(i);
        device["name"]      = QVariant(name);
        device["mac"]       = QVariant(i);
        device["paired"]    = QVariant(false);
        device["connected"] = QVariant(false);
        device["connecting"]= QVariant(false);
        device["showInfo"]  = QVariant(false);
        scannedDevices.append(device);
    //}
}

void MyMap::dump()
{
    qDebug() << Q_FUNC_INFO;
    int i = 0;
    //for (int i = 0; i < LENGTH_LIST; ++i) {
        QVariantMap map = scannedDevices[i];
        qDebug() << "size:" << map.size();
        if (map.size() <= 0) {
            qWarning() << "map size zero";
            return;
        }
        foreach (QString k, map.keys()) {
            qDebug() << QString("%1 => %2").arg(k).arg(map[k].toString());
        }
        // for (QVariantMap::const_iterator iter = map.begin(); iter != map.end(); ++iter) {
        //   qDebug() << iter.key() << iter.value();
        // }
    //}
}

// save object BarCtrl into file
void MyMap::save()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(MYMAPFILE);
    if (!file.open(QIODevice::WriteOnly)) {
        qDebug() << "write file failed";
        return;
    }
    QDataStream out(&file);
    out << *this;
    file.close();
}

// load object BarCtrl from file
void MyMap::load()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(MYMAPFILE);
    if (!file.open(QIODevice::ReadOnly)) {
        qDebug() << "read file failed";
        return;
    }
    QDataStream out(&file);
    out >> *this;
    file.close();
}
