/**
    \file commonutil.h
    \brief provides some common utility function here

    - macro SHOW_CURRECT_EPOCH() will show elapse time into qDebug()
    - myMessageOutput() is cusomized message handler function to redirect
        qDebug() info
**/
#ifndef __COMMONUTIL_H__
#define __COMMONUTIL_H__

#include <QtGlobal>


// macro to show epoch time elapse everywhere at c++ code
extern qint64 g_epoch_start;
#define SHOW_CURRENT_EPOCH()    \
	qDebug() << __FILE__ << "func:" << Q_FUNC_INFO << "#" << __LINE__ << "elapse:" << ( QDateTime::currentMSecsSinceEpoch() - g_epoch_start )

extern bool g_messageVerbose;
// customized message handler
void myMessageOutput(QtMsgType type, const QMessageLogContext &context, const QString &msg);

#endif  // __COMMONUTIL_H__
