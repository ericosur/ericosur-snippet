/**
 * \file getcover.cpp
 * \brief implementation for class GetCover
 */
#include "getcover.h"
#include "yoseshm.h"

#include <QImage>
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

/// default will output tb
bool GetCover::m_writetb = true;
bool GetCover::m_followtype = false;
bool GetCover::m_resizetb = false;

GetCover::GetCover()
{
}

void GetCover::save_hash(const QString& hash)
{
    qDebug() << Q_FUNC_INFO << "=>" << hash;
    QByteArray arr = hash.toLocal8Bit();
    qDebug() << arr.size() << arr.constData();
    myShm::saveToShm(arr.size(), (const char*)arr.constData());
}
QString GetCover::load_hash()
{
    QString ret = "";

    uint32_t size = 0;
    myShm::readFromShm(size, buffer);
    QByteArray arr((char*)buffer, (int)size);
    ret.append(arr);
    return ret;
}
QString GetCover::get_thumb_name(const QString& hstr)
{
    QString res = QString("/tmp/") + hstr + QString(".png");
    return res;
}
QString GetCover::md5sum(const char* buffer, int size)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(buffer, size);
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

bool GetCover::getcover(const QString& fn, QString& tbfn)
{
    QFile fileobj(fn);
    //fileobj.setFileName(tbfn);
    if (!fileobj.exists()) {
        qDebug() << fn << "not exists";
        return false;
    }

    bool ret = false;
    if (fn.contains(QRegExp("\\.mp3$"))) {
        //qDebug() << "call extract_cover_from_mp3()...";
        if ( !extract_info_from_mp3(fn) ) {
            qWarning() << "can't get info from" << fn;
        }
        extract_length_from_mp3(fn);  // test
        ret = extract_cover_from_mp3(fn, tbfn);
    } else if (fn.contains(QRegExp("\\.m4a$"))) {
        //qDebug() << "call extract_cover_from_mp4()...";
        if ( !extract_info_from_mp4(fn) ) {
            qWarning() << "can't get info from" << fn;
        }
        extract_length_from_mp4(fn);
        ret = extract_cover_from_mp4(fn, tbfn);
    } else if (fn.contains(QRegExp("\\.flac$"))) {
        qDebug() << "flac...";
        if ( !extract_info_from_flac(fn) ) {
            qWarning() << "can't get info from" << fn;
        }
        extract_length_from_flac(fn);
        ret = extract_cover_from_flac(fn, tbfn);
    }
    // TODO: add function to extract flac album
    // http://stackoverflow.com/questions/7119073/c-taglib-cover-art-from-flac-and-asf-files
    return ret;
}

/// fn [in] path to media file to be extracted album art
/// tbfn [out] path to extracted album art
/// bool: true if successful, false if failed
bool GetCover::extract_cover_from_mp3(const QString& fn, QString& tbfn)
{
    TagLib::MPEG::File file(fn.toStdString().c_str());
    tbfn = "";
    if (!file.isValid()) {
        //qDebug() << "file is invalid";
        return false;
    }
    if (!file.hasID3v2Tag()) {
        return false;
    }

    //qDebug() << "id3v2 tag...";
    TagLib::ID3v2::Tag *tag = file.ID3v2Tag();
    // qDebug() << QString("artist(%1),album(%2),title(%3")
    //             .arg(tag->artist().toCString(true))
    //             .arg(tag->album().toCString(true))
    //             .arg(tag->title().toCString(true));
    TagLib::ID3v2::FrameList frames = tag->frameListMap()["APIC"];
    if (frames.isEmpty()) {
        //qDebug() << "APIC frame is empty";
        return false;
    }
/*
      ID3v2::FrameList::ConstIterator it = id3v2tag->frameList().begin();
      for(; it != id3v2tag->frameList().end(); it++)
        cout << (*it)->frameID() << " - \"" << (*it)->toString() << "\"" << endl;
*/
    TagLib::ID3v2::FrameList::ConstIterator it = frames.begin();
    //cout << (*it)->frameID() << "==>" << (*it)->toString();
    QString tbtype = (*it)->toString().toCString(); // shows: APIC
    qDebug() << (*it)->frameID().data() << "type:" << tbtype;   // shows: images/jpeg
    //cast Frame * to AttachedPictureFrame*
    TagLib::ID3v2::AttachedPictureFrame *pf = static_cast<TagLib::ID3v2::AttachedPictureFrame *> (*it);
    if (pf == NULL) {
        //qDebug() << "getMP3Frame: pf is null";
        return false;
    }
    bool isJpeg = tbtype.contains("jpeg");
    /// _img is the original thumbnail from media file
    QImage _img;
    _img.loadFromData((const uchar*)pf->picture().data(), pf->picture().size());
    bool ret = save_thumbnail(_img, tbfn, isJpeg);

    return ret;
}

