#ifndef __ImgTest_H__
#define __ImgTest_H__

#include <QObject>
#include <QString>
#include <QImage>

class ImgTest : public QObject
{
	Q_OBJECT

public:
    static ImgTest* getInstance();

    void load();
    QString md5sum(const char* buffer, int size);

protected:
    static ImgTest* _instance;
    explicit ImgTest();

private:
    QImage m_img;
};

#endif	// __ImgTest_H__
