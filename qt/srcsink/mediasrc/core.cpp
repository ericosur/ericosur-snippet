#include "core.h"
#include "util.h"
#include "getcover.h"

#include <string.h>
#include <stdlib.h>
#include <QCoreApplication>
#include <QDebug>
#include <QThread>

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
        msgrx = new MsgRxThread();
    }

    if (travel == NULL) {
        travel = new TravelThread();
    }

    connect(msgrx, SIGNAL(sigReceived(const QString&)),
        this, SLOT(sltMessageReceived(const QString&)));
    connect(this, SIGNAL(sigQuitApp()), qApp, SLOT(quit()));

    if (msgrx != NULL) {
        msgrx->start();
    }

    connect(this, SIGNAL(sigStart()), this, SLOT(sltStart()));
    connect(this, SIGNAL(sigGetfolder()), this, SLOT(sltGetfolder()));
    connect(this, SIGNAL(sigNext()), this, SLOT(sltNext()));

    check_shm();
}

void Core::sltMessageReceived(const QString& msg)
{
    qDebug() << Q_FUNC_INFO << "msg:" << msg;
    if (msg == "foo") {
        qDebug() << "IPC notification: foo starts...";
    } else if (msg == "quit") {
        qDebug() << "quit command received...";
        emit sigQuitApp();
    } else if (msg == "start") {
        qDebug() << "received start command...";
        emit sigStart();
    } else if (msg == "getfolder") {
        qDebug() << "request getfolder...";
        emit sigGetfolder();
    }
}

void Core::sltWaitFinished()
{
    qDebug() << "foo is NOT running...";
}

void Core::test()
{
    qDebug() << Q_FUNC_INFO;
    startTravel();
}

void Core::simple_test_shm_read_write()
{
    const int BUFFER_SIZE = 1024;
    byte* buf = (byte*) malloc(BUFFER_SIZE);

    memset(buf, 0xcc, BUFFER_SIZE);
    if (util_shm_write(LOCAL_SHM_KEY, BUFFER_SIZE, buf) < 0) {
        qWarning() << "shm write failed";
        //return;
    }
    memset(buf, 0xff, BUFFER_SIZE);
    delete buf;
    emit sigNext();
}

void Core::sltNext()
{
    qDebug() << Q_FUNC_INFO;
    const int BUFFER_SIZE = 1024;
    byte* buf = NULL;

    buf = (byte*)util_shm_read(LOCAL_SHM_KEY, BUFFER_SIZE);
    if (buf == (void*)-1) {
        qDebug() << "shm read failed";
        return;
    }
    for (unsigned int i = 0; i < BUFFER_SIZE; i++) {
        if (buf[i] != 0xcc) {
            qWarning() << "incorrect!";
            return;
        }
    }
    qDebug() << "ok";
}

void Core::startTravel()
{
    QString mediapath = qgetenv("MEDIASRC");
    if (mediapath == "") {
#ifdef __arm__
        mediapath = "/media/usb/storage";
#else
        QString homepath = qgetenv("HOME");
        if (homepath == "") {
            homepath = "/home/rasmus";
        }
        mediapath = homepath + "/Music";
#endif  // __arm__
    }

    qWarning() << "setStartPath():" << mediapath;
    travel->setStartPath(mediapath);
    travel->start();
    connect(travel, SIGNAL(finished()), this, SLOT(sltTravelFinished()));
}

void Core::sltTravelFinished()
{
    qDebug() << Q_FUNC_INFO;
    filelist = travel->getFilelist();
    folderlist = travel->getPathlist();
    qDebug() << "size of filelist:" << filelist.size();
}

void Core::sltStart()
{
    SendItemToShm(AUDIO_ITEM);
}

void Core::sltGetfolder()
{
    SendItemToShm(FOLDER_ITEM);
}

void Core::SendItemToShm(ItemType it)
{
    qDebug() << Q_FUNC_INFO;

    if (it == AUDIO_ITEM && filelist.size() <= 0) {
        qWarning() << "file list empty...";
        return;
    }
    if (it == FOLDER_ITEM && folderlist.size() <= 0) {
        qWarning() << "folder list is empty...";
        return;
    }

    int cnt = 1;
    FileItem* fi;

    do {
        if (it == AUDIO_ITEM) {
            fi = fetchOneItem();
        } else if (it == FOLDER_ITEM) {
            fi = fetchOneFolderItem();
        } else {
            fi = getOneEmptyFileItem();
        }
        memcpy(mBuffer, fi, sizeof(FileItem));
        delete fi;

        // block here
        int wait_cnt = 0;
        while (true) {
            if ( mBuffer->rw_ctrl != 0 ) {
                //qDebug() << "cannot write..., and wait...";
            } else {
                //qDebug() << "can write...";
                break;
            }
            // leave inner wait loop
            if ( wait_cnt > MAX_RETRY_TIMES ) {
                qDebug() << "timeout...";
                break;
            }

            QThread::msleep(WAIT_MSEC_LENGTH);
            //qDebug() << "wait...";
            wait_cnt ++;
        }
        // leave outer loop
        if (wait_cnt > MAX_RETRY_TIMES) {
            break;
        }

        qDebug() << "cnt:" << cnt;
        cnt ++;
        if (cnt > MAX_ITEM) {
            qDebug() << qApp->applicationName() << "reach max items...";
            break;
        }
    } while (true);

    // mark as finished
    mBuffer->rw_ctrl = (char)0xff;

    qDebug() << Q_FUNC_INFO << "finished transmitting audio filelist";
    //emit sigQuitApp();
}

FileItem* Core::fetchOneItem()
{
    static int _id = 0;

    FileItem* fi = getOneEmptyFileItem();
    QString _name = "no name";
    QString _artist = "unknown artist";
    QString _album = "unknown album";

    if (filelist.size() > _id + 1) {
        if ( GetCover::getInstance()->getcover(filelist[_id]) ) {
            _name = GetCover::getInstance()->getTitle();
            _artist = GetCover::getInstance()->getArtist();
            _album = GetCover::getInstance()->getAlbum();
            fillFileItem(fi, _name, _artist, _album);
        }
        fi->id = _id;
        fi->rw_ctrl = 1;
    }

    //dumpFileItem(fi);
    _id ++;

    return fi;
}

FileItem* Core::fetchOneFolderItem()
{
    static int _id = 0;

    FileItem* fi = getOneEmptyFileItem();

    if (folderlist.size() > _id + 1) {
        QString _name = folderlist[_id];
        fillFileItem(fi, _name, "", "");
        fi->id = _id;
        fi->rw_ctrl = 1;
    }

    //dumpFileItem(fi);
    _id ++;

    return fi;
}

void Core::check_shm()
{
    // fill all zero into 0xff
    FileItem _fi;
    memset(&_fi, 0, sizeof(FileItem));
    if (util_shm_write(LOCAL_SHM_KEY, sizeof(FileItem), &_fi) < 0) {
        qWarning() << "shm write failed";
    }
    FileItem *buf = (FileItem*)util_shm_read(LOCAL_SHM_KEY, sizeof(FileItem));
    if (buf == NULL) {
        qWarning() << "failed to read shm...";
        return;
    }
    mBuffer = buf;
    QString sum1 = md5sum((char*)&_fi, sizeof(FileItem));
    QString sum2 = md5sum((char*)buf, sizeof(FileItem));
    if (sum1 != sum2) {
        qWarning() << "mismatch md5sum!!!";
    } else {
        qDebug() << "md5sum:" << sum1;
    }
}
