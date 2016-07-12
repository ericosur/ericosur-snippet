#ifndef __MSGQCOMMAND_H__
#define __MSGQCOMMAND_H__

#include <QObject>
#include <QHash>
#include <QString>


class MyCtrl;
typedef void (MyCtrl::*fpAct)(void);

class MyCtrl : public QObject
{
    Q_OBJECT

public:
    MyCtrl();

    Q_INVOKABLE void qmlRunCommand(const QString& cmd);

    void doCommand(const QString& cmd);
    void actTest();

    //void (Foo::*do_something)(void);

signals:
    void sigTest();
    void sigError();

private:
    void initHash();

private:
    QHash<QString, fpAct> myhash;

    // need this function pointer to refer fpAct from hash
    fpAct fp;
};


#endif  // __MSGQCOMMAND_H__
