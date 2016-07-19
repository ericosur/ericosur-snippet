#ifndef	_SHMEM_H
#define	_SHMEM_H

#define KEY_SHM_EXAMPLE     0x0000C0DE
#define START_VALUE         1000

struct shm_ex {
    int    flag;
    int    data[4];
};

#endif /* _SHMEM_H */
