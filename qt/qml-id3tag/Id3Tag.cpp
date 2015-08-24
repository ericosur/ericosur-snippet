#include "Id3Tag.h"

#include <QDebug>
#include <QCryptographicHash>

//#include <iostream>
#include <stdio.h>

#include <tmap.h>
#include <tstring.h>
#include <tpropertymap.h>
#include <mpegfile.h>
#include <id3v2frame.h>
#include <attachedpictureframe.h>


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

bool ID3TAG::getFrame(TagLib::ID3v2::Tag* tag)
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

             QCryptographicHash hash( QCryptographicHash::Md5 );
             hash.addData(m_filename.toStdString().c_str(), m_filename.length());
             QString str_hash = hash.result().toHex().data();
             //qDebug() << "hash: " << str_hash;
             m_coverpath = m_tmppath + '/' + str_hash;
             //qDebug() << "m_coverpath: " << m_coverpath;

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

    getFrame(tag);
    //TagLib::PropertyMap pm(tag->properties());
    //TagLib::String s = pm.toString();
    // cout << s.toCString(true) << endl;

    return true;

    //return true;
}
