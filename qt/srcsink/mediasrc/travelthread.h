#ifndef __TRAVEL_THREAD_H__
#define __TRAVEL_THREAD_H__

#include <QObject>
#include <QThread>
#include <QDir>
#include <QStringList>
#include <QHash>

typedef QHash<QString, QStringList*> FolderHashList;

class TravelThread : public QThread
{
    Q_OBJECT

    Q_PROPERTY(QStringList filelist READ filelist WRITE setFilelist NOTIFY filelistChanged)

public:
    QStringList filelist() const {
        return mFilelist;
    }
    void setFilelist(const QStringList& sl) {
        mFilelist = sl;
        emit filelistChanged();
    }

public:
    TravelThread();
    void run();

    void setStartPath(const QString& startpath) {
        mStartpath = startpath;
    }
    QStringList getFilelist() const {
        return mFilelist;
    }
    QStringList getPathlist() {
        return mPathlist;
    }

    FolderHashList getFolderhash() {
        return mFolderHash;
    }

    void dumpFolderHash();
    void clearFolderHash();
    void report_status();

signals:
    void filelistChanged();

protected:
    void init_filter();
    bool isInBlacklist(const QString& name);
    void travel_dir(const QString& path);

private:
    QString mStartpath = "";
    QStringList mFilter;
    QStringList mAudioFilter;
    QStringList mFilelist;  // list with all folders/files
    QStringList mPathlist;  // list with all folders


    // key is path name, value is a string list
    FolderHashList mFolderHash;
};

#endif // __TRAVEL_THREAD_H__
