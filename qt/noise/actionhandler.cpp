/**
    \file actionhandler.cpp
    \brief implementation of class ActionHandler
**/
#include "actionhandler.h"
#include <QCoreApplication>
#include <QDebug>
#include <QString>
#include <QStringList>

ActionHandler* ActionHandler::_instance = NULL;
ActionHandler* ActionHandler::getInstance()
{
    if (_instance == NULL) {
        _instance = new ActionHandler;
    }
    return _instance;
}

ActionHandler::ActionHandler()
{
    fp = NULL;
    m_msg = "";
    m_args.clear();

    initActionTable();
    init_ui_dict();
}

/**
    \brief a hash table for command vs handle function

    \note more than one command goes to the same function
**/
void ActionHandler::initActionTable()
{
    dict["list"] = &ActionHandler::actList;
    dict["home"] = &ActionHandler::actHome;
    dict["quit"] = &ActionHandler::actQuit;
    dict["exit"] = &ActionHandler::actQuit;
    dict["help"] = &ActionHandler::actList;
    dict["show"] = &ActionHandler::actShow;
}

void ActionHandler::init_ui_dict()
{
    uidict["btui"] = "btui/1.0-r0/package/usr/share/btui";
    uidict["hdmiui"] = "hdmiui/1.0-r0/package/usr/share";
    uidict["launcherui"] = "launcherui/1.0-r0/package/usr/share";
    uidict["mediaui"] = "mediaui/1.0-r0/package/usr/share/mediaui";
    uidict["mediarearui"] = "mediaui/1.0-r0/package/usr/share/mediarearui";
    uidict["radioui"] = "radioui/1.0-r0/package/usr/share/radioui";
    uidict["abeep"] = "abeep/1.0-r0/package/usr/sbin";
    uidict["statusbarui"] = "statusbarui/1.0-r0/package/usr/sbin";
    uidict["videocontrol"] = "videocontrol/1.0-r0/package/usr/share/videocontrol-1.0";
    uidict["vdcrear"] = "videocontrolrear/1.0-r0/package/usr/share/videocontrolrear-1.0";
    uidict["testtool"] = "testtool/1.0-r0/package/usr/share/testtool-1.0";
    uidict["msgbox"] = "appipctool/1.0-r0/package/usr/sbin";
    uidict["testopt"] = "appipctool/1.0-r0/package/usr/sbin";
    uidict["testmemcpy"] = "appipctool/1.0-r0/package/usr/sbin";
    uidict["testmemset"] = "appipctool/1.0-r0/package/usr/sbin";
}

/**
    \brief splitArgs() use seperator "/" to split str
    into left-hand-side and right-hand-side part and
    store into m_args
**/
int ActionHandler::splitArgs(const QString& str)
{
    if (str.length() <= 0) {
        qDebug() << Q_FUNC_INFO << "str.length() <= 0";
        return -1;
    }
    m_args.clear();
    int i = str.indexOf(" ");
    if (i < 0) {
        m_args.append(str);
    } else {
        m_args.append( str.left(i) );   // left-hand-side
        m_args.append( str.right(str.length() - i - 1) );   // right-hand-side
    }
    //m_args = str.split("/");
//    qDebug() << Q_FUNC_INFO << "args.size()" << m_args.size();
//    for (int i = 0; i < m_args.size(); ++i) {
//        qDebug() << i << m_args.at(i);
//    }
    return m_args.size();
}
/**
    \brief all unhandled command string goes here
    it split, and issue commands

    \note the first string at m_args will be converted
    to lower case
**/
void ActionHandler::sltHandleMsg(const QString& s)
{
    //qDebug() << Q_FUNC_INFO << "recv:" << s;
    m_msg = s;
    if ( splitArgs(m_msg) <= 0 ) {
        qDebug() << "no arguments, exit...";
        return;
    }
    QString cmd = m_args.at(0).toLower();   // cmd is taken as lower case
    if (dict.contains(cmd)) {
        fp = dict[cmd];
        // a very strange way to call function pointer to current class
        (*this.*fp)();
    } else {
        qDebug() << Q_FUNC_INFO << "NO such command!!";
    }
}

ActionHandler::ACTIONTYPE ActionHandler::getType(const QString& arg)
{
    ACTIONTYPE ret = AT_NONE;
    if (arg == "on" || arg == "1" || arg == "true" || arg == "yes") {
        ret = AT_TRUE;
    } else if (arg == "off" || arg == "0" || arg == "false" || arg == "no") {
        ret = AT_FALSE;
    }
    return ret;
}
QString ActionHandler::getArg(const QString& defaultstr)
{
    QString arg;
    if (m_args.size() <= 1) {
        arg = defaultstr;
    } else {
        arg = m_args.at(1);
    }
    //qDebug() << "arg:" << arg;
    return arg;
}
int ActionHandler::getArgNumber(int defaultval)
{
    int val = defaultval;
    if (m_args.size() <= 1) {
        val = defaultval;
        return val;
    }

    QString arg = m_args.at(1);
    bool ok = false;
    qDebug() << "arg:" << arg;
    val = arg.toInt(&ok, 10);
    if (!ok) {
        val = defaultval;
    }
    return val;
}
void ActionHandler::actList()
{
    qDebug() << Q_FUNC_INFO << "all supported msgq commands:";
    QHashIterator<QString, fpAct> i(dict);
    while (i.hasNext()) {
        i.next();
        qDebug() << i.key();
    }
}
void ActionHandler::actQuit()
{
    //QCoreApplication::exit();
    m_ret = RET_EXIT;
}
void ActionHandler::actHome()
{
    qDebug() << "go home...";
}
void ActionHandler::actShow()
{
    QString arg = getArg();
    //qDebug() << "show args..." << arg;
}
