#include "funlock_wait.h"
#include "flock.h"
#include "flock_broker.h"
#include <QDebug>

FunlockWaitThread::FunlockWaitThread()
{
    qDebug() << Q_FUNC_INFO << "created...";
}

void FunlockWaitThread::run()
{
    // block here if file lock is not granted
    int ret = util_file_unlock_wait(FlockBroker::getInstance()->getLockPtr());
    if (ret == 0) {
        qDebug() << "util_file_unlock_wait() unlocked...";
    }
}
