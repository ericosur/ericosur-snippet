#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <time.h>

#include "YoseMessageQueue.h"

char *getxtsj()
{
    time_t  tv;
    struct  tm   *tmp;
    static char buf[20];
    tv = time( 0 );
    tmp = localtime(&tv);
    sprintf(buf, "%02d:%02d:%02d", tmp->tm_hour, tmp->tm_min,tmp->tm_sec);
    return buf;
}

int sendMyMessage(int msqid, struct mymsgbuf* buf, const char* str)
{
    int sendlength;
    int flag;

    buf->mtype = YOSE_MESSAGE_TYPE;
    sendlength = sizeof(struct mymsgbuf) - sizeof(long);
    strncpy(buf->mtext, str, MAX_SEND_SIZE - 32);
    flag = msgsnd( msqid, buf, sendlength, 0 );
    if ( flag < 0 ) {
        perror("msgsnd: send message error");
        return -1;
    }
    printf("sendMyMessage: %s\n", buf->mtext);
    return 0;
}

int main(int argc, char **argv)
{
    int msqid;
    struct mymsgbuf buf;
    //int recvlength;
    int key = MESGQKEY;
    //const int MAXREPEAT = 5;

    //key = ftok(MSGQ_FILE, 'm' );
    if ( key < 0 ) {
        perror("msgsnd: ftok key error");
        return -1;
    } else {
        printf("key: %d\n", key);
    }

    msqid = msgget( key, 0660 | IPC_CREAT );
    if ( msqid < 0 ) {
        perror("msgsnd: create message queue error");
        return -1;
    } else {
        printf("msgsnd: msqid: %d\n", msqid);
    }

    sendMyMessage(msqid, &buf, "home");
    sleep(1);
    sendMyMessage(msqid, &buf, "pause");
    sleep(1);
    sendMyMessage(msqid, &buf, "stop");
    sleep(1);
    sendMyMessage(msqid, &buf, "file:///etc/image_version");
    sleep(1);
    sendMyMessage(msqid, &buf, "helloworld from sendtest");
    sleep(1);
    sendMyMessage(msqid, &buf, __DATE__ __TIME__);

    if ( system("ipcs -q") )
        ;

    return 0;
}
