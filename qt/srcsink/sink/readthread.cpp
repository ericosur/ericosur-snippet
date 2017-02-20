#include "readthread.h"
#include "flowctrl.h"

ReadThread::ReadThread()
{
    qDebug() << Q_FUNC_INFO << "created...";
}

void ReadThread::run()
{
    qDebug() << Q_FUNC_INFO << "run start...";

    if (mItemType == NO_ITEM) {
        qWarning() << "did not specify requested item type";
        return;
    }

    if (fi == NULL) {
        fi = getOneEmptyFileItem();
    }

    int count = 0;

    // block here
    do {
        // buf = (FileItem*)util_shm_read(LOCAL_SHM_KEY, sizeof(FileItem));
        // if (buf == NULL) {
        //     qWarning() << "shm read failed";
        //     return;
        // } else {
        //     qDebug() << "buf addr:" << buf;
        // }
        if (mBuffer->rw_ctrl == 1) {    // ok to read
            dumpFileItem(mBuffer);
            mBuffer->rw_ctrl = 0;
            count ++;
        } else if (mBuffer->rw_ctrl == (char)0xff) {
            qDebug() << "it finished...";
            break;
        } else {
            QThread::msleep(WAIT_MSEC_LENGTH);
            //qDebug() << "wait...";
        }
        if (count > MAX_ITEM) {
            qDebug() << "max item reached...";
            break;
        }
    } while (true);

    qDebug() << Q_FUNC_INFO << "run finished...";
}
