#include "Id3Tag.h"

#include <QDebug>
#include <QCryptographicHash>

//#include <iostream>
//#include <stdio.h>

// taglib headers {
#include <taglib.h>
#include <tmap.h>
#include <tstring.h>
//#include <tpropertymap.h>
#include <id3v2tag.h>
#include <mpegfile.h>
#include <id3v2frame.h>
#include <attachedpictureframe.h>
#include <mp4file.h>
#include <mp4tag.h>
#include <mp4coverart.h>
// taglib headers }

// undef this to disable cover extraction actions
#define MY_GET_FRAME

// how to extract cover from m4a
// http://stackoverflow.com/questions/4752020/how-do-i-use-taglib-to-read-write-coverart-in-different-audio-formats

// yeah it's global
QCache<QString, MyId3Data> m_cache;

ID3TAG::ID3TAG(QObject *parent)
    : QObject(parent)
    , m_filename("")
    , m_title("")
    , m_artist("")
    , m_album("")
{
    m_cover = QImage(NULL);
}

ID3TAG::~ID3TAG()
{
}

QString ID3TAG::getFilename() const
{
    return m_filename;
}

void ID3TAG::setFilename(const QString &s)
{
    m_filename = s;
}

QString ID3TAG::getTitle() const
{
    return m_title;
}

QString ID3TAG::getArtist() const
{
    return m_artist;
}

QString ID3TAG::getAlbum() const
{
    return m_album;
}

QImage ID3TAG::getCover() const
{
    return m_cover;
}

QString ID3TAG::getHashFilename(const QString& fn)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(fn.toStdString().c_str(), fn.length());
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}

bool ID3TAG::getdata(MyId3Data* id3)
{
    QRegExp rxmp3("\\.mp3$");
    QRegExp rxm4a("\\.m4a$");
    QString fn = m_filename;

    if (fn.contains(rxmp3)) {
        qDebug() << "getdata() mp3, fn: " << fn;

        TagLib::MPEG::File file(fn.toStdString().c_str());
        if (!file.isValid()) {
            qDebug("taglib: file is invalid");
            return false;
        }
        TagLib::ID3v2::Tag *tag = file.ID3v2Tag(true);
        if (tag == NULL) {
            qDebug("taglib: null tag");
            return false;
        }

        m_artist = tag->artist().toCString(true);
        m_album = tag->album().toCString(true);
        m_title = tag->title().toCString(true);
        id3->set_artist(m_artist);
        id3->set_album(m_album);
        id3->set_title(m_title);
#ifdef MY_GET_FRAME
        // frames
        TagLib::ID3v2::FrameList frames;
        //look for picture frames
        frames = tag->frameListMap()["APIC"];
        if (frames.isEmpty()) {
            qDebug() << "getMP3Frame: frame is empty";
            id3->set_img(QImage(NULL));
        } else {
            TagLib::ID3v2::FrameList::ConstIterator it = frames.begin();
            //for(; it != frames.end() ; it++)
            {
                //cast Frame * to AttachedPictureFrame*
                TagLib::ID3v2::AttachedPictureFrame *pf = static_cast<TagLib::ID3v2::AttachedPictureFrame *> (*it);
                QImage _img;
                _img.loadFromData((const uchar*)pf->picture().data(), pf->picture().size());
                id3->set_img(_img);
            }
        }
#endif
        return true;
    } else if (fn.contains(rxm4a)) {
        qDebug("getdata() m4a...");
        // refer to: http://stackoverflow.com/questions/6542465/c-taglib-cover-art-from-mpeg-4-files
        TagLib::MP4::File file(fn.toStdString().c_str());
        TagLib::MP4::Tag *tag = file.tag();
        m_artist = tag->artist().toCString(true);
        m_album = tag->album().toCString(true);
        m_title = tag->title().toCString(true);
        id3->set_artist(m_artist);
        id3->set_album(m_album);
        id3->set_title(m_title);
#ifdef MY_GET_FRAME
        qDebug("try to load m4a cover...");
        // get cover from m4a
        TagLib::MP4::ItemListMap itemsListMap = tag->itemListMap();
        TagLib::MP4::Item coverItem = itemsListMap["covr"];
        TagLib::MP4::CoverArtList coverArtList = coverItem.toCoverArtList();
        TagLib::MP4::CoverArt coverArt = coverArtList.front();

        QImage _img;
        _img.loadFromData((const uchar *)coverArt.data().data(), coverArt.data().size());
        id3->set_img(_img);
        //qDebug() << _img;
#endif
        return true;
    }
    return false;
}

bool ID3TAG::getMetaData(const QString& fn)
{
    //qDebug() << "getMetaData(): " << fn;
    m_filename = fn;
    m_artist = "";
    m_title = "";
    m_album = "";

    QString str_hash = getHashFilename(fn);
    //qDebug() << "hash: " << str_hash;

    MyId3Data *id3 = NULL;
    if ( m_cache.contains(fn) ) {
        // cache hit
        qDebug() << "cache hit for: " << fn;
        id3 = m_cache.object(fn);
        if (id3 == 0) {
            return false;
        } else {
            m_artist = id3->get_artist();
            m_title = id3->get_title();
            m_album = id3->get_album();
            return true;
        }
    } else {
        // not in cache...
        // try to load it from file
        qDebug() << "cache not hit for: " << fn;
        id3 = new MyId3Data;
        id3->set_fn(m_filename);
        id3->set_str(str_hash);
        if ( getdata(id3) ) {
            if ( m_cache.insert(fn, id3) ) {
                qDebug() << "insert data to cache";
                return true;
            } else {
                qDebug() << "cache insert failed";
                return false;
            }
        } else {
            return false;
        }
    }
    // no need to delete *id3, let QCache handle it
}
