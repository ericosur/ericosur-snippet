#ifndef __MSGQ_RX_H__
#define __MSGQ_RX_H__

#include <QObject>
#include <QThread>

#define MAX_SEND_SIZE           64
#define MESGQKEY_MESSAGE_TYPE   9
#define MESGQKEY_MONITOR        0x0880CAFE

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

class MsgRxThread : public QThread
{
    Q_OBJECT

public:
    MsgRxThread();
    void run();

signals:
    void sigReceived(const QString& s);

private:
};

#endif // __MSGQ_RX_H__
