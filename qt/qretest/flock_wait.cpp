#include "flock_wait.h"
#include "flock.h"
#include "testcases.h"

#include <QDebug>

void FlockWaitThread::run()
{
    FILE* fptr = NULL;

    // block here if file lock is not granted
    fptr = util_file_lock_wait(PIDFILE);

    if (fptr != NULL) {
        fclose(fptr);
        qDebug() << "file lock is released by another process...";
    }
}
