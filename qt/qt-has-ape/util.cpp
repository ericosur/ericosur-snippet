/**
 * \file: util.cpp
 * \brief: functions to ultilize taglib
 */
#include "util.h"
#include <QDebug>

#include <taglib/taglib.h>
#include <taglib/tmap.h>
#include <taglib/tstring.h>
//#include <taglib/id3v1tag.h>
#include <taglib/id3v2tag.h>
#include <taglib/mpegfile.h>
//#include <taglib/id3v2frame.h>
#include <taglib/fileref.h>
#include <taglib/tag.h>
#include <taglib/tpropertymap.h>

bool hasAPETag(const QString& fn)
{
    TagLib::MPEG::File file(fn.toStdString().c_str());
    if (!file.isValid()) {
        return false;
    }
    return file.hasAPETag();
}


bool getTags(const QString& fn)
{
    TagLib::FileRef f(fn.toUtf8());

    if (!f.isNull() && f.tag()) {

        TagLib::Tag *tag = f.tag();
        QString title = tag->title().toCString(true);
        QString artist = tag->artist().toCString(true);
        QString album = tag->album().toCString(true);
        QString year = QString::number(tag->year());
        QString comment = tag->comment().toCString(true);
        QString track = QString::number(tag->track());
        QString genre = tag->genre().toCString(true);

        qDebug() << "-- TAG (basic) --";
        if (title.length())  qDebug() << "title:" << title;
        if (artist.length()) qDebug() << "artist:" << artist;
        if (album.length()) qDebug() << "album:" << album;
        if (year.length()) qDebug() << "year:" << year;
        if (comment.length()) qDebug() << "comment:" << comment;
        if (track.length()) qDebug() << "track:" << track;
        if (genre.length()) qDebug() << "genre:" << genre;

        TagLib::PropertyMap tags = f.file()->properties();
        qDebug() << "-- TAG (properties) --";
        for(TagLib::PropertyMap::ConstIterator i = tags.begin(); i != tags.end(); ++i) {
            for(TagLib::StringList::ConstIterator j = i->second.begin(); j != i->second.end(); ++j) {
                QString iname = i->first.toCString(true);
                QString jname = (*j).toCString(true);
                qDebug() << iname << "-" << jname;
            }
        }
        return true;
    }

    return false;
}
