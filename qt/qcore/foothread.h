#ifndef FOOTHREAD_H
#define FOOTHREAD_H

#include <QObject>
#include <QThread>

class FooThread : public QThread
{
    Q_OBJECT

public:
    FooThread();

    void run();

public slots:
    void onClose();

};

#endif // FOOTHREAD_H
