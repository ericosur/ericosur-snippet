/// file: foothread.cpp

#include "foothread.h"

#include <QDebug>

FooThread::FooThread()
{
}

void FooThread::run()
{
    while (1) {
        // do nothing
    }
}

void FooThread::onClose()
{
    qDebug() << "FooThread::onClose()";
    this->terminate();
}
