#include <stdio.h>
#include <string.h>
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

int main(int argc, char **argv)
{
    int msqid;
    struct mymsgbuf buf;
    int flag;
    int sendlength, recvlength;
    int key = MESGQKEY;
    const int MAXREPEAT = 5;
    int i;

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

    buf.mtype = YOSE_MESSAGE_TYPE;

    for (i=0; i<MAXREPEAT; i++) {
        //strcpy(buf.time, getxtsj()) ;
        //strcpy(buf.mtext, "happy new year!") ;
        sprintf(buf.mtext, "[%d] %s", i, getxtsj());
        sendlength = sizeof(struct mymsgbuf) - sizeof(long);
        flag = msgsnd( msqid, &buf, sendlength, 0 );
        if ( flag < 0 ) {
            perror("msgsnd: send message error");
            return -1;
        }
        printf("send: %s\n", buf.mtext);
        sleep(1);
    }

    system("ipcs -q");
    return 0;
}
