#include "msgqsend.h"
#include <stdio.h>
#include <string.h>

bool _debug = false;

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
        return msqid;
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
