/// file: adastx.c

#include <stdio.h>
#include <time.h>

#include "adasmsgq.h"

// send to message queue within 1 second
// need RX to fetch messages, or
// message queue will be blocked
int test()
{
    const int STRLEN = 60;
    const int TIME_DIFF = 1;

    int i = 0;
    char str[STRLEN];

    unsigned int begin_time = (unsigned)time(NULL);
    unsigned int curr_time;

    while (1) {
        curr_time = (unsigned)time(NULL);
        sprintf(str, "%u: %d", (unsigned)time(NULL), i);
        send_msgq(MSGQKEY_Z2Y, YOSE_MESSAGE_TYPE, str);
        if (curr_time - begin_time >= TIME_DIFF)
            break;
        i++;
    }

    fprintf(stdout, "last count: %d\n", i);
    return 0;
}

int main()
{
    test();
    return 0;
}
