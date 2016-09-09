/**
    \file actionhandler.h
    \brief header file for class ActionHandler
**/
#ifndef __ACTIONHANDLER_H__
#define __ACTIONHANDLER_H__

#include <QObject>
#include <QHash>
#include <QString>
#include <QStringList>

class ActionHandler;
typedef void (ActionHandler::*fpAct)(void);

/**
    \brief ActionHandler

    Just connect a signal to ActionHandler::sltHandleMsg()
    and redirect a QString command string to this class.
**/
class ActionHandler : public QObject
{
    Q_OBJECT
public:
    enum ACTIONTYPE {
        AT_NONE = -1,
        AT_FALSE = 0,
        AT_TRUE = 1
    };

    enum ACTION_RETTYPE {
        RET_NORMAL = 0,
        RET_EXIT = 199,
    };

    static ActionHandler* getInstance();
    QStringList getList() {
        return dict.keys();
    }
    QStringList getUiList() {
        return uidict.keys();
    }
    int getReturnCode() const {
        return m_ret;
    }

public slots:
    // volmsg send command string to this slot function
    void sltHandleMsg(const QString& s);

signals:
    void sigPrint(const QString& s);

protected:
    static ActionHandler* _instance;
    explicit ActionHandler();

    void initActionTable();
    void init_ui_dict();
    int splitArgs(const QString& s);
    ACTIONTYPE getType(const QString& s);
    QString getArg(const QString& defaultstr = "on");
    int getArgNumber(int defaultval = 0);

private:
    // action functions for commands
    void actList();
    void actHome();
    void actQuit();
    void actShow();

private:
    // a hash table for command vs action function
    QHash<QString, fpAct> dict;
    fpAct fp;
    int m_ret = 0;

    QString m_msg;  // complete command string
    QStringList m_args;  // arguments
    QHash<QString, QString> uidict;
};

#endif  // __ACTIONHANDLER_H__
