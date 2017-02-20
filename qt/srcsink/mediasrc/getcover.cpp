/**
 * \file getcover.cpp
 * \brief implementation for class GetCover
 */
#include "getcover.h"

#include <QDebug>
#include <QRegExp>
#include <QFile>
#include <QCryptographicHash>

// taglib headers {
#include <taglib/taglib.h>
#include <taglib/tmap.h>
#include <taglib/tstring.h>
//#include <taglib/tpropertymap.h>
#include <taglib/id3v1tag.h>
#include <taglib/id3v2tag.h>
#include <taglib/mpegfile.h>
#include <taglib/id3v2frame.h>
#include <taglib/attachedpictureframe.h>
#include <taglib/mp4file.h>
#include <taglib/mp4tag.h>
#include <taglib/mp4coverart.h>
#include <taglib/flacfile.h>
// taglib headers }

#define DEFAULT_BUFFER_SIZE     (512)
char buffer[DEFAULT_BUFFER_SIZE];

GetCover* GetCover::_instance = NULL;

GetCover* GetCover::getInstance()
{
    if (_instance == NULL) {
        _instance = new GetCover();
    }
    return _instance;
}
GetCover::GetCover()
{
}

QString GetCover::md5sum(const char* buf, int size)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(buf, size);
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}

QString GetCover::get_hash_filename(const QString& fn)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(fn.toStdString().c_str(), fn.length());
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}

bool GetCover::getcover(const QString& fn)
{
    QFile fileobj(fn);
    //fileobj.setFileName(tbfn);
    if (!fileobj.exists()) {
        qDebug() << fn << "not exists";
        return false;
    }
    m_title = "";
    m_artist = "";
    m_album = "";
    m_length = 0;

    if (fn.contains(QRegExp("\\.mp3$"))) {
        //qDebug() << "call extract_cover_from_mp3()...";
        if ( !extract_info_from_mp3(fn) ) {
            qWarning() << "can't get info from" << fn;
        }
        extract_length_from_mp3(fn);  // test

    } else if (fn.contains(QRegExp("\\.m4a$"))) {
        //qDebug() << "call extract_cover_from_mp4()...";
        if ( !extract_info_from_mp4(fn) ) {
            qWarning() << "can't get info from" << fn;
        }
        extract_length_from_mp4(fn);

    } else if (fn.contains(QRegExp("\\.flac$"))) {
        qDebug() << "flac...";
        if ( !extract_info_from_flac(fn) ) {
            qWarning() << "can't get info from" << fn;
        }
        extract_length_from_flac(fn);
    }
    // TODO: add function to extract flac album
    // http://stackoverflow.com/questions/7119073/c-taglib-cover-art-from-flac-and-asf-files
    return true;
}

bool GetCover::isFileExisted(const QString& fn)
{
    QFile fileobj(fn);
    return fileobj.exists();
}

void GetCover::show_aat(const QString& artist, const QString& album, const QString& title)
{
    qDebug() << "metadata ==========>>>" << endl
        << "artist:" << artist << endl
        << "album:" << album << endl
        << "title:" << title;
}

bool GetCover::extract_info_from_mp3(const QString& fn)
{
    TagLib::MPEG::File file(fn.toStdString().c_str());
    if (!file.isValid()) {
        //qDebug() << "file is invalid";
        return false;
    }
    if (file.hasID3v2Tag()) {
        //qDebug() << "id3v2 tag...";
        TagLib::ID3v2::Tag *tag = file.ID3v2Tag();
        m_artist = tag->artist().toCString(true);
        m_album = tag->album().toCString(true);
        m_title = tag->title().toCString(true);
        //show_aat(_artist, _album, _title);
        return true;
    }
    return false;
}

bool GetCover::extract_info_from_mp4(const QString& fn)
{
    TagLib::MP4::File file(fn.toStdString().c_str());
    TagLib::MP4::Tag *tag = file.tag();
    if (tag == NULL) {
        //qDebug() << "tag is null";
        return false;
    }
    m_artist = tag->artist().toCString(true);
    m_album = tag->album().toCString(true);
    m_title = tag->title().toCString(true);
    //show_aat(_artist, _album, _title);
    return true;
}

bool GetCover::extract_info_from_flac(const QString& fn)
{
    TagLib::FLAC::File file(fn.toStdString().c_str());
    TagLib::Tag *tag = file.tag();
    if (tag != NULL) {
        m_artist = tag->artist().toCString(true);
        m_album = tag->album().toCString(true);
        m_title = tag->title().toCString(true);
        //show_aat(_artist, _album, _title);
        return true;
    } else if (file.hasID3v2Tag()) {
        TagLib::ID3v2::Tag *tag = file.ID3v2Tag();
        m_artist = tag->artist().toCString(true);
        m_album = tag->album().toCString(true);
        m_title = tag->title().toCString(true);
        //show_aat(_artist, _album, _title);
        return true;
    }
    return false;
}

bool GetCover::extract_length_from_mp3(const QString& fn)
{
    TagLib::MPEG::File file(fn.toStdString().c_str());
    TagLib::MPEG::Properties p(&file);

    qDebug() << "mp3 len(fn):" << p.length();
    m_length = p.length();
    return true;
}

bool GetCover::extract_length_from_mp4(const QString& fn)
{
    TagLib::MP4::File file(fn.toStdString().c_str());

    qDebug() << "m4a len(fn):" << file.audioProperties()->length();
    m_length = file.audioProperties()->length();
    return true;
}

bool GetCover::extract_length_from_flac(const QString& fn)
{
    qDebug() << Q_FUNC_INFO;

    TagLib::FLAC::File file(fn.toStdString().c_str());
    TagLib::FLAC::Properties p(&file);

    qDebug() << "flac len(fn):" << p.length();
    m_length = p.length();
    return true;
}
