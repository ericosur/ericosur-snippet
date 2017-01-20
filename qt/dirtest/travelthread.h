#ifndef __TRAVEL_THREAD_H__
#define __TRAVEL_THREAD_H__

#include <QObject>
#include <QThread>
#include <QDir>
#include <QStringList>
#include <QHash>

class TravelThread : public QThread
{
    Q_OBJECT

public:
    TravelThread();
    void run();

    void setStartPath(const QString& startpath) {
        mStartpath = startpath;
    }
    QStringList getFilelist() {
        return mFilelist;
    }
    QStringList getPathlist() {
        return mPathlist;
    }
    void dumpFolderHash();
    void clearFolderHash();

signals:

protected:
    void init_filter();
    bool isInBlacklist(const QString& name);
    void travel_dir(const QString& path);

private:
    QString mStartpath = "";
    QStringList mFilter;
    QStringList mFilelist;  // list with all folders/files
    QStringList mPathlist;  // list with all folders

    // key is path name, value is a string list
    QHash<QString, QStringList*> mFolderHash;
};

#endif // __TRAVEL_THREAD_H__
