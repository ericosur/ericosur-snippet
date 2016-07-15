#ifndef __MSGQCOMMAND_H__
#define __MSGQCOMMAND_H__

#include <QObject>
#include <QHash>
#include <QString>
#include <QStringList>

class MyCtrl;
typedef void (MyCtrl::*fpAct)(void);

class MyCtrl : public QObject
{
    Q_OBJECT

public:
    MyCtrl();

    Q_PROPERTY(QStringList mylist READ getMylist NOTIFY sigMylistChanged);

    Q_INVOKABLE void qmlRunCommand(const QString& cmd);

    void doCommand(const QString& cmd);
    void actTest();

    QStringList getMylist() const {
        return mylist;
    }

    void initList();

signals:
    void sigTest();
    void sigError();

    void sigMylistChanged();

private:
    void initHash();

private:
    QHash<QString, fpAct> myhash;
    // need this function pointer to refer fpAct from hash
    fpAct fp;

    QStringList mylist;
};


#endif  // __MSGQCOMMAND_H__
