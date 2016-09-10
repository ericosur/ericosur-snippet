#ifndef __ImgTest_H__
#define __ImgTest_H__

#include <QObject>
#include <QString>
#include <QImage>

#define TESTIMAGE "/tmp/z.jpg"

class ImgTest : public QObject
{
	Q_OBJECT

public:
    static ImgTest* getInstance();

    void load(const QString& fn=TESTIMAGE);
    QString md5sum(const char* buffer, int size);
    void show();

protected:
    static ImgTest* _instance;
    explicit ImgTest();

private:
    QImage m_img;
};

#endif	// __ImgTest_H__
