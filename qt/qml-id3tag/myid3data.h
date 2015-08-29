#ifndef MYID3DATA_H
#define MYID3DATA_H

#include <QString>
#include <QImage>

class MyId3Data
{
public:
    MyId3Data();
    MyId3Data(const QString& fn);
    ~MyId3Data();

#ifdef MY_USE_MD5SUM
    QString getHash(const QString& str);
#endif

    void set_fn(const QString& fn) {
        m_fn = fn;
    }
    QString get_fn() const {
        return m_fn;
    }
    void set_str(const QString& s) {
        m_str = s;
    }
    QString get_str() {
        return m_str;
    }
    void set_artist(const QString& s) {
        m_artist = s;
    }
    QString get_artist() {
        return m_artist;
    }
    void set_album(const QString& s) {
        m_album = s;
    }
    QString get_album() {
        return m_album;
    }
    void set_title(const QString& s) {
        m_title = s;
    }
    QString get_title() {
        return m_title;
    }

    void set_img(const QImage& img) {
        m_img = img;
    }
    QImage get_img() const {
        return m_img;
    }

private:
    QString m_fn;
    QString m_str;
    QString m_artist;
    QString m_album;
    QString m_title;
    QImage m_img;
#ifdef MY_USE_MD5SUM
    QString m_md5;
#endif
};

#endif // MYID3DATA_H
