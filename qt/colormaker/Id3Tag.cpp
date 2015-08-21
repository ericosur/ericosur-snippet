#include "Id3Tag.h"

#include <QDebug>
//#include <stdio.h>
//#include <iostream>

#include <tmap.h>
#include <tstring.h>
#include <tpropertymap.h>
#include <mpegfile.h>
#include <id3v2tag.h>
#include <id3v2frame.h>
#include <attachedpictureframe.h>

ID3TAG::ID3TAG(QObject *parent)
    : QObject(parent)
    , m_filename("")
    , m_title("")
    , m_artist("")
    , m_album("")
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

    //TagLib::PropertyMap pm(tag->properties());
    //TagLib::String s = pm.toString();

    m_artist = tag->artist().toCString(true);
    m_album = tag->album().toCString(true);
    m_title = tag->title().toCString(true);

    return true;
/*
     cout << tag->title().toCString(true) << endl
         << tag->album().toCString(true) << endl
         << tag->artist().toCString(true) << endl
         << s.toCString(true) << endl;

     // frames
     TagLib::ID3v2::FrameList frames;
     //look for picture frames
     frames = tag->frameListMap()["APIC"];
     if (frames.isEmpty()) {
         cout << "frmaes is empty" << endl;
     } else {
         TagLib::ID3v2::FrameList::ConstIterator it = frames.begin();
         for(; it != frames.end() ; it++)
         {
             //cast Frame * to AttachedPictureFrame*
             TagLib::ID3v2::AttachedPictureFrame *pictureFrame =
                 static_cast<TagLib::ID3v2::AttachedPictureFrame *> (*it);

             //Warning. format of picture assumed to be jpg. This may be false, for example it may be png.
             FILE *fout = fopen(PICNAME, "wb");
             if (fout == NULL) {
                 return -1;
             }
             cout << "processing the file "<< FNAME << endl;
             fwrite(pictureFrame->picture().data(), pictureFrame->picture().size(), 1, fout);
             fclose(fout);
             cout << "The picture has been written to " << PICNAME << endl;
             cout << "Remember that the file type .jpg is just assumed for simplicity" << endl;
         }
     }

 */

    //return true;
}
