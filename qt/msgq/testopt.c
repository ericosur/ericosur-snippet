#include <unistd.h>  /* getopt */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_SEND_SIZE           1024
#define YOSE_MESSAGE_TYPE       9
#define DEFAULT_INVALID_KEY     0xDEADBEEF

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

int send_msgq(int key, const char* str)
{
    int msqid;
    struct mymsgbuf buf;
    int sendlength;

    printf("key: 0x%08X\nstr: %s\n", key, str);
    msqid = msgget( key, 0660 | IPC_CREAT );
    if ( msqid < 0 ) {
        perror("msgsnd: create message queue error");
        return -1;
    } else {
        printf("msgsnd: msqid: %d\n", msqid);
    }

    buf.mtype = YOSE_MESSAGE_TYPE;
    sendlength = sizeof(struct mymsgbuf) - sizeof(long);
    strncpy(buf.mtext, str, MAX_SEND_SIZE - 32);

    if ( msgsnd(msqid, &buf, sendlength, 0) < 0 ) {
        perror("msgsnd: send message error");
        return -1;
    }
    printf("sendMyMessage: %s\n", buf.mtext);
    return 0;
}

int main(int argc, char **argv)
{
    int cmd_opt = 0;
    int msgq_key = DEFAULT_INVALID_KEY;
    int tmp_key = 0;
    int res = 0;
    int r;

    //fprintf(stderr, "argc: %d\n", argc);
    while(1) {
        //fprintf(stderr, "process index: %d\n", optind);
        cmd_opt = getopt(argc, argv, "hk:vycq");

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
                printf("-h  help message\n"
                    "-k  assign key\n"
                    "-v  videocontrol to yoseui key\n"
                    "-y  yoseui to videocontrol key\n"
                    "-c  yoseui to clock key\n"
                    );
                break;
            /* Single arg */
            case 'k':
                //fprintf(stderr, "option arg: %s\n", optarg);
                tmp_key = strtol(optarg, NULL, 16);
                //printf("tmp_key = 0x%08X\n", tmp_key);
                if (tmp_key > 0) {
                    msgq_key = tmp_key;
                }
                break;

            case 'v':
                msgq_key = 0x600DFEA6;
                break;

            case 'y':
                msgq_key = 0x600DCAFE;
                break;

            case 'c':
                msgq_key = 0x00C0FFEE;
                break;

            case 'q':
                r = system("ipcs -q");
                (void)r;
                exit(1);

            /* Error handle: Mainly missing arg or illegal option */
            case '?':
                fprintf(stderr, "Illegal option:-%c\n", isprint(optopt)?optopt:'#');
                break;
            default:
                fprintf(stderr, "Not supported option\n");
                exit(-1);
        }
    }

    char msg_str[96];
    /* Do we have args? */
    if (argc > optind) {
        int i = 0;
        for (i = optind; i < argc; i++) {
            //fprintf(stderr, "argv[%d] = %s\n", i, argv[i]);
            strcpy(msg_str, argv[i]);
            break;
        }
    }

    if (msgq_key != DEFAULT_INVALID_KEY) {
        res = send_msgq(msgq_key, msg_str);
    }

    return res;
}
