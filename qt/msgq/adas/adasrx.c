/// file: adastx.c

#include <stdio.h>

#include "adasmsgq.h"


int main()
{
    printf("adasrun forever, press ctrl-C to quit...\n");

    recv_msgq(MSGQKEY_Z2Y, YOSE_MESSAGE_TYPE);

    return 0;
}
