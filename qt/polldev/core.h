#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include "pollthread.h"

class Core : public QObject
{
    Q_OBJECT

public:
    static Core* _instance;
    static Core* getInstance();

    void start();
    void launchIpod();
    void launchMedia();

signals:
    void sigQuit();

public slots:
    void sltWaitFinished();
    void sltUsbDetected();
    void sltIpodDetected();

protected:
    Core();

private:
    PollThread* poll = NULL;
};

#endif  // __CORE_H__
