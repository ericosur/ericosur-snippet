/// file: proc2.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <error.h>
#include <unistd.h>
#include <sys/shm.h>
#include "shmem.h"

// 500ms
#define SLEEP_DURATION  (750*1000)

int main(int argc, char *argv[])
{
    int             shm_id;
    struct shm_ex   *ex;

    /* get the ID of shared memory,
       fail if specified shmem not created
    */
    shm_id = shmget((key_t)KEY_SHM_EXAMPLE, sizeof(struct shm_ex), 0600 | IPC_EXCL);
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

    do {
        printf("%s get data:\n", argv[0]);
        printf("\tdata[0]: %d\n", ex->data[0]);
        printf("\tdata[1]: %d\n", ex->data[1]);
        printf("\tdata[2]: %d\n", ex->data[2]);
        printf("\tdata[3]: %d\n", ex->data[3]);
        usleep(SLEEP_DURATION);
    } while (ex->flag);

    if ( ex->flag == 0 ) {
        printf("%s end\n", argv[0]);
    }

    /* detach shared memory */
    if (shmdt(ex) == -1) {
        perror("shmdt");
        exit(EXIT_FAILURE);
    }

    exit(EXIT_SUCCESS);
}
