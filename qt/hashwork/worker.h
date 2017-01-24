/**
 * \file worker.h
 */

#ifndef __WORKER_H__
#define __WORKER_H__

#include <QThread>
#include <QCryptographicHash>

class Worker : public QObject
{
    Q_OBJECT

public:
    Worker();

public slots:
    void sltWork();

protected:
    void do_something();

private:
    QThread* mThread = NULL;

};

#endif  // __WORKER_H__
