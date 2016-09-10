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

    const int DEFAULT_SHRINK_WIDTH = 800;
    const int DEFAULT_SHRINK_HEIGHT = 800;

    void load(const QString& fn=TESTIMAGE);
    static QString md5sum(const char* buffer, int size);
    void show();
    bool shrink();

protected:
    static ImgTest* _instance;
    explicit ImgTest();

private:
    QImage m_img;
    bool isLoaded = false;
};

#endif	// __ImgTest_H__
