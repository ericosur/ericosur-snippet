#include <unistd.h>  /* getopt */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_VALID_KEY           0x7FFFFFFF
#define MAX_BUFFER_SIZE         (1024+sizeof(long))
#define DEFAULT_INVALID_KEY     0xDEADBEEF
#define DEFAULT_MESSAGE_TYPE    9
#define DEFAULT_SEND_SIZE       64
#define MAX_ARGV_SIZE           DEFAULT_SEND_SIZE
#define MIN_SEND_SIZE           16

#define MSGQKEY_V2Y        0x600DFEA6
#define MSGQKEY_Y2V        0x600DCAFE
#define MSGQKEY_C2Y        0x00C0FFEE

#define MYMIN(x, y) ((x > y) ? y : x)

struct myoptions {
    int msgq_key;
    long msgq_type;
    int msgq_size;
};

void dump(unsigned char* buf, unsigned int size)
{
    for (unsigned int i = 0; i < size; i++) {
        if (i && i%16==0)  printf("\n");
        printf("%02X ", buf[i]);
    }
    printf("\n");
}

void dump_opt(struct myoptions* opt)
{
    printf("key: 0x%08X type: %ld size: %d\n",
        opt->msgq_key, opt->msgq_type, opt->msgq_size);
}
int send_msgq(struct myoptions* opt, const char* str)
{
    int msqid;
    unsigned char buffer[MAX_BUFFER_SIZE];

    printf("send_msgq(): str: %s\n", str);
    // only open a listening (previously created) message queue
    //msqid = msgget( opt->key, 0660 | IPC_EXCEL );
    msqid = msgget( opt->msgq_key, 0660 | IPC_CREAT );
    if ( msqid < 0 ) {
        perror("msgget: get message queue error");
        return -1;
    } else {
        printf("msgget: msqid: %d\n", msqid);
    }

    if (opt->msgq_size > MAX_BUFFER_SIZE - sizeof(long)) {
        opt->msgq_size = MAX_BUFFER_SIZE - sizeof(long);
        fprintf(stderr, "assigned msgq_size is too large, "
            "modified to %d\n", opt->msgq_size);
    }
    if (opt->msgq_size < MIN_SEND_SIZE) {
        opt->msgq_size = MIN_SEND_SIZE;
        fprintf(stderr, "assigned msgq_size is too small, "
            "modified to %d\n", opt->msgq_size);
    }

    dump_opt(opt);

    memset(buffer, 0, MAX_BUFFER_SIZE);
    memcpy(buffer, &opt->msgq_type, sizeof(long));
    if (strlen(str)+1 > opt->msgq_size) {
        fprintf(stderr, "strlen > msgq_size, msg not sent\n");
        return -1;
    }
    memcpy(buffer+sizeof(long), str, strlen(str)+1);
    dump(buffer, opt->msgq_size+sizeof(long));
    if ( msgsnd(msqid, &buffer, opt->msgq_size, 0) < 0 ) {
        perror("msgsnd: send message error");
        return -1;
    }
    return 0;
}

void print_help()
{
    fprintf(stderr,
            "testopt [options] <message>\n"
            "-h  help message\n"
            "-k  assign key\n"
            "-t  assign type (default:9)\n"
    );
}

void process_cmd_opt(int argc, char** argv, struct myoptions* opt)
{
    int cmd_opt = 0;
    int tmp_key = 0;
    int tmp_type = 0;
    int tmp_size = 0;
    int r;

    opt->msgq_key = DEFAULT_INVALID_KEY;
    opt->msgq_type = DEFAULT_MESSAGE_TYPE;
    opt->msgq_size = DEFAULT_SEND_SIZE;

    //fprintf(stderr, "argc: %d\n", argc);
    while(1) {
        //fprintf(stderr, "process index: %d\n", optind);
        cmd_opt = getopt(argc, argv, "hk:t:s:q");

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
                print_help();
                exit(2);
                break;
            /* Single arg */
            case 'k':
                //fprintf(stderr, "option arg: %s\n", optarg);
                tmp_key = strtol(optarg, NULL, 16);
                //fprintf(stderr, "assign key = 0x%08X\n", tmp_key);
                if (tmp_key > 0) {
                    opt->msgq_key = tmp_key;
                }
                break;
            case 't':
                tmp_type = strtol(optarg, NULL, 10);
                //fprintf(stderr, "assign type = %d\n", tmp_type);
                opt->msgq_type = tmp_type;
                break;
            case 's':
                tmp_size = strtol(optarg, NULL, 10);
                //fprintf(stderr, "assign size = %d\n", tmp_size);
                opt->msgq_size = tmp_size;
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

}

void test()
{
struct mymsgbuf {
    long mtype;
    char mtext[DEFAULT_SEND_SIZE];
} bb;

    bb.mtype = 9;
    strncpy(bb.mtext, "hello world", DEFAULT_SEND_SIZE);
    dump((unsigned char*)&bb, sizeof(bb));
}

int main(int argc, char **argv)
{
    struct myoptions opt = {DEFAULT_INVALID_KEY,
        DEFAULT_MESSAGE_TYPE, DEFAULT_SEND_SIZE};

    process_cmd_opt(argc, argv, &opt);

    char msg_str[MAX_ARGV_SIZE];
    /* Do we have args? */
    if (argc > optind) {
        int i = 0;
        for (i = optind; i < argc; i++) {
            //fprintf(stderr, "argv[%d] = %s\n", i, argv[i]);
            memset(msg_str, 0, sizeof(msg_str));
            strncpy(msg_str, argv[i], MAX_ARGV_SIZE-1);
            break;
        }
    }
    //printf("msgq_key: %08x\n", opt.msgq_key);
    int res = 0;
    if (opt.msgq_key <= MAX_VALID_KEY) {
        res = send_msgq(&opt, msg_str);
    }

    //test();

    return res;
}
