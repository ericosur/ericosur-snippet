#ifndef YOSEMSG_H
#define YOSEMSG_H

#include <QObject>
#include <QThread>

class YoseMsg : public QThread
{
    Q_OBJECT

public:
    YoseMsg() {}
    ~YoseMsg() {}

    void run();

public slots:
    void sltPrint(const QString& s);

signals:
    void sigReceived(const QString& s);

};

#endif // YOSEMSG_H
