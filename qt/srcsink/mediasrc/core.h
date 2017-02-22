#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include <QStringList>
#include <QDebug>

#include "msgqrx.h"
#include "travelthread.h"
#include "fileitem.h"
#include "commonutil.h"
#include "idhash.h"

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
    void sigGetfolder();
    void sigQuitApp();

public slots:
    void sltMessageReceived(const QString& msg);
    void sltWaitFinished();
    void sltNext();
    void sltStart();
    void sltGetfolder();
    void sltTravelFinished();

protected:
    Core();

    void SendItemToShm(ItemType it);
    FileItem* fetchOneItem();
    FileItem* fetchOneFolderItem();
    void check_shm();

private:
    MsgRxThread* msgrx = NULL;
    TravelThread* travel = NULL;
    QStringList filelist;
    QStringList folderlist;
    FileItem* mBuffer = NULL;
};

#endif  // __CORE_H__
