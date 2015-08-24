#ifndef __ID3TAG_H__
#define __ID3TAG_H__

#include <QObject>
#include <QDebug>
#include <QImage>
//#include <iostream>
#include <id3v2tag.h>

class ID3TAG : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString filename READ getFilename)
    Q_PROPERTY(QString title READ getTitle)
    Q_PROPERTY(QString artist READ getArtist)
    Q_PROPERTY(QString album READ getAlbum)
    Q_PROPERTY(QImage cover READ getCover)
    Q_PROPERTY(QString coverpath READ getCoverPath)
    Q_PROPERTY(QString tmppath READ gettmppath WRITE settmppath)

public:
    ID3TAG(QObject *parent = 0);
    ~ID3TAG();

    QString getFilename() const;
    QString getTitle() const;
    QString getArtist() const;
    QString getAlbum() const;
    QImage getCover() const;
    QString getCoverPath() const;
    QString gettmppath() const;
    void settmppath(const QString& p);

    Q_INVOKABLE bool getMetaData(const QString& fn);

Q_SIGNALS:
    void newImage(const QImage& newImage);

protected:
    bool getMP3Frame(TagLib::ID3v2::Tag*);
    QString getHashFilename(const QString& fn);

private:
    QString m_filename;
    QString m_title;
    QString m_artist;
    QString m_album;
    QImage m_cover;
    QString m_coverpath;
    QString m_tmppath;
};

#endif // __ID3TAG_H__
