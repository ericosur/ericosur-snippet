#include "imgtest.h"

#include <QDebug>
#include <QFile>
#include <QCryptographicHash>

#define TESTIMAGE "/tmp/z.jpg"

ImgTest* ImgTest::_instance = NULL;

ImgTest* ImgTest::getInstance()
{
    if (_instance == NULL) {
        _instance = new ImgTest();
    }
    return _instance;
}

ImgTest::ImgTest()
{
}

void ImgTest::load()
{
    qDebug() << Q_FUNC_INFO << "load image from:" << TESTIMAGE;
    m_img.load(TESTIMAGE);
    qDebug() << Q_FUNC_INFO << "load finished, byteCount:" << m_img.byteCount();
    QString hstr = md5sum((const char*)m_img.constBits(), m_img.byteCount());
    qDebug() << "md5sum finished:" << hstr;

}

QString ImgTest::md5sum(const char* buffer, int size)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(buffer, size);
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}
