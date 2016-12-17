#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include "msgqrx.h"
#include "flock_wait.h"

class Core : public QObject
{
	Q_OBJECT

public:
    static Core* _instance;
    static Core* getInstance();

signals:
	void sigQuit();

public slots:
	void sltMessageReceived(const QString& msg);
	void sltWaitFinished();

protected:
    Core();

private:
	MsgRxThread* msgrx = NULL;
	FlockWaitThread* lockwait = NULL;
};

#endif	// __CORE_H__
