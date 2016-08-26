#include "retry.h"
#include <unistd.h>  /* getopt */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <QDebug>

#define MAX_VALID_KEY           ((key_t)0x7FFFFFFF)
#define MAX_BUFFER_SIZE         ((uint)(1024+sizeof(long)))
#define DEFAULT_INVALID_KEY     ((key_t)0xDEADBEEF)
#define DEFAULT_MESSAGE_TYPE    9
#define DEFAULT_SEND_SIZE       64U
#define MAX_ARGV_SIZE           DEFAULT_SEND_SIZE
#define MIN_SEND_SIZE           16U

/// default wait for 100ms
#define DEFAULT_WAIT_DURATION	500
/// default max retry times
#define DEFAULT_MAX_RETRY		20

#define MYMIN(x, y) ((x > y) ? y : x)

struct myoptions {
    key_t msgq_key;
    long msgq_type;
    uint msgq_size;
};


RetryThread::RetryThread()
{
}

void RetryThread::run()
{
    struct myoptions opt = {
    	MAX_VALID_KEY,
        DEFAULT_MESSAGE_TYPE,
        DEFAULT_SEND_SIZE
    };

	while (m_shouldrun) {
		qDebug() << "try something:" << m_retrycount;
		send_msgq(&opt, "hello");
		m_retrycount ++;
		if (m_retrycount > DEFAULT_MAX_RETRY) {
			qDebug() << "quit because max retied...";
			m_shouldrun = false;
			break;
		}
		QThread::msleep(DEFAULT_WAIT_DURATION);
	}
}

void RetryThread::sltNotifyStop()
{
	m_shouldrun = false;
	qDebug() << "notify stop...";
}

int RetryThread::send_msgq(struct myoptions* opt, const char* str)
{
    int msqid;
    unsigned char buffer[MAX_BUFFER_SIZE];

    printf("send_msgq(): str: %s\n", str);
    // only open a listening (previously created) message queue
    //msqid = msgget( opt->key, 0660 | IPC_EXCEL );
    msqid = msgget( opt->msgq_key, 0660 | IPC_EXCL );
    if ( msqid < 0 ) {
        qDebug() << "msgget: get message queue error";
        return -1;
    } else {
        //printf("msgget: msqid: %d\n", msqid);
    }

    if ((unsigned long)opt->msgq_size > MAX_BUFFER_SIZE - sizeof(long)) {
        opt->msgq_size = MAX_BUFFER_SIZE - sizeof(long);
        fprintf(stderr, "assigned msgq_size is too large, "
            "modified to %d\n", opt->msgq_size);
    }
    if (opt->msgq_size < MIN_SEND_SIZE) {
        opt->msgq_size = MIN_SEND_SIZE;
        fprintf(stderr, "assigned msgq_size is too small, "
            "modified to %d\n", opt->msgq_size);
    }

    //dump_opt(opt);

    memset(buffer, 0, MAX_BUFFER_SIZE);
    memcpy(buffer, &opt->msgq_type, sizeof(long));
    if (strlen(str)+1 > (unsigned long)opt->msgq_size) {
        fprintf(stderr, "strlen > msgq_size, msg not sent\n");
        return -1;
    }
    memcpy(buffer+sizeof(long), str, strlen(str)+1);
    //dump(buffer, opt->msgq_size+sizeof(long));
    if ( msgsnd(msqid, &buffer, opt->msgq_size, 0) < 0 ) {
        qDebug() << "msgsnd: send message error";
        return -1;
    }
    return 0;
}
