/**
  * \file mymap.cpp
**/

#include "mymap.h"
#include <QDebug>
#include <QFile>

#define MYMAPFILE "/tmp/mymap.dat"

QDataStream& operator<<(QDataStream& ds, const MyMap& obj)
{
    ds << obj.mMap;
    return ds;
}

QDataStream& operator>>(QDataStream&ds, MyMap& obj)
{
    ds >> obj.mMap;
    return ds;
}

MyMap::MyMap()
{
    qDebug() << "mymap created";
}

void MyMap::init()
{
    mMap["mango"] = 53;
    mMap["watermelon"] = 97;
    mMap["chicken"] = 43;
}

void MyMap::dump()
{
    qDebug() << Q_FUNC_INFO;
    foreach (QString k, mMap.keys()) {
        qDebug() << QString("%1 => %2").arg(k).arg(mMap[k]);
    }
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
