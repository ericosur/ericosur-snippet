#include "readthread.h"
#include "flowctrl.h"

#define WAIT_MSEC_LENGTH    (500)

ReadThread::ReadThread()
{
    qDebug() << Q_FUNC_INFO << "created...";
}

void ReadThread::run()
{
    qDebug() << Q_FUNC_INFO << "run start...";

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
            } else if (buf->rw_ctrl == -1) {
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

