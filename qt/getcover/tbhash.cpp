#include "tbhash.h"
#include "getcover.h"

#include <QDebug>
#include <QFile>
#include <QDataStream>
#include <QMetaProperty>

#include <assert.h>

#define FOOFILE  "/tmp/tbhash.dat"

TbHash* TbHash::_instance = NULL;

/**
 * overloaded operator function for putting TbHash into QDataStream
 */
QDataStream& operator<<(QDataStream& ds, const TbHash& obj)
{
    qDebug() << Q_FUNC_INFO << obj.m_tbhash.size();
    ds << obj.m_tbhash;
    return ds;
}
/**
 * overloaded operator function for reading QDataStream into TbHash
 */
QDataStream& operator>>(QDataStream& ds, TbHash& obj)
{
    ds >> obj.m_tbhash;
    qDebug() << Q_FUNC_INFO << obj.m_tbhash.size();
    return ds;
}

/// singleton interface
TbHash* TbHash::getInstance()
{
    if (_instance == NULL) {
        _instance = new TbHash();
    }
    return _instance;
}

TbHash::TbHash()
{
}

QHash<QString, QString>& TbHash::getTbhash()
{
    return m_tbhash;
}
/**
 * @brief TbHash::getThumbnail query thumbnail file name from fn
 * @param fn [in] media file name
 * @param tbfn [out] thumbnail file name
 * @return true if tb exists, false if errors
 */
bool TbHash::getThumbnail(const QString& fn, QString& tbfn)
{
    if (hasThumbFile(fn, tbfn)) {
        return true;
    }
    // try to extract cover from fn
    if ( GetCover::getcover(fn, tbfn) ) {
        m_tbhash.insert(fn, tbfn);
        return true;
    } else {
        m_tbhash.insert(fn, "null");
    }
    return false;
}
/** \brief query if specified fn and returns related tbfn
    \param fn [in] specified media file name
    \param tbfn [out] will return
    - empty string if no thumbnail for fn
    - file name of thumbnail file, usu full path like
        /tmp/6f5902ac237024bdd0c176cb93063dc4.png
    \return true if tbfn exists, false if no tbfn
    \note it will change the order of tbfn in m_thumbq,
    if you query some tbfn, will be taken as recently used
**/
bool TbHash::hasThumbFile(const QString& fn, QString& tbfn)
{
    // not existed at hash table
    if (!m_tbhash.contains(fn)) {
        tbfn = "";
        return false;
    }

    // existed in thumbnail hash
    tbfn = m_tbhash[fn];
    if (tbfn == "null") {
        return false;
    }
    QFile fileobj(tbfn);
    //fileobj.setFileName(tbfn);
    if (fileobj.exists()) {
        // change the pos of tbfn in queue
        add_or_move_to_head_at_queue(tbfn);
        return true;
    } else {
        m_tbhash.remove(fn);
    }
    tbfn = "";
    return false;
}
/** \brief add tbfn into m_thumbq (QQueue)
    \param tbfn [in] given thumbnail filename will be:
    - add into queue head if not exists
    - remove old one and add into queue head

    Purpose of add_or_move_to_head_at_queue() is to
    maintain a RUL, if total size hits limit, will
    remove the least used thumbnails to lower disk usage.

    \note m_thumbq is a queue with tbfn filenames, it
    maintains a recently used list of tbfn.
**/
void TbHash::add_or_move_to_head_at_queue(const QString& tbfn)
{
    int pos = m_thumbq.indexOf(tbfn);

    if (pos == -1) {
        m_thumbq.enqueue(tbfn);
        // check total size of tbfn
        checkThumbQuota();
    } else {
        m_thumbq.removeAt(pos);
        m_thumbq.enqueue(tbfn);
    }
    qDebug() << Q_FUNC_INFO << "current tbfn queue size:" << m_thumbq.size();
}
/** \brief checkThumbQuota() will sum up all occuppied
    disk size of thumbnail files

    total size will be stored at m_tbsize
**/
void TbHash::checkThumbQuota()
{
    m_tbsize = 0;
    QFile fileobj;
    for (int i = 0; i < m_thumbq.size(); ++i) {
        QString tbfn = m_thumbq.at(i);
        fileobj.setFileName(tbfn);
        m_tbsize += fileobj.size();
    }
    qDebug() << Q_FUNC_INFO << "current tbfn total size:" << m_tbsize;
}

void TbHash::setDoWrite(bool b)
{
    GetCover::setWriteTb(b);
}

// save object BarCtrl into file
void TbHash::save()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(FOOFILE);
    if (!file.open(QIODevice::WriteOnly)) {
        qDebug() << "write file failed" << FOOFILE;
        return;
    }
    QDataStream out(&file);
    out << *this;
    file.close();
}

// load object BarCtrl from file
void TbHash::load()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(FOOFILE);
    if (!file.open(QIODevice::ReadOnly)) {
        qDebug() << "read file failed" << FOOFILE;
        return;
    }
    QDataStream out(&file);
    out >> *this;
    file.close();
}

void TbHash::show()
{
    qDebug() << Q_FUNC_INFO << "size:" << m_tbhash.size();
    QHashIterator<QString, QString> i(m_tbhash);
    while (i.hasNext()) {
        i.next();
        qDebug() << i.key() << ":" << i.value();
    }
}
