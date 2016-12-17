#include "testcases.h"
#include "flock_wait.h"
#include "flock.h"
#include "flock_broker.h"
#include <QDebug>

FlockWaitThread::FlockWaitThread()
{
    qDebug() << Q_FUNC_INFO << "created...";
}
void FlockWaitThread::run()
{
    FILE* fptr = NULL;

    // block here if file lock is not granted
    fptr = util_file_lock_wait(PIDFILE);
    qDebug() << "file lock is released by another process...";

    if (fptr != NULL) {
        FlockBroker::getInstance()->setLockPtr(fptr);
    }
}
