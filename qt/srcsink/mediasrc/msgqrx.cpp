#include "msgqrx.h"
#include <QDebug>
#include <sys/types.h>
#include <sys/msg.h>
#include <sys/ipc.h>

MsgRxThread::MsgRxThread()
{
    qDebug() << Q_FUNC_INFO << "created...";
}

void MsgRxThread::run()
{
    qDebug() << Q_FUNC_INFO << "running...";
    key_t key = MESGQKEY_MONITOR;
    int msgqueue_id;
    struct mymsgbuf qbuf;

    if((msgqueue_id = msgget(key, IPC_CREAT|0660)) == -1) {
        perror("MsgRxThread: msgget");
        return; // error here
    }
    qDebug() << "MsgRxThread: key: " << QString("0x") + QString::number(key, 16).toUpper()
             << " msgqueue_id: " << msgqueue_id;
    while ( true ) {
        qbuf.mtype = MESGQKEY_MESSAGE_TYPE;
        msgrcv(msgqueue_id, (struct mymsgbuf *)&qbuf, MAX_SEND_SIZE, MESGQKEY_MESSAGE_TYPE, 0);
        //printf("%i: Type: %ld Text: %s\n",count, qbuf.mtype, qbuf.mtext);
        qDebug() << "msgrcv: " << " type: " << qbuf.mtype << " text: " << qbuf.mtext;
        emit sigReceived(QString(qbuf.mtext));
    }
}
