/// file: yoseshm.cpp

#include "yoseshm.h"
#include "shmdef.h"

#include <QDebug>

#include <unistd.h>
#include <error.h>
#include <sys/shm.h>

#define MAX_BUFFER_SIZE 4096
struct shm_st {
    uint32_t size;
    byte buffer[MAX_BUFFER_SIZE];
};

void myShm::saveToShm(uint32_t size, const void* buffer)
{
    int shm_id;
    shm_st *st;

    qDebug() << Q_FUNC_INFO << "claim size:" << size + sizeof(uint32_t);
    // get id of shared memory
    shm_id = shmget((key_t)SHMKEY, sizeof(shm_st), 0600 | IPC_CREAT);
    if (shm_id == -1) {
        perror("shmget");
        return;
    }

    // attach shared memory
    st = (shm_st*)shmat(shm_id, (void*)0, 0);
    if (st == (void*)-1) {
        perror("shmget");
        return;
    }

    // record size of buffer
    st->size = size;
    // copy content into shared memory
    memcpy(st->buffer, buffer, size);

    // detach shared memory
    if (shmdt(st) == -1) {
        perror("shmdt");
        return;
    }

}

void myShm::readFromShm(uint32_t& size, void* buffer)
{
    int shm_id;
    shm_st *st;
    // get the ID of shared memory,
    // fail if specified shmem not created
    shm_id = shmget((key_t)SHMKEY, sizeof(shm_st), 0600 | IPC_EXCL);
    if (shm_id == -1) {
        perror("shmget");
        return;
    }
    // attach shared memory
    st = (shm_st*)shmat(shm_id, (void *)0, 0);
    if (st == (void *)-1) {
        perror("shmget");
        return;
    }
    size = st->size;
    memcpy(buffer, st->buffer, size);
    // detach shared memory
    if (shmdt(st) == -1) {
        perror("shmdt");
        return;
    }
}

void myShm::removeShm()
{
    qDebug() << Q_FUNC_INFO;
    int shm_id;
    // get id of shm
    shm_id = shmget((key_t)SHMKEY, sizeof(shm_st), 0600 | IPC_EXCL);
    if (shm_id == -1) {
        perror("shmget");
        return;
    }
    // destroy shared memory
    if (shmctl(shm_id, IPC_RMID, 0) == -1) {
        perror("shmctl");
        return;
    }
}
