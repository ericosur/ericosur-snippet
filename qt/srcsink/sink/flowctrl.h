#ifndef __FLOW_CTRL_H__
#define __FLOW_CTRL_H__

#include <QObject>
#include <QString>
#include <QDebug>

#include "msgqsend.h"
#include "fileitem.h"
#include "readthread.h"

#define MAX_ITEM    (10)

class FlowControl : public QObject
{
    Q_OBJECT

public:
    static FlowControl* getInstance();

    void start();

signals:
    void sigQuitApp();

public slots:
    void sltReadFinished();

protected:
    static FlowControl* _instance;
    FlowControl();

    void check_shm();

private:
    ReadThread* readthead = NULL;
};

#endif // __FLOW_CTRL_H__
