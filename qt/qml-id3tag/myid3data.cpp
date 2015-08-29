#include "myid3data.h"

#ifdef MY_USE_MD5SUM
#include <QCryptographicHash>
#endif

MyId3Data::MyId3Data() :
    m_fn("")
#ifdef MY_USE_MD5SUM
    , m_md5("")
#endif
{
    m_img = QImage(NULL);
}

MyId3Data::MyId3Data(const QString &fn)
{
    m_fn = fn;
    m_img = QImage(NULL);
#ifdef MY_USE_MD5SUM
    m_md5 = getHash(m_fn);
#endif
}

MyId3Data::~MyId3Data()
{
}

#ifdef MY_USE_MD5SUM
QString MyId3Data::getHash(const QString& str)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(str.toStdString().c_str(), str.length());
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}
#endif  // MY_USE_MD5SUM
