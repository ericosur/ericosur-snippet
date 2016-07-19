#ifndef __MSGQDEF_H__
#define __MSGQDEF_H__

#define MAX_SEND_SIZE           64
#define YOSE_MESSAGE_TYPE       9
#define MESGQKEY				0x0DEFC0DE

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

#endif // __MSGQDEF_H__
