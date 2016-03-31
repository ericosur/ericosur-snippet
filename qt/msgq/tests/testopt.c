#include <unistd.h>  /* getopt */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_SEND_SIZE           64
#define YOSE_MESSAGE_TYPE       9
#define DEFAULT_INVALID_KEY     0xDEADBEEF
#define MSGQKEY_V2Y        0x600DFEA6
#define MSGQKEY_Y2V        0x600DCAFE
#define MSGQKEY_C2Y        0x00C0FFEE

struct mymsgbuf {
    long mtype;
    char mtext[MAX_SEND_SIZE];
};

int send_msgq(int key, int type, const char* str)
{
    int msqid;
    struct mymsgbuf buf;
    int sendlength;

    printf("send_msgq(): key: 0x%08X\ntype: %d\nstr: %s\n", key, type, str);
    msqid = msgget( key, 0660 | IPC_CREAT );
    //msqid = msgget( key, 0660 | IPC_EXCL );
    if ( msqid < 0 ) {
        perror("msgsnd: create message queue error");
        return -1;
    } else {
        printf("msgsnd: msqid: %d\n", msqid);
    }

    buf.mtype = type;
    sendlength = sizeof(struct mymsgbuf) - sizeof(long);
    strncpy(buf.mtext, str, MAX_SEND_SIZE - 32);

    if ( msgsnd(msqid, &buf, sendlength, 0) < 0 ) {
        perror("msgsnd: send message error");
        return -1;
    }
    //printf("sendMyMessage: %s\n", buf.mtext);
    return 0;
}

void helpMessage()
{
    fprintf(stderr,
            "testopt [options] <message>\n"
            "-h  help message\n"
            "-k  assign key\n"
            "-t  assign type (default:9)\n"
            "-v  videocontrol to yoseui key (%08X)\n"
            "-y  yoseui to videocontrol key (%08X)\n"
            "-c  yoseui to clock key (%08X)\n",
            MSGQKEY_V2Y, MSGQKEY_Y2V, MSGQKEY_C2Y);
}

int main(int argc, char **argv)
{
    int cmd_opt = 0;
    int msgq_key = DEFAULT_INVALID_KEY;
    int msgq_type = YOSE_MESSAGE_TYPE;  // default value
    int tmp_key = 0;
    int tmp_type = 0;
    int res = 0;
    int r;

    //fprintf(stderr, "argc: %d\n", argc);
    while(1) {
        //fprintf(stderr, "process index: %d\n", optind);
        cmd_opt = getopt(argc, argv, "hk:t:vycq");

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
            case 'v':
                msgq_key = MSGQKEY_V2Y;
                break;

            case 'y':
                msgq_key = MSGQKEY_Y2V;
                break;

            case 'c':
                msgq_key = MSGQKEY_C2Y;
                break;

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
    printf("msgq_key: %08x\n", msgq_key);
    if (msgq_key != DEFAULT_INVALID_KEY) {
        res = send_msgq(msgq_key, msgq_type, msg_str);
    }

    return res;
}
