#include <QThread>

class WaitOneSecond : public QThread
{
	Q_OBJECT
public:
	WaitOneSecond(int d = 100) {
		m_delay = d;
	}
	void run() {
		QThread::msleep(m_delay);
	}
private:
	int m_delay;
};
