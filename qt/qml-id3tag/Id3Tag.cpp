#include "Id3Tag.h"

#include <QDebug>
#include <QCryptographicHash>

//#include <iostream>
#include <stdio.h>

#include <tmap.h>
#include <tstring.h>
//#include <tpropertymap.h>
#include <mpegfile.h>
#include <id3v2frame.h>
#include <attachedpictureframe.h>
#include <mp4file.h>
#include <mp4tag.h>
#include <mp4coverart.h>

// TODO: mp4
// http://stackoverflow.com/questions/4752020/how-do-i-use-taglib-to-read-write-coverart-in-different-audio-formats

ID3TAG::ID3TAG(QObject *parent)
    : QObject(parent)
    , m_filename("")
    , m_title("")
    , m_artist("")
    , m_album("")
    , m_tmppath("/tmp")
    , m_cover()
{
}

ID3TAG::~ID3TAG()
{
}

QString ID3TAG::getFilename() const
{
    return m_filename;
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

QString ID3TAG::getHashFilename(const QString& fn)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(fn.toStdString().c_str(), fn.length());
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}

bool ID3TAG::getMP3Frame(TagLib::ID3v2::Tag* tag)
{
     // frames
     TagLib::ID3v2::FrameList frames;
     //look for picture frames
     frames = tag->frameListMap()["APIC"];
     if (frames.isEmpty()) {
         qDebug() << "frame is empty";
     } else {
         TagLib::ID3v2::FrameList::ConstIterator it = frames.begin();
         for(; it != frames.end() ; it++)
         {
             //cast Frame * to AttachedPictureFrame*
             TagLib::ID3v2::AttachedPictureFrame *pictureFrame =
                 static_cast<TagLib::ID3v2::AttachedPictureFrame *> (*it);

             //QImage coverQImg;
             //coverQImg.loadFromData((const uchar *) coverImg->picture().data(), coverImg->picture().size());
             //m_cover.loadFromData((const uchar *)pictureFrame->picture().data(), pictureFrame->picture().size());
             //http://stackoverflow.com/questions/20691414/qt-qml-send-qimage-from-c-to-qml-and-display-the-qimage-on-gui
             //Warning. format of picture assumed to be jpg. This may be false, for example it may be png.

             FILE *fout = fopen(m_coverpath.toStdString().c_str(), "wb");
             if (fout == NULL) {
                 qDebug() << "cannot output";
                 m_coverpath = "";
                 return false;
             }
             fwrite(pictureFrame->picture().data(), pictureFrame->picture().size(), 1, fout);
             fflush(fout);
             fclose(fout);
         }
     }
     return true;
}


bool ID3TAG::getMetaData(const QString& fn)
{
    qDebug() << "getMetaData(): " << fn;
    m_filename = fn;
    m_artist = "";
    m_title = "";
    m_album = "";

    QString str_hash = getHashFilename(fn);
    //qDebug() << "hash: " << str_hash;
    m_coverpath = m_tmppath + '/' + str_hash;
    qDebug() << "m_coverpath: " << m_coverpath;

    QRegExp rxmp3("\\.mp3$");
    QRegExp rxm4a("\\.m4a$");
    if (fn.contains(rxmp3)) {
        qDebug("mp3...");

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

        if (!getMP3Frame(tag)) {
            m_coverpath = "";
            return false;
        }

        return true;
    } else if (fn.contains(rxm4a)) {
        qDebug("m4a...");
        // refer to: http://stackoverflow.com/questions/6542465/c-taglib-cover-art-from-mpeg-4-files
        TagLib::MP4::File file(fn.toStdString().c_str());
        TagLib::MP4::Tag *tag = file.tag();
        m_artist = tag->artist().toCString(true);
        m_album = tag->album().toCString(true);
        m_title = tag->title().toCString(true);
        // get cover from m4a
        TagLib::MP4::ItemListMap itemsListMap = tag->itemListMap();
        TagLib::MP4::Item coverItem = itemsListMap["covr"];
        TagLib::MP4::CoverArtList coverArtList = coverItem.toCoverArtList();
        TagLib::MP4::CoverArt coverArt = coverArtList.front();

        FILE *fout = fopen(m_coverpath.toStdString().c_str(), "wb");
        if (fout == NULL) {
            qDebug() << "cannot output";
            m_coverpath = "";
            return false;
        }
        //image.loadFromData((const uchar *) coverArt.data().data(),coverArt.data().size());
        fwrite((const uchar *)coverArt.data().data(), coverArt.data().size(), 1, fout);
        fflush(fout);
        fclose(fout);
        return true;
    }
    return false;
}
