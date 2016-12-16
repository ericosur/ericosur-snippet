#ifndef __FLOCK_WAIT_H__
#define __FLOCK_WAIT_H__

#include <QObject>
#include <QThread>

class FlockWaitThread : public QThread
{
    Q_OBJECT

public:
    FlockWaitThread() {}
    ~FlockWaitThread() {}

    void run();
private:

};


#endif  // __FLOCK_WAIT_H__
