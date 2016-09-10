#ifndef __GET_COVER_H__
#define __GET_COVER_H__

#include <QObject>
#include <QString>
#include <QSettings>

class GetCover : public QObject
{
    Q_OBJECT
public:
    static QString get_hash_filename(const QString& fn);
    static bool getcover(const QString& mp3fn, QString& tbfn);
    static bool isFileExisted(const QString& fn);
    static void setWriteTb(bool b);

protected:
    GetCover();	// not welcome to have instance

    static QString md5sum(const char* buffer, int size);
    static bool extract_cover_from_mp3(const QString& fn, QString& tbfn);
    static bool extract_cover_from_mp4(const QString& fn, QString& tbfn);

    static void save_hash(const QString& hash);
    static QString load_hash();
    static QString get_thumb_name(const QString& hstr);

private:
	// default true
	static bool m_writetb;
};

#endif  // __GET_COVER_H__
