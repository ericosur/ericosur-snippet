#ifndef __ID3TAG_H__
#define __ID3TAG_H__

#include <QObject>
#include <QDebug>
#include <iostream>

class ID3TAG : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString filename READ getFilename)
    Q_PROPERTY(QString title READ getTitle)
    Q_PROPERTY(QString artist READ getArtist)
    Q_PROPERTY(QString album READ getAlbum)

public:
    ID3TAG(QObject *parent = 0);
    ~ID3TAG();

    QString getFilename() const;
    QString getTitle() const;
    QString getArtist() const;
    QString getAlbum() const;

    Q_INVOKABLE bool getMetaData(const QString& fn);

protected:

private:
    QString m_filename;
    QString m_title;
    QString m_artist;
    QString m_album;
};

#endif // __ID3TAG_H__
