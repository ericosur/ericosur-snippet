#include "flock_wait.h"
#include "flock.h"
#include <stdio.h>
#include <QDebug>

FlockWaitThread::FlockWaitThread(const QString& pidfile)
{
    qDebug() << Q_FUNC_INFO << "created... pidfile:" << pidfile;
    mPidFile = pidfile;
}

void FlockWaitThread::run()
{
	qDebug() << Q_FUNC_INFO << "starts...";
    // block here if file lock is not granted
    FILE* fptr = util_file_lock_wait(mPidFile.toUtf8());
    qDebug() << "file lock is released...";
    if (fptr != NULL) {
        fclose(fptr);
    }
    // thread finished if flock is released
}
