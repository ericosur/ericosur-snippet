#ifndef __YOSEMESSAGEQUEUE_H__
#define __YOSEMESSAGEQUEUE_H__

#define MAX_SEND_SIZE           256
#define YOSE_MESSAGE_TYPE       9
#define MSGQ_FILE               "/tmp/msg.tmp"

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

#endif // __YOSEMESSAGEQUEUE_H__
