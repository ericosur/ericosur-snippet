/**
 * \file getcover.h
 * \brief header file for class GetCover
 */
#ifndef __GET_COVER_H__
#define __GET_COVER_H__

#include <QString>
#include <QSettings>

class GetCover
{
public:
    static GetCover* getInstance();

    static QString get_hash_filename(const QString& fn);
    bool getcover(const QString& mp3fn);
    static bool isFileExisted(const QString& fn);
    static void setWriteTb(bool b);

    QString getTitle() {
        return m_title;
    }
    QString getArtist() {
        return m_artist;
    }
    QString getAlbum() {
        return m_album;
    }
    int getLength() {
        return m_length;
    }

protected:
    static GetCover* _instance;
    GetCover(); // not welcome to have instance

    static QString md5sum(const char* buffer, int size);
    bool extract_info_from_mp3(const QString& fn);
    bool extract_info_from_mp4(const QString& fn);
    bool extract_info_from_flac(const QString& fn);
    bool extract_length_from_mp3(const QString& fn);
    bool extract_length_from_mp4(const QString& fn);
    bool extract_length_from_flac(const QString& fn);

    void show_aat(const QString& artist, const QString& album, const QString& title);

private:
    QString m_title = "";
    QString m_artist = "";
    QString m_album = "";
    int m_length = 0;
};

#endif  // __GET_COVER_H__
