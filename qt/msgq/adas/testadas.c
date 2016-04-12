#include <unistd.h>  /* getopt */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <ctype.h>

#include "adasmsgq.h"

void helpMessage()
{
    fprintf(stderr,
            "testopt [options] <message>\n"
            "-h  help message\n"
            "-k  assign key (default: 0x%08X\n"
            "-q  system message queue status\n"
            "-t  assign type (default:%d)\n",
            MSGQKEY_Z2Y, YOSE_MESSAGE_TYPE);
}

int main(int argc, char **argv)
{
    int cmd_opt = 0;
    int msgq_key = MSGQKEY_Z2Y;
    int msgq_type = YOSE_MESSAGE_TYPE;  // default value
    int tmp_key = 0;
    int tmp_type = 0;
    int res = 0;
    int r;

    //fprintf(stderr, "argc: %d\n", argc);
    while(1) {
        //fprintf(stderr, "process index: %d\n", optind);
        cmd_opt = getopt(argc, argv, "hk:t:q");

        /* End condition always first */
        if (cmd_opt == -1) {
            break;
        }

        /* Print option when it is valid */
        if (cmd_opt != '?') {
            //fprintf(stderr, "option:-%c\n", cmd_opt);
        }

        /* Lets parse */
        switch (cmd_opt) {
            case 'h':
                helpMessage();
                exit(2);
                break;
            /* Single arg */
            case 'k':
                //fprintf(stderr, "option arg: %s\n", optarg);
                tmp_key = strtol(optarg, NULL, 16);
                fprintf(stderr, "assign key = 0x%08X\n", tmp_key);
                if (tmp_key > 0) {
                    msgq_key = tmp_key;
                }
                break;
            case 't':
                tmp_type = strtol(optarg, NULL, 10);
                fprintf(stderr, "assign type = %d\n", tmp_type);
                msgq_type = tmp_type;

            case 'q':
                r = system("ipcs -q");
                (void)r;
                exit(1);

            /* Error handle: Mainly missing arg or illegal option */
            case '?':
                fprintf(stderr, "Illegal option:-%c\n", isprint(optopt)?optopt:'#');
                exit(3);
                break;
            default:
                fprintf(stderr, "Not supported option\n");
                exit(4);
                break;
        }
    }

    char msg_str[MAX_SEND_SIZE];
    /* Do we have args? */
    if (argc > optind) {
        int i = 0;
        for (i = optind; i < argc; i++) {
            //fprintf(stderr, "argv[%d] = %s\n", i, argv[i]);
            strcpy(msg_str, argv[i]);
            break;
        }
    }
    //printf("msgq_key: %08x\n", msgq_key);
    //if (msgq_key != DEFAULT_INVALID_KEY) {
        res = send_msgq(msgq_key, msgq_type, msg_str);
    //}

    return res;
}
