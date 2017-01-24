#ifndef __POLL_THREAD_H__
#define __POLL_THREAD_H__

#include <QObject>
#include <QThread>
#include <QByteArray>
#include <QString>

class PollThread : public QThread
{
    Q_OBJECT

public:
    PollThread();
    void run();

protected:
    void do_hard_work();
    QByteArray fill_buffer(const int size);

signals:

private:
    QString mAnswer;
};

#endif // __POLL_THREAD_H__
