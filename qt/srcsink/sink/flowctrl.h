#ifndef __FLOW_CTRL_H__
#define __FLOW_CTRL_H__

#include <QObject>
#include <QString>
#include <QDebug>

#include "msgqsend.h"
#include "fileitem.h"
#include "readthread.h"
#include "commonutil.h"

class FlowControl : public QObject
{
    Q_OBJECT

public:
    static FlowControl* getInstance();

    void start();
    void requestGetfolder();

signals:
    void sigGetfolder();
    void sigQuitApp();

public slots:
    void sltReadFinished();
    void sltGetfolder();

protected:
    static FlowControl* _instance;
    FlowControl();

    void check_shm();

private:
    ReadThread* readthead = NULL;
    bool mFileFinished = false;
    bool mFolderFinished = false;
};

#endif // __FLOW_CTRL_H__
