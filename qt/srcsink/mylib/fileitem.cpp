#include "fileitem.h"


// caller should release fileitem after used it
FileItem* getOneEmptyFileItem()
{
    FileItem* fi = new FileItem;
    fi->id = 0;
    memset(fi->name, 0, MAX_FILEITEM_NAME);
    memset(fi->artist, 0, MAX_FILEITEM_ARTIST);
    memset(fi->album, 0, MAX_FILEITEM_ALBUM);
    fi->length = 0;
    fi->rw_ctrl = 0;
    return fi;
}

void copy_qstring_to_char_array(void* buf, const int MAX_SIZE, const QString& qstr)
{
    QByteArray ba = qstr.toUtf8();
    memcpy(buf, ba.data(), qMin(MAX_SIZE, ba.size()));
}

void fillFileItem(FileItem* fi, const QString& name, const QString& artist, const QString& album)
{
    copy_qstring_to_char_array(fi->name, MAX_FILEITEM_NAME, name);
    copy_qstring_to_char_array(fi->artist, MAX_FILEITEM_ARTIST, artist);
    copy_qstring_to_char_array(fi->album, MAX_FILEITEM_ALBUM, album);
}

void dumpFileItem(const FileItem* _fi)
{
    qDebug() << "fileitem, id:" << _fi->id << endl
        << "name:" << _fi->name << endl
        << "artist:" << _fi->artist << endl
        << "album:" << _fi->album << endl
        << "rw_ctrl:" << (_fi->rw_ctrl ? "true" : "false");
}
