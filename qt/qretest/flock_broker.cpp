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
    qDebug() << Q_FUNC_INFO << "created...";
}

FlockBroker::~FlockBroker()
{
    qDebug() << Q_FUNC_INFO;
    if (waitlock)
        delete waitlock;
    if (waitunlock)
        delete waitunlock;
    if (simpleNotify)
        delete simpleNotify;
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

void FlockBroker::startWatchFile()
{
    simpleNotify = new SimpleNotify(OBSERVE_FILE);
    connect(simpleNotify, SIGNAL(sigNotify()), this, SLOT(sltFileChanged()));
    connect(simpleNotify, SIGNAL(finished()), this, SLOT(sltNotifyFinished()));
    simpleNotify->start();
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

void FlockBroker::sltFileChanged()
{
    qDebug() << Q_FUNC_INFO;

}

void FlockBroker::sltNotifyFinished()
{
    qDebug() << Q_FUNC_INFO;
}
