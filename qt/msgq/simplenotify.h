#ifndef __SIMPLE_NOTIFY_H__
#define __SIMPLE_NOTIFY_H__

#include <QObject>
#include <QString>
#include <QThread>

// use QThread to wrap a INotify system for monitor file change
class SimpleNotify : public QThread
{
    Q_OBJECT

public:
    SimpleNotify(const QString& watch_file);
    ~SimpleNotify() {}

    void run();

public slots:

signals:
    void sigNotify();

private:
    QString m_filename; // file to monitor
};

#endif // __SIMPLE_NOTIFY_H__
