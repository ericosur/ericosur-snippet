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
    FileItem* buf = NULL;

    buf = (FileItem*)util_shm_read(LOCAL_SHM_KEY, sizeof(FileItem));
    do {
        if (buf == NULL) {
            qDebug() << "shm read failed";
            break;
        } else {
            if (buf->rw_ctrl == 1) {    // ok to read
                dumpFileItem(buf);
                buf->rw_ctrl = 0;
                count ++;
            } else if (buf->rw_ctrl == (char)0xff) {
                qDebug() << "it finished...";
                break;
            } else {
                QThread::msleep(WAIT_MSEC_LENGTH);
                qDebug() << "wait...";
            }
            if (count > MAX_ITEM) {
                qDebug() << "max item reached...";
                break;
            }
        }
    } while (true);

    qDebug() << Q_FUNC_INFO << "run finished...";
}

