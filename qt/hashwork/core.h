#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include "pollthread.h"
#include "worker.h"

class Core : public QObject
{
    Q_OBJECT

public:
    static Core* _instance;
    static Core* getInstance();

    void start();

signals:
    void sigQuit();
    void sigWork();

public slots:
    void sltWaitFinished();

protected:
    Core();

private:
    PollThread* poll = NULL;
    Worker* worker = NULL;
};

#endif  // __CORE_H__
