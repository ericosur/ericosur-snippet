#ifndef _CORE_H__
#define _CORE_H__

#include <QObject>
#include <QString>
#include <QDebug>

#include "demo_capture.h"

class Core : public QObject
{
    Q_OBJECT

public:
    Core() {}
    Q_INVOKABLE QString demo();

public slots:
    void cppSloot(const QString &msg)  {
        qDebug() << "called the C++ slot with message:" << msg;
    }
};


#endif
