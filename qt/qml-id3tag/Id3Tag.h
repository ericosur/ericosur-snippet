#ifndef __ID3TAG_H__
#define __ID3TAG_H__

#include <QObject>

QT_BEGIN_NAMESPACE
#include <QImage>
#include <QCache>
QT_END_NAMESPACE

#include "myid3data.h"

class ID3TAG : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString filename READ getFilename WRITE setFilename)
    Q_PROPERTY(QString title READ getTitle)
    Q_PROPERTY(QString artist READ getArtist)
    Q_PROPERTY(QString album READ getAlbum)
    Q_PROPERTY(QImage cover READ getCover)

public:
    ID3TAG(QObject *parent = 0);
    ~ID3TAG();

    QString getFilename() const;
    void setFilename(const QString& s); // will invoke getMetaData()
    QString getTitle() const;
    QString getArtist() const;
    QString getAlbum() const;
    QImage getCover() const;
    QString getCoverPath() const;

    // invoke this function to load/store id3 tags
    Q_INVOKABLE bool getMetaData(const QString& fn);

protected:
    QString getHashFilename(const QString& fn);
    bool getdata(MyId3Data* id3);

private:
    QString m_filename;
    QString m_title;
    QString m_artist;
    QString m_album;
    QImage  m_cover;
};

// key: fn, value: myid3data
extern QCache<QString, MyId3Data> m_cache;

#endif // __ID3TAG_H__
