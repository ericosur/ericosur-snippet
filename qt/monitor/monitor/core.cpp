#include "core.h"
#include <QCoreApplication>
#include <QDebug>

Core* Core::_instance = NULL;
Core* Core::getInstance()
{
	if (_instance == NULL) {
		_instance = new Core();
	}
	return _instance;
}

Core::Core()
{
	qDebug() << Q_FUNC_INFO << "created...";

	// thread to receive msgq
	if (msgrx == NULL) {
		msgrx = new MsgRxThread;
	}
	// thread to wait flock
	if (lockwait == NULL) {
		lockwait = new FlockWaitThread("/tmp/foo.pid");
	}

	connect(msgrx, SIGNAL(sigReceived(const QString&)),
		this, SLOT(sltMessageReceived(const QString&)));
	connect(lockwait, SIGNAL(finished()),
		this, SLOT(sltWaitFinished()));
	connect(this, SIGNAL(sigQuit()),
		qApp, SLOT(quit()));

	if (msgrx != NULL) {
		msgrx->start();
	}
}

void Core::sltMessageReceived(const QString& msg)
{
	qDebug() << Q_FUNC_INFO << "msg:" << msg;
	if (msg == "foo") {
		qDebug() << "IPC notification: foo starts...";
		// start wait flock thread
		if (lockwait != NULL) {
			lockwait->start();
		}
	} else if (msg == "quit") {
		qDebug() << "quit command received...";
		emit sigQuit();
	}
}

void Core::sltWaitFinished()
{
	qDebug() << "foo is NOT running...";
}
