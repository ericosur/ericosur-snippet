#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include <QStringList>
#include <QDebug>

#include "msgqrx.h"
#include "travelthread.h"
#include "fileitem.h"
#include "commonutil.h"

typedef unsigned char byte;

class Core : public QObject
{
    Q_OBJECT

public:
    static Core* _instance;
    static Core* getInstance();

    void test();
    void simple_test_shm_read_write();
    void startTravel();

signals:
    void sigNext();
    void sigStart();
    void sigQuitApp();

public slots:
    void sltMessageReceived(const QString& msg);
    void sltWaitFinished();
    void sltNext();
    void sltStart();
    void sltTravelFinished();

protected:
    Core();

    FileItem* fetchOneItem();

private:
    MsgRxThread* msgrx = NULL;
    TravelThread* travel = NULL;
    QStringList filelist;
};

#endif  // __CORE_H__
