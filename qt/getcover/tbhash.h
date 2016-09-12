/**
 * \file tbhash.h
 * \brief class TbHash
 */
#ifndef __TbHash_H__
#define __TbHash_H__

#include <QObject>
#include <QString>
#include <QHash>
#include <QQueue>

/**
 * \class TbHash
 * \brief flow controller to extract and manage thumbnail of media file
 */
class TbHash : public QObject
{
	Q_OBJECT

public:
    static TbHash* getInstance();

    bool getThumbnail(const QString& fn, QString& tbfn);
    bool hasThumbFile(const QString& fn, QString& tbfn);
    void add_or_move_to_head_at_queue(const QString& tbfn);
    void checkThumbQuota();
    /**
     * @param b [in] control write hash table info file or not
     */
    void setDoWrite(bool b);

    /// load thumbnail hash table from file
    void load();
    /// save thumbnail hash table into file
    void save();
    /// dump m_tbhash
    void show();

    QHash<QString, QString>& getTbhash();

    friend QDataStream& operator<<(QDataStream& ds, const TbHash& obj);
    friend QDataStream& operator>>(QDataStream& ds, TbHash& obj);

protected:
    static TbHash* _instance;
    explicit TbHash();

private:
    QHash<QString, QString> m_tbhash;
    QQueue<QString> m_thumbq;
    int m_tbsize;
};

#endif	// __TbHash_H__
