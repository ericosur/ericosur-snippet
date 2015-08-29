#ifndef __ID3TAG_H__
#define __ID3TAG_H__

#include <QObject>
#include <QDebug>
#include <QImage>

#include <QCache>

#include "myid3data.h"

class ID3TAG : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString filename READ getFilename WRITE setFilename)
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
    void setFilename(const QString& s); // will invoke getMetaData()
    QString getTitle() const;
    QString getArtist() const;
    QString getAlbum() const;
    QImage getCover() const;
    QString getCoverPath() const;
    QString gettmppath() const;
    void settmppath(const QString& p);

    Q_INVOKABLE bool getMetaData(const QString& fn);

    /*
    static QImage& getCurrCover() {
        return m_cover_curr;
    }
    static QImage& getPrevCover() {
        return m_cover_prev;
    }
    */


Q_SIGNALS:
    void newImage(const QImage& newImage);

protected:
    QString getHashFilename(const QString& fn);
    bool getdata(MyId3Data* id3);

protected:
    QImage getMp3Cover(const QString& fn);
    QImage getM4ACover(const QString& fn);

private:
    QString m_filename;
    QString m_title;
    QString m_artist;
    QString m_album;
    QString m_coverpath;
    QString m_tmppath;
    QImage  m_cover;
};

// key: fn, value: myid3data
extern QCache<QString, MyId3Data> m_cache;

#endif // __ID3TAG_H__
