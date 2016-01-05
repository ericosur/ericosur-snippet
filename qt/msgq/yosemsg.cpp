#include <QDebug>

#include <sys/types.h>
#include <sys/msg.h>
#include <sys/ipc.h>

#include "YoseMessageQueue.h"
#include "yosemsg.h"

YoseMsg::YoseMsg() :
    m_count(0)
{

}

void YoseMsg::run()
{
    qDebug() << "hello world";
    key_t key = MESGQKEY;
    int msgqueue_id;
    struct mymsgbuf qbuf;

    //key = ftok(MSGQ_FILE, 'm');
    int type = YOSE_MESSAGE_TYPE;
    if((msgqueue_id = msgget(key, IPC_CREAT|0660)) == -1) {
        perror("msgsnd: msgget");
        return; // error here
    }
    qDebug() << "mythread: key: " << key << " msgqueue_id: " << msgqueue_id;
    while ( true ) {
        qbuf.mtype = YOSE_MESSAGE_TYPE;
        msgrcv(msgqueue_id, (struct mymsgbuf *)&qbuf, MAX_SEND_SIZE, type, 0);
        //printf("%i: Type: %ld Text: %s\n",count, qbuf.mtype, qbuf.mtext);
        qDebug() << "msgqueue: " << " type: " << qbuf.mtype << " text: " << qbuf.mtext;
        emit sigReceived(QString(qbuf.mtext));
    }
}

void YoseMsg::sltPrint(const QString& s)
{
    emit sigReceived(s);
}
