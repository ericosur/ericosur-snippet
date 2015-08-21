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

public:
    ID3TAG(QObject *parent = 0);
    ~ID3TAG();

    QString getFilename() const;
    QString getTitle() const;
    QString getArtist() const;
    QString getAlbum() const;
    QImage getCover() const;

    Q_INVOKABLE bool getMetaData(const QString& fn);

Q_SIGNALS:
    void newImage(const QImage& newImage);

protected:
    bool getFrame(TagLib::ID3v2::Tag*);

private:
    QString m_filename;
    QString m_title;
    QString m_artist;
    QString m_album;
    QImage m_cover;
};

#endif // __ID3TAG_H__
