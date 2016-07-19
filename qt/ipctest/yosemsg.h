#ifndef YOSEMSG_H
#define YOSEMSG_H

#include <QObject>
#include <QThread>
#include <QHash>
#include <QString>

class YoseMsg;
typedef void (YoseMsg::*actfp)();

class YoseMsg : public QThread
{
    Q_OBJECT

public:
    YoseMsg();
    ~YoseMsg() {}

    void run();

public slots:
    void sltPrint(const QString& s);
    void sltHome();
    //void sltQuit();

signals:
    void sigPrint(const QString& s);
    void sigHome();
    void sigQuit();
    void sigRead(const QString& s);
    void sigMd5sum(const QString& s);
    void sigWrite();

protected:
    void initActionTable();
    void dispatchAction();

    void actHome();
    void actQuit();
    void actRead();
    void actMd5sum();
    void actWrite();

private:
    QString m_msg;
    QHash<QString, actfp> actionTable;
    actfp m_fp;
};

#endif // YOSEMSG_H
