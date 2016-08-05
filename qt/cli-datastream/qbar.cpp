#include "qbar.h"

#include <QDebug>
#include <QFile>
#include <QDataStream>
#include <QMetaProperty>

#define FOOFILE  "/tmp/aaa.dat"

#include <iostream>
using namespace std;

QDataStream& operator<<(QDataStream& ds, const QBar& obj)
{
    int ii;
    ii = obj.metaObject()->indexOfProperty("title");
    ds << obj.metaObject()->property(ii).read(&obj);
    ii = obj.metaObject()->indexOfProperty("number");
    ds << obj.metaObject()->property(ii).read(&obj);

    return ds;
}
QDataStream& operator>>(QDataStream& ds, QBar& obj)
{
    int ii;
    QVariant var;
    ds >> var;
    ii = obj.metaObject()->indexOfProperty("title");
    obj.metaObject()->property(ii).write(&obj, var);
    ds >> var;
    ii = obj.metaObject()->indexOfProperty("number");
    obj.metaObject()->property(ii).write(&obj, var);

    return ds;
}


QBar::QBar()
{
}

// save object BarCtrl into file
void QBar::save()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(FOOFILE);
    if (!file.open(QIODevice::WriteOnly)) {
        qDebug() << "write file failed";
        return;
    }
    QDataStream out(&file);
    out << *this;
    file.close();
}

// load object BarCtrl from file
void QBar::load()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(FOOFILE);
    if (!file.open(QIODevice::ReadOnly)) {
        qDebug() << "read file failed";
        return;
    }
    QDataStream out(&file);
    out >> *this;
    file.close();
}

void QBar::show()
{
    //qDebug() << Q_FUNC_INFO;
    for (int i=this->metaObject()->propertyOffset(); i<this->metaObject()->propertyCount(); ++i) {
        if(this->metaObject()->property(i).isStored(this)) {
            qDebug() << QString::fromLatin1(this->metaObject()->property(i).name())
                    << ":" << this->metaObject()->property(i).read(this);
            //cout << ">>> " << this->metaObject()->property(i).name() << endl;
        }
    }
}

QString QBar::title() const
{
    return m_title;
}
void QBar::setTitle(const QString& s)
{
    m_title = s;
    emit titleChanged();
}
QString QBar::name() const
{
    return m_name;
}
void QBar::setName(const QString &s)
{
    m_name = s;
    emit nameChanged();
}
QString QBar::number() const
{
    return m_number;
}
void QBar::setNumber(const QString &s)
{
    m_number = s;
    emit numberChanged();
}
