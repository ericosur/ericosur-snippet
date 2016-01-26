#ifndef MYTHREADS_H
#define MYTHREADS_H

#include <QObject>
#include <QThread>
#include <QSettings>
#include <QElapsedTimer>

class MyEmptyThread : public QThread
{
    Q_OBJECT
public:
    MyEmptyThread(QSettings *set);
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

protected:
    QSettings *m_setting;
    QString m_result;
    int m_count;
    QElapsedTimer e;
};


class ThreadFoo : public MyEmptyThread
{
    Q_OBJECT
public:
    ThreadFoo(QSettings *set);
    ~ThreadFoo() {}
    void run();

};


class ThreadBar : public MyEmptyThread
{
    Q_OBJECT
public:
    ThreadBar(QSettings *set);
    ~ThreadBar() {}
    void run();

};

#endif // MYTHREADS_H
