#ifndef __FUNLOCK_WAIT_H__
#define __FUNLOCK_WAIT_H__

#include <QObject>
#include <QThread>

class FunlockWaitThread : public QThread
{
public:
    FunlockWaitThread();

    void run();
private:

};


#endif  // __FUNLOCK_WAIT_H__
