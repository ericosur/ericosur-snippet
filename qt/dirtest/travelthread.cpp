#include <QDebug>
#include <QThread>
#include <QRegExp>

#include "travelthread.h"


TravelThread::TravelThread()
{
    qDebug() << Q_FUNC_INFO << "created";

    mFilter.clear();
    mFilelist.clear();
    mPathlist.clear();

    init_filter();
}

void TravelThread::init_filter()
{
    mFilter << "*.mp3" << "*.wav" << "*.aac" << "*.m4a"
        << "*.wma" << "*.flac" << "*.ogg" << "*.ape"
        << "*.mp4" << "*.wmv" << "*.mov" << "*.flv"
        << "*.mkv" << "*.avi" << "*.mpg" << "*.mpeg"
        << "*.png" << "*.jpg" << "*.jpeg" << "*.bmp"
        << "*.jpe" << "*.mid" << "*.amr";
}

bool TravelThread::isInBlacklist(const QString& name)
{
    if (name == "System Volume Information"
        || name == "lost+found"
        || name.contains(QRegExp("FOUND\\.\\d+"))
        || name == "$RECYCLE.BIN"
        || name == "Recycled"
    ) {
        return true;
    }
    return false;
}

void TravelThread::run()
{
    qDebug() << Q_FUNC_INFO << "running...";

    travel_dir(mStartpath);
    //mPathlist = collect_path(mFilelist);

    qDebug() << Q_FUNC_INFO << "finished...";
}

void TravelThread::travel_dir(const QString& path)
{
    QDir dir(path);

    //qDebug() << /* Q_FUNC_INFO << */ "path:" << path;
    if (isInBlacklist(dir.dirName())) {
        qDebug() << "skip:" << path;
        return;
    }

    QStringList *tmp = NULL;
    foreach (QString file, dir.entryList(mFilter, QDir::Files | QDir::NoSymLinks)) {
        if ( !mFolderHash.contains(path) ) {
            tmp = new QStringList;
            mFolderHash.insert(path, tmp);
        }
        QFileInfo _info(dir, file);
        mFilelist << _info.filePath();
        (*tmp) << _info.filePath();
    }


    foreach (QString subDir, dir.entryList(QDir::Dirs
                                           | QDir::NoDotAndDotDot | QDir::NoSymLinks)) {
        travel_dir(path + QDir::separator() + subDir);
    }

    mPathlist = mFolderHash.keys();
}

void TravelThread::dumpFolderHash()
{
    qDebug() << Q_FUNC_INFO << "mFolderHash.size():" << mFolderHash.size();

    int count = 0;
    foreach (QString key, mFolderHash.keys()) {
        //qDebug() << "key:" << key;
        if (!QDir(key).exists()) {
            qDebug() << "path not found:" << key;
        }
        count += mFolderHash[key]->size();
    }
    if (mFilelist.size() != count) {
        qWarning() << "mismatched size!" << count;
    }
}

void TravelThread::clearFolderHash()
{
    foreach (QString key, mFolderHash.keys()) {
        delete mFolderHash[key];
    }
}
