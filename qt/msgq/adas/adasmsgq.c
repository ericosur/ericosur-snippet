/// file: adasmsgq.c

#include "adasmsgq.h"

int _debug = 0;

int send_msgq(int key, int type, const char* str)
{
    int msqid;
    struct mymsgbuf buf;
    int sendlength;

    if (_debug)
        printf("send_msgq(): key: 0x%08X\ttype: %d\nstr: %s\n", key, type, str);

    // will create msgq if run first
    msqid = msgget( key, 0660 | IPC_CREAT );
    //msqid = msgget( key, 0660 | IPC_EXCL );
    if ( msqid < 0 ) {
        perror("send_msgq: create message queue error");
        return -1;
    } else {
        if (_debug)
            printf("send_msgq: msqid: %d\n", msqid);
    }

    memset(&buf, 0, sizeof(struct mymsgbuf));
    buf.mtype = type;
    sendlength = sizeof(struct mymsgbuf) - sizeof(long);
    strncpy(buf.mtext, str, MAX_SEND_SIZE - sizeof(long));

    if ( msgsnd(msqid, &buf, sendlength, 0) < 0 ) {
        perror("send_msgq: send message error");
        return -1;
    }
    //printf("sendMyMessage: %s\n", buf.mtext);
    return 0;
}

// just a test function to recv, need put it into thread
void recv_msgq(int key, int type)
{
    if (_debug)
        printf("recv_msgq(): key:0x%08X\ntype: %d\n", key, type);

    int msgqueue_id;
    struct mymsgbuf qbuf;

    //key = ftok(MSGQ_FILE, 'm');
    if((msgqueue_id = msgget(key, IPC_CREAT|0660)) == -1) {
        perror("recv_msgq: msgget");
        return; // error here
    }
    if (_debug)
        printf("msgqueue_id: %d\n", msgqueue_id);
    for ( ; ; ) {
        qbuf.mtype = YOSE_MESSAGE_TYPE;
        msgrcv(msgqueue_id, (struct mymsgbuf *)&qbuf, MAX_SEND_SIZE, type, 0);
        printf("Type: %ld Text: %s\n", qbuf.mtype, qbuf.mtext);
    }
}
