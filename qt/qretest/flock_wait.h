#ifndef __FLOCK_WAIT_H__
#define __FLOCK_WAIT_H__

#include <QObject>
#include <QThread>

class FlockWaitThread : public QThread
{
public:
    FlockWaitThread();

    void run();
private:

};


#endif  // __FLOCK_WAIT_H__
