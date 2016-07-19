/// file: proc1.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <error.h>
#include <sys/shm.h>
#include "shmem.h"

#define MAX_DURATION    6

int main(int argc, char *argv[])
{
    int             shm_id;
    struct shm_ex   *ex;
    int cnt = 0;

    /* get the ID of shared memory */
    shm_id = shmget((key_t)KEY_SHM_EXAMPLE, sizeof(struct shm_ex), 0666 | IPC_CREAT);
    if (shm_id == -1) {
        perror("shmget");
        exit(EXIT_FAILURE);
    }

    /* attach shared memory */
    ex = (struct shm_ex *)shmat(shm_id, (void *)0, 0);
    if (ex == (void *)-1) {
        perror("shmget");
        exit(EXIT_FAILURE);
    }

    /* initial value */
    ex->flag = 1;
    ex->data[0] = ex->data[1] = ex->data[2] = ex->data[3] = START_VALUE;
    while (ex->flag) {
        ex->data[0] += 2;
        ex->data[1] += 4;
        ex->data[2] += 8;
        ex->data[3] += 16;
        sleep(1);
        cnt ++;
        if (cnt > MAX_DURATION) {
            printf("%s max duration meets, call stop\n", argv[0]);
            ex->flag = 0;
        }
    }

    /* detach shared memory */
    if (shmdt(ex) == -1) {
        perror("shmdt");
        exit(EXIT_FAILURE);
    }

    /* destroy shared memory */
    if (shmctl(shm_id, IPC_RMID, 0) == -1) {
        perror("shmctl");
        exit(EXIT_FAILURE);
    }

    exit(EXIT_SUCCESS);
}
