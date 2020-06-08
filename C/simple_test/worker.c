/*
    example code from: https://linuxhint.com/linux-exec-system-call/
    boss.c and worker.c
 */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    printf("We are in worker.c\n");
    printf("PID of hello.c = %d\n", getpid());
    for (int i=0; i<argc; i++) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }
    return 0;
}
