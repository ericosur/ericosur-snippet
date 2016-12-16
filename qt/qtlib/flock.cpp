/**
    \file flock.c
    \brief implementation for flock
**/

#include <sys/file.h>
#include <stdio.h>
#include <errno.h>
#include <fcntl.h>

/**
 * @brief do exclusive file lock and block until we get an exclusive lock
 *
 * @param fname - the file name of lock file ( ex: config.conf.lck )
 * @return FILE * - lock file descriptor;  NULL: error
 */
FILE *util_file_lock_wait(const char *fname)
{
    FILE    *lockf;

    lockf = fopen(fname, "w+");

    /* block until we get an exclusive lock */
    if (flock(fileno(lockf), LOCK_EX)) {
        perror("fail to lock:");
        return NULL;
    }
    return lockf;
}

/**
 * @brief do exclusive file unlock
 *
 * @param lockf - the file descriptor of lock file return by util_file_lock_wait()
 * @return int - 0:no error; <0: error
 */
int util_file_unlock_wait(FILE  *lockf)
{
    if( lockf == NULL )
        return -1;

    /* block until we get an exclusive lock */
    if (flock(fileno(lockf), LOCK_UN)) {
        perror("fail to unlock:");
        return -2;
    }
    fclose(lockf);
    return 0;
}

/**
 * @brief do exclusive non-block file lock
 *
 * @param name - the full path and file name of lock file ( ex: /var/run/btui.pid )
 * @return int - 0:no error; !0: error
 */
int util_file_lock(const char *name)
{
    int file = open(name, O_CREAT | O_RDWR, 0666);
    int ret = flock(file, LOCK_EX | LOCK_NB);

    if(ret) {
        if(EWOULDBLOCK == errno) {
            perror("File is being used!!!\n");
            return ret;
        }
    }

    return 0;
}

int util_test_file_lock(const char *name)
{
    int file = open(name, O_CREAT | O_RDWR, 0660);
    int ret = flock(file, LOCK_EX | LOCK_NB);
    if ( ret ) {
        if (EWOULDBLOCK == errno) {
            fprintf(stderr, "name: %s ", name);
            perror("File is being used!!!");
            return ret;
        }
    }
    if ( flock(file, LOCK_UN) != 0 ) {
        fprintf(stderr, "name: %s ", name);
        perror("unlock:");
    }

    return 0;
}
