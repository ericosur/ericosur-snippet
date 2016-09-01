#include <stdio.h>
#include <unistd.h>

//#define DEMO_PID_FILE   "/var/run/mylock.pid"
#define DEMO_PID_FILE   "./mylock.pid"
/// default sleep (in seconds)
#define DEFAULT_SLEEP   (60*1)

FILE *util_file_lock_wait(const char *fname);
int util_file_unlock_wait(FILE  *lockf);
int util_file_lock(const char *name);

int main(int argc, char** argv)
{
    fprintf(stderr, "%s: pid:%d\n", argv[0], getpid());
    FILE* ptr = util_file_lock_wait(DEMO_PID_FILE);
    if (ptr == NULL) {
        perror("fail to lock:");
    } else {
        fprintf(stderr, "yeah I got lock: %s\n", DEMO_PID_FILE);
    }

    while (1) {
        sleep(DEFAULT_SLEEP);
    }

    return 0;
}
