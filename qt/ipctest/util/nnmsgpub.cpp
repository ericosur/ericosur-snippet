// file: nnmsgpub.cpp

#include "nnmsgpub.h"

#include <QDebug>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/pubsub.h>

NnmsgPub::NnmsgPub(const QString& url)
{
    m_url = url;
    m_sock = -1;
    qDebug() << Q_FUNC_INFO << "url set to:" << m_url;
    bindserver();
}

NnmsgPub::~NnmsgPub()
{
    qDebug() << Q_FUNC_INFO;
    shutdown();
}

void NnmsgPub::bindserver()
{
    int ret;

    m_sock = nn_socket(AF_SP, NN_PUB);
    if (m_sock < 0) {
        m_sock = -1;
        qDebug() << Q_FUNC_INFO << "cannot create socket...:" << errno;
    }

    m_eid = nn_bind(m_sock, m_url.toUtf8());
    if (m_eid < 0) {
        qDebug() << Q_FUNC_INFO << "fail to bind:" << m_url << ":" << errno;
    }
}

void NnmsgPub::shutdown()
{
    if (m_sock < 0)
        return;

    int ret = nn_shutdown(m_sock, m_eid);
    if (ret < 0) {
        qDebug() << Q_FUNC_INFO << "fail to shutdown:" << errno;
    }
}

void NnmsgPub::senddata(const QString& str)
{
    if (m_sock < 0) {
        qDebug() << Q_FUNC_INFO << "sock not ready...";
        return;
    }
    // start to send specified data
    int sz_d = str.length() + 1;
    int bytes = nn_send(m_sock, str.toUtf8(), sz_d, 0);

    qDebug() << Q_FUNC_INFO <<
        QString("sent ") + ((bytes == sz_d) ? "ok" : "nok");
}
