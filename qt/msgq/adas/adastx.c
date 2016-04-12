/// file: adastx.c

#include <stdio.h>
#include <time.h>

#include "adasmsgq.h"


void show_time()
{
    fprintf(stdout, "time: %u\n", (unsigned)time(NULL));
}
// send to message queue within 1 second
// need RX to fetch messages, or
// message queue will be blocked
int test()
{
    const int STRLEN = 60;
    //const int TIME_DIFF = 1;
    const int REPEAT_COUNT = 60000;

    int i;
    char str[STRLEN];

    show_time();
    for (i = 0; i < REPEAT_COUNT; i++) {
        sprintf(str, "%u: %d", (unsigned)time(NULL), i);
        send_msgq(MSGQKEY_Z2Y, YOSE_MESSAGE_TYPE, str);
    }

    show_time();
    return 0;
}

int main()
{
    test();
    return 0;
}
