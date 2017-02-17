#include "util.h"

#include <stdio.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int util_shm_write( int key, int shm_size, void *data)
{
    int shmid;
    //int ret;
    void *shmadd;

    shmid = shmget((key_t)key, shm_size, SHM_R|SHM_W|IPC_CREAT);
    if(shmid < 0) {
        perror("shmget");
        return -1;
    }

    shmadd = shmat(shmid, NULL, 0);
    if(shmadd == (void*)-1) {
        perror("shmat");
        return -1;
    }

    memcpy(shmadd, data, shm_size);

    return 0;

}

void * util_shm_read( int key, int shm_size)
{
    int shmid;
    //int ret;
    void *shmadd;

    shmid = shmget((key_t)key, shm_size, SHM_R|SHM_W|IPC_CREAT);
    if(shmid < 0)   {
        perror("shmget");
        return NULL;
    }

    shmadd = shmat(shmid, NULL, 0);
    if(shmadd == (void*)-1) {
        perror("shmat");
        return NULL;
    }

    return shmadd;
}
