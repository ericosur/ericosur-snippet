#ifndef MYTHREADS_H
#define MYTHREADS_H

#include <QObject>
#include <QThread>
#include <QElapsedTimer>

class MyEmptyThread : public QThread
{
    Q_OBJECT
public:
    MyEmptyThread();
    ~MyEmptyThread() {}

    QString getResult() const {
        return m_result;
    }

    int getCount() const {
        return m_count;
    }

    quint64 getEpoch() const {
        return e.elapsed();
    }

    static QString doHardWork(const QString& s, int method=0);

protected:
    QString m_result;
    int m_count;
    QElapsedTimer e;
};


class ThreadFoo : public MyEmptyThread
{
    Q_OBJECT
public:
    ThreadFoo(int method, const QString& initstr);
    ~ThreadFoo() {}
    void run();
private:
    int m_method;
    QString m_str;
};


#endif // MYTHREADS_H