/**
    \return true if thumbnail extracted, false if no thumbnail
**/
bool GetCover::extract_cover_from_mp4(const QString& fn, QString& tbfn)
{
    TagLib::MP4::File file(fn.toStdString().c_str());
    TagLib::MP4::Tag *tag = file.tag();
    tbfn = "";
    if (tag == NULL) {
        //qDebug() << "tag is null";
        return false;
    }
    // m_artist = tag->artist().toCString(true);
    // m_album = tag->album().toCString(true);
    // m_title = tag->title().toCString(true);
    /// get covr from m4a
    if ( !tag->itemListMap().contains("covr") ) {
        //qDebug() << "no covr";
        return false;
    }

    //qDebug() << "get covr...";
    TagLib::MP4::CoverArtList list = tag->itemListMap()["covr"].toCoverArtList();
    // const char *psz_format = list[0].format() == TagLib::MP4::CoverArt::PNG ? "image/png" : "image/jpeg";
    // (void)psz_format;
    bool isJpeg = (list[0].format() == TagLib::MP4::CoverArt::JPEG);
//    qDebug() << "id3tag: mp4: found embedded art: " << psz_format << ", "
//             << list[0].data().size() << "bytes";
    QImage _img;
    _img.loadFromData((const uchar *)list[0].data().data(), list[0].data().size());
    //QString confmd5 = ();

    bool ret = save_thumbnail(_img, tbfn, isJpeg);
    return ret;
}

bool GetCover::extract_cover_from_flac(const QString& fn, QString& tbfn)
{
    tbfn = "";

    TagLib::FLAC::File file(fn.toStdString().c_str());
    const TagLib::List<TagLib::FLAC::Picture*>& picList = file.pictureList();
    if ( picList.size() == 0 ) {
        qDebug() << Q_FUNC_INFO << "picList is empty...";
        return false;
    }
    TagLib::FLAC::Picture* pic = picList[0];
    bool isJpeg = false;
    QString mimetype = pic->mimeType().toCString(true);
    if (mimetype.contains("jpeg")) {
        isJpeg = true;
    }
    qDebug() << "mime type:" << mimetype;

    QImage _img;
    _img.loadFromData((const uchar*)pic->data().data(), pic->data().size());
    bool ret = save_thumbnail(_img, tbfn, isJpeg);
    return ret;
}

bool GetCover::save_thumbnail(const QImage& img, QString& tbfn, bool isJpeg)
{
    QString hstr = md5sum((const char*)img.constBits(), img.byteCount());
    //qDebug() << "hstr:" << hstr;
    tbfn = get_thumb_name(hstr);
    //qDebug() << "tbfn:" << hstr;
    if ( isFileExisted(tbfn) ) {
        //qDebug() << "such thumbnail existed, don't save and report last tbfn:" << tbfn;
        return true;
    }

    const int DEFAULT_SHRINK_WIDTH = 800;
    const int DEFAULT_SHRINK_HEIGHT = 800;
    if (m_writetb) {
        // m_resizetb will ignore m_followtype
        if (m_resizetb) {
            QImage resized_img = img.scaled(
                QSize(DEFAULT_SHRINK_WIDTH, DEFAULT_SHRINK_HEIGHT),
                Qt::KeepAspectRatio);
            resized_img.save(tbfn, "PNG");
        } else {
            if (m_followtype && isJpeg) {
                    img.save(tbfn, "JPG");
            } else {
                img.save(tbfn, "PNG");
            }
        }
    } else {
        qDebug() << "will not save tb...";
    }

    //qDebug() << "thumbnail:" << tbfn;
    return true;
}

bool GetCover::isFileExisted(const QString& fn)
{
    QFile fileobj(fn);
    return fileobj.exists();
}

void GetCover::setWriteTb(bool b)
{
    m_writetb = b;
}
void GetCover::setFollowImageType(bool b)
{
    m_followtype = b;
}
void GetCover::setResizeTb(bool b)
{
    m_resizetb = b;
}
void GetCover::show_toggles()
{
    qDebug() << "m_writetb" << (m_writetb?"on":"off")
        << "m_followtype" << (m_followtype?"on":"off")
        << "m_resizetb" << (m_resizetb?"on":"off");
}
void GetCover::showInfo(const QString& fn)
{
    Q_UNUSED(fn);
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
        QString _artist = tag->artist().toCString(true);
        QString _album = tag->album().toCString(true);
        QString _title = tag->title().toCString(true);
        show_aat(_artist, _album, _title);
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
    QString _artist = tag->artist().toCString(true);
    QString _album = tag->album().toCString(true);
    QString _title = tag->title().toCString(true);
    show_aat(_artist, _album, _title);
    return true;
}

bool GetCover::extract_info_from_flac(const QString& fn)
{
    TagLib::FLAC::File file(fn.toStdString().c_str());
    TagLib::Tag *tag = file.tag();
    if (tag != NULL) {
        QString _artist = tag->artist().toCString(true);
        QString _album = tag->album().toCString(true);
        QString _title = tag->title().toCString(true);
        show_aat(_artist, _album, _title);
        return true;
    } else if (file.hasID3v2Tag()) {
        TagLib::ID3v2::Tag *tag = file.ID3v2Tag();
        QString _artist = tag->artist().toCString(true);
        QString _album = tag->album().toCString(true);
        QString _title = tag->title().toCString(true);
        show_aat(_artist, _album, _title);
        return true;
    }
    return false;
}

bool GetCover::extract_length_from_mp3(const QString& fn)
{
    TagLib::MPEG::File file(fn.toStdString().c_str());
    TagLib::MPEG::Properties p(&file);

    qDebug() << "mp3 len(fn):" << p.length();
    return true;
}

bool GetCover::extract_length_from_mp4(const QString& fn)
{
    TagLib::MP4::File file(fn.toStdString().c_str());

    qDebug() << "m4a len(fn):" << file.audioProperties()->length();
    return true;
}

bool GetCover::extract_length_from_flac(const QString& fn)
{
    qDebug() << Q_FUNC_INFO;

    TagLib::FLAC::File file(fn.toStdString().c_str());
    TagLib::FLAC::Properties p(&file);

    qDebug() << "flac len(fn):" << p.length();
    return true;
}
