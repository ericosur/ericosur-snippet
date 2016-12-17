#include <QCoreApplication>
#include "flock_broker.h"

FlockBroker* FlockBroker::_instance = NULL;
FlockBroker* FlockBroker::getInstance() {
    if (_instance == NULL) {
        _instance = new FlockBroker;
    }
    return _instance;
}

FlockBroker::FlockBroker()
{

}

FlockWaitThread* FlockBroker::getWaitLock()
{
    if (waitlock == NULL) {
        // start a thread and wait for it finished
        waitlock = new FlockWaitThread;
    }
    return waitlock;
}

FunlockWaitThread* FlockBroker::getWaitUnlock()
{
    if (waitunlock == NULL) {
        // start a thread and wait for it finished
        waitunlock = new FunlockWaitThread;
    }
    return waitunlock;
}

void FlockBroker::startLockWait()
{
    connect(getWaitLock(), SIGNAL(finished()), getInstance(), SLOT(sltLockWaitFinished()));
    getWaitLock()->start();
}

void FlockBroker::startUnlockWait()
{
    connect(getWaitUnlock(), SIGNAL(finished()), getInstance(), SLOT(sltUnlockWaitFinished()));
    getWaitUnlock()->start();
}

void FlockBroker::setLockPtr(FILE* ptr)
{
    qDebug() << Q_FUNC_INFO;
    lock_ptr = ptr;
}

FILE* FlockBroker::getLockPtr()
{
    return lock_ptr;
}

void FlockBroker::sltLockWaitFinished()
{
    qDebug() << Q_FUNC_INFO;
    getInstance()->startUnlockWait();
}

void FlockBroker::sltUnlockWaitFinished()
{
    qDebug() << Q_FUNC_INFO;
}
