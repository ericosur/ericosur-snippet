#include "imgtest.h"

#include <QDebug>
#include <QFile>
#include <QCryptographicHash>

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

void ImgTest::load(const QString& fn)
{
    qDebug() << Q_FUNC_INFO << "load image from:" << fn;
    bool ret = m_img.load(fn);
    if (!ret) {
    	qDebug() << "load FAILED";
    	return;
    }
    qDebug() << Q_FUNC_INFO << "load finished, byteCount:" << m_img.byteCount();
    QString hstr = md5sum((const char*)m_img.constBits(), m_img.byteCount());
    qDebug() << "md5sum finished:" << hstr;
    show();
}

QString ImgTest::md5sum(const char* buffer, int size)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(buffer, size);
    QString str_hash = hash.result().toHex().data();
    return str_hash;
}

void ImgTest::show()
{
	qDebug() << "width:" << m_img.width()
		<< "height:" << m_img.height()
		<< "dotsPerMeterX:" << m_img.dotsPerMeterX()
		<< "dotsPerMeterY:" << m_img.dotsPerMeterY()
		<< "textKeys:" << m_img.textKeys()
		<< "depth:" << m_img.depth()
		<< "bitPlaneCount:" << m_img.bitPlaneCount()
		<< "format:" << m_img.format();
}