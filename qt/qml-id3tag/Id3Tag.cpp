#include "Id3Tag.h"

#include <QDebug>
#include <QCryptographicHash>

//#include <iostream>
#include <stdio.h>

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

#define MY_GET_FRAME

// TODO: mp4
// http://stackoverflow.com/questions/4752020/how-do-i-use-taglib-to-read-write-coverart-in-different-audio-formats

QCache<QString, MyId3Data> m_cache;

ID3TAG::ID3TAG(QObject *parent)
    : QObject(parent)
    , m_filename("")
    , m_title("")
    , m_artist("")
    , m_album("")
    , m_tmppath("/tmp")		
{
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
    //getMetaData(s);
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

QString ID3TAG::getCoverPath() const
{
    return m_coverpath;
}

QString ID3TAG::gettmppath() const
{
    return m_tmppath;
}

void ID3TAG::settmppath(const QString& p)
{
    m_tmppath = p;
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

QImage ID3TAG::getMp3Cover(const QString &fn)
{
    return QImage(NULL);
/*
    qDebug("getMp3Cover:" );
    qDebug(fn.toStdString().c_str());
    TagLib::MPEG::File file(fn.toStdString().c_str());
    if (!file.isValid()) {
        qDebug("getMp3Cover: file is invalid");
        return QImage(NULL);
    }
    TagLib::ID3v2::Tag *tag = file.ID3v2Tag(true);
    if (tag == NULL) {
        qDebug("getMp3Cover: null tag");
        return QImage(NULL);
    }
    // frames
    TagLib::ID3v2::FrameList frames;
    //look for picture frames
    frames = tag->frameListMap()["APIC"];
    if (frames.isEmpty()) {
        qDebug() << "getMp3Cover: frame is empty";
        return QImage(NULL);
    } else {
        TagLib::ID3v2::FrameList::ConstIterator it = frames.begin();
        //for(; it != frames.end() ; it++)  // only take one frame
        {
            //cast Frame * to AttachedPictureFrame*
            TagLib::ID3v2::AttachedPictureFrame *pictureFrame =
                static_cast<TagLib::ID3v2::AttachedPictureFrame *> (*it);

            if (!m_cover_curr.isNull())
                m_cover_prev = m_cover_curr;
            //http://stackoverflow.com/questions/20691414/qt-qml-send-qimage-from-c-to-qml-and-display-the-qimage-on-gui
            //Warning. format of picture assumed to be jpg. This may be false, for example it may be png.
            m_cover_curr.loadFromData((const uchar *) pictureFrame->picture().data(), pictureFrame->picture().size());
        }
    }
    return m_cover_curr;
*/
}

QImage ID3TAG::getM4ACover(const QString &fn)
{
    return QImage(NULL);
/*
    // refer to: http://stackoverflow.com/questions/6542465/c-taglib-cover-art-from-mpeg-4-files
    TagLib::MP4::File file(fn.toStdString().c_str());
    TagLib::MP4::Tag *tag = file.tag();
    if (tag == NULL) {
        qDebug("getM4ACover: tag is null");
        return QImage(NULL);
    }
    // get cover from m4a
    TagLib::MP4::ItemListMap itemsListMap = tag->itemListMap();
    TagLib::MP4::Item coverItem = itemsListMap["covr"];
    TagLib::MP4::CoverArtList coverArtList = coverItem.toCoverArtList();
    TagLib::MP4::CoverArt coverArt = coverArtList.front();

    if (!m_cover_curr.isNull()) {
        m_cover_prev = m_cover_curr;
    }
    m_cover_curr.loadFromData((const uchar *)coverArt.data().data(), coverArt.data().size());
    return m_cover_curr;
*/
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
            m_coverpath = "";
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
        qDebug("try to load cover...");
        // get cover from m4a
        TagLib::MP4::ItemListMap itemsListMap = tag->itemListMap();
        TagLib::MP4::Item coverItem = itemsListMap["covr"];
        TagLib::MP4::CoverArtList coverArtList = coverItem.toCoverArtList();
        TagLib::MP4::CoverArt coverArt = coverArtList.front();

        QImage _img;
        _img.loadFromData((const uchar *)coverArt.data().data(), coverArt.data().size());
        id3->set_img(_img);
        qDebug() << _img;
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
    m_coverpath = m_tmppath + '/' + str_hash;
    //qDebug() << "m_coverpath: " << m_coverpath;

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

    //if (id3)
    //    delete id3;
}
