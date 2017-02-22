#ifndef __COMMON_IDHASH_H__
#define __COMMON_IDHASH_H__

#include <QHash>
#include <QString>
#include <QDebug>

class IdHash
{
public:
    void dumpToFile(const QString& fn);

public:
    QHash<QString, int> mFile2IdHash;
    QHash<int, QString> mId2FileHash;
    QHash<QString, int> mFolder2IdHash;
    QHash<int, QString> mId2FolderHash;
};


#endif  // __COMMON_IDHASH_H__
