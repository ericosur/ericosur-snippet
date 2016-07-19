#include <QStringList>
#include <QDebug>

#include <sys/types.h>
#include <sys/msg.h>
#include <sys/ipc.h>

#include "msgqdef.h"
#include "yosemsg.h"
#include "yoseshm.h"

YoseMsg::YoseMsg()
{
    m_fp = NULL;

    connect(this, SIGNAL(sigPrint(const QString&)), this, SLOT(sltPrint(const QString&)));

    initActionTable();
    m_shouldRun = true;
}

void YoseMsg::initActionTable()
{
    actionTable["home"] = &YoseMsg::actHome;
    actionTable["quit"] = &YoseMsg::actQuit;
    actionTable["read"] = &YoseMsg::actRead;
    actionTable["md5sum"] = &YoseMsg::actMd5sum;
    actionTable["write"] = &YoseMsg::actWrite;
}

void YoseMsg::removeMsg()
{
    int msg_id;

    msg_id = msgget(MESGQKEY, IPC_EXCL|0660);
    if(msg_id == -1) {
        perror("msgget");
        return; // error here
    }
    // remove an existed message queue
    if (msgctl(msg_id, IPC_RMID, NULL) == -1) {
        perror("msgctl");
        return;
    }
}

void YoseMsg::run()
{
    int msgqueue_id;
    struct mymsgbuf qbuf;

    qDebug() << Q_FUNC_INFO;
    if((msgqueue_id = msgget(MESGQKEY, IPC_CREAT|0660)) == -1) {
        perror("msgsnd: msgget");
        return; // error here
    }
    qDebug() << "mythread: key: " << QString("0x") + QString::number(MESGQKEY, 16).toUpper()
        << " msgqueue_id: " << msgqueue_id;
    while ( m_shouldRun ) {
        memset(&qbuf, 0, sizeof(qbuf));
        qbuf.mtype = YOSE_MESSAGE_TYPE;
        msgrcv(msgqueue_id, (struct mymsgbuf *)&qbuf, MAX_SEND_SIZE, YOSE_MESSAGE_TYPE, 0);
        //printf("Type: %ld Text: %s\n", qbuf.mtype, qbuf.mtext);
        m_msg = qbuf.mtext;
        qDebug() << "msgqueue: " << " type: " << qbuf.mtype << " text: " << qbuf.mtext;
        dispatchAction();
    }
    qDebug() << Q_FUNC_INFO << "end of loop";
}

void YoseMsg::dispatchAction()
{
    QString cmd = m_msg.split(" ").at(0);
    if (actionTable.contains(cmd)) {
        m_fp = actionTable[cmd];
        (*this.*m_fp)();
    } else {
        qDebug() << Q_FUNC_INFO << "unknow command:" << m_msg;
        emit sigPrint(m_msg);
    }
}

void YoseMsg::actHome()
{
    emit sigHome();
}

void YoseMsg::actQuit()
{
    // remove shm
    myShm::removeShm();
    m_shouldRun = false;
    YoseMsg::removeMsg();
    exit();

    emit sigQuit();
}

void YoseMsg::actRead()
{
    QStringList list = m_msg.split(" ");
    QString parm;
    if (list.size() > 1) {
        parm = list.at(1);
    }
    qDebug() << Q_FUNC_INFO << "parm:" << parm;
    emit sigRead(parm);
}

void YoseMsg::actMd5sum()
{
    QStringList list = m_msg.split(" ");
    QString parm;
    if (list.size() > 1) {
        parm = list.at(1);
    }
    qDebug() << Q_FUNC_INFO << "parm:" << parm;
    emit sigMd5sum(parm);
}

void YoseMsg::actWrite()
{
    qDebug() << Q_FUNC_INFO;
    emit sigWrite();
}

void YoseMsg::sltPrint(const QString& s)
{
    qDebug() << Q_FUNC_INFO << "print:" << s;
}

void YoseMsg::sltHome()
{
    qDebug() << Q_FUNC_INFO;
}

void YoseMsg::sltAskQuit()
{
    qDebug() << Q_FUNC_INFO;
    actQuit();
}
