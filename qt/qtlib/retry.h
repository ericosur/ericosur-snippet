/**
	\file retry.h
	\brief header file for class RetryThread
**/

#ifndef __RETRY_H__
#define __RETRY_H__

#include <QThread>

struct myoptions;

/** \brief RetryThread will send message queue string every period time
**/
class RetryThread : public QThread
{
	Q_OBJECT
public:
	RetryThread();
	/// thread body here
	void run();

protected:
	/** \brief send str into message queue

		use myoptions to set msgq_key, msgq_type, and msgq_size

		\param opt [in] message queue key, type, and buffer size to send
		\param str [in] string to send
	**/
	int send_msgq(struct myoptions* opt, const char* str);

public slots:
	/// notify this slot and try to finish this thread...
	void sltNotifyStop();

private:
	/// count for retry times
	int m_retrycount = 0;
	/// set it to false will break while-loop at run()
	bool m_shouldrun = true;
};

#endif	// __RETRY_H__
