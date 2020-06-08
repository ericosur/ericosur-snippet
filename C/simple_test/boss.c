/*
    example code from: https://linuxhint.com/linux-exec-system-call/
    boss.c and worker.c
 */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    printf("PID of example.c = %d\n", getpid());
    char *args[] = {"Hello", "C", "Programming", NULL};
    execv("./worker", args);
    printf("===== back to boss.c =====\n");
    return 0;
}
