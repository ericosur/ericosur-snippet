#ifndef __MSGQ_SEND_H__
#define __MSGQ_SEND_H__

#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_SEND_SIZE           64
#define MESGQKEY_MESSAGE_TYPE   9
#define MESGQKEY_MONITOR        0x0880CAFE

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

int send_msgq(int key, int type, const char* str);


#endif	// __MSGQ_SEND_H__
