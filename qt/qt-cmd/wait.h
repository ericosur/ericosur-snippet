#ifndef __WAIT_H__
#define __WAIT_H__

#include <QThread>
#include <QDebug>
#include <QString>

#define DEFAULT_WAIT_DURATION	1000

class WaitOneSecond : public QThread
{
	Q_OBJECT
public:
	WaitOneSecond(const QString& msg, int d = DEFAULT_WAIT_DURATION) {
		m_msg = msg;
		m_delay = d;
	}
	void run() {
		qDebug() << Q_FUNC_INFO << m_msg;
		QThread::msleep(m_delay);
	}
private:
	QString m_msg;
	int m_delay;
};

#endif	// __WAIT_H__
