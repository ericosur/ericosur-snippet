// file: nnmsgpub.h
#ifndef __NNMSG_PUB_H__
#define __NNMSG_PUB_H__

#include <QObject>
#include <QString>

class NnmsgPub : public QObject
{
    Q_OBJECT
public:
    NnmsgPub(const QString& url);
    ~NnmsgPub();

    void bindserver();
    void shutdown();

    int getsock() const {
        return m_sock;
    }
    QString geturl() const {
        return m_url;
    }

    void senddata(const QString& str);
protected:

private:
    int m_sock;
    int m_eid;
    QString m_url;
};

#endif  // __NNMSG_PUB_H__
