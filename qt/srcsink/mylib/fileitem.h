#ifndef __FILE_ITEM_H__
#define __FILE_ITEM_H__

#include <string.h>
#include <QString>
#include <QDebug>

#define MAX_FILEITEM_NAME       512
#define MAX_FILEITEM_ARTIST     128
#define MAX_FILEITEM_ALBUM      128

// define one single file item
typedef struct FileItem
{
    unsigned int id;
    char name[MAX_FILEITEM_NAME];
    char artist[MAX_FILEITEM_ARTIST];
    char album[MAX_FILEITEM_ALBUM];
    unsigned int length;
    char rw_ctrl;
} FileItem;

FileItem* getOneEmptyFileItem();
void fillFileItem(FileItem* fi, const QString& name, const QString& artist, const QString& album);
void dumpFileItem(const FileItem* _fi);

#endif // __FILE_ITEM_H__