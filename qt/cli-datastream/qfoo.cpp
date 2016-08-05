#include "qfoo.h"
#include <QDebug>
#include <QString>

QFoo::QFoo()
{

}

void QFoo::sltTitle()
{
    qDebug() << Q_FUNC_INFO;
}

void QFoo::sltName()
{
    qDebug() << Q_FUNC_INFO;
}

void QFoo::sltNumber()
{
    qDebug() << Q_FUNC_INFO;
}
