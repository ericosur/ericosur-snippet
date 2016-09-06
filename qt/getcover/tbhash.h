#ifndef __TbHash_H__
#define __TbHash_H__

#include <QObject>
#include <QString>
#include <QHash>
#include <QQueue>

class TbHash : public QObject
{
	Q_OBJECT

public:
    static TbHash* getInstance();

    bool getThumbnail(const QString& fn, QString& tbfn);
    bool hasThumbFile(const QString& fn, QString& tbfn);
    void add_or_move_to_head_at_queue(const QString& tbfn);
    void checkThumbQuota();

    void load();
    void save();
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
