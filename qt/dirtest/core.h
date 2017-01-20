#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include <QDebug>
#include <QCoreApplication>

#include "travelthread.h"

#ifdef __arm__
#define DEFAULT_START_PATH "/media/usb/storage"
#else
#define DEFAULT_START_PATH "/home/rasmus/Pictures"
#endif

class Core : public QObject
{
    Q_OBJECT

public:
    static Core* _instance;
    static Core* getInstance();

    void startTotalSize(const QString& startpath);
    void start(const QString& startpath);

signals:
    void sigQuit();

public slots:
    void sltWaitFinished();
    // void sltUsbDetected();
    // void sltIpodDetected();

protected:
    Core();

    void init_image_filter();
    void init_filter();
    qlonglong imageSpace(const QString &path);
    void travel_dir(const QString& path);
    void dumpList(const QStringList& list, const QString& fn);

private:
    TravelThread* mTravel = NULL;
};

#endif  // __CORE_H__
