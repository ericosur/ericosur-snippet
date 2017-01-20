#ifndef __POLL_THREAD_H__
#define __POLL_THREAD_H__

#include <QObject>
#include <QThread>

#ifdef USE_YOSETARGET
#include <libhu_ipc.h>
#include <libhu_status.h>
#else
typedef enum _devtype {
    DEV_USB,
    DEV_IPOD
} DevType;
#define status_get_dev(x)   (0)
#endif  // USE_YOSETARGET

class PollThread : public QThread
{
    Q_OBJECT

public:
    PollThread();
    void run();

signals:
    void sigUsbDectected();
    void sigIpodDectected();

private:

};

#endif // __POLL_THREAD_H__
