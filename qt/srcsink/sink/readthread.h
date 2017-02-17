#ifndef __READ_THREAD_H__
#define __READ_THREAD_H__

#include <QObject>
#include <QThread>
#include <QString>
#include <QDebug>

#include "fileitem.h"
#include "util.h"

class ReadThread : public QThread
{
    Q_OBJECT

public:
    ReadThread();

    void run();

protected:

private:
    FileItem* fi = NULL;
};

#endif // __READ_THREAD_H__
