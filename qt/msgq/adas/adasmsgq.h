/// file: adasmsgq.h
// api for definition msgq between IVI and ADAS

#ifndef __ADASMSGQ_H__
#define __ADASMSGQ_H__

#include <unistd.h>  // getopt
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_SEND_SIZE           256
#define YOSE_MESSAGE_TYPE       9

#define MSGQKEY_Z2Y        0x0ADA5000

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

int send_msgq(int key, int type, const char* str);
void recv_msgq(int key, int type);


#endif  //__ADASMSGQ_H__
