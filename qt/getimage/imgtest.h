/**
 * \file imgtest.h
 * \brief class ImgTest here
 */
#ifndef __ImgTest_H__
#define __ImgTest_H__

#include <QObject>
#include <QString>
#include <QImage>

#define TESTIMAGE "/tmp/z.jpg"

/**
 * \class ImgTest
 * \brief singleton class for testing QImage manipulation functions
 */
class ImgTest : public QObject
{
	Q_OBJECT

public:
    static ImgTest* getInstance();

    const int DEFAULT_SHRINK_WIDTH = 800;
    const int DEFAULT_SHRINK_HEIGHT = 800;

    /**
     * @param fn [in] specified image file to load
     */
    void load(const QString& fn=TESTIMAGE);
    /**
     * @brief ImgTest::md5sum take md5sum from a buffer with size
     * @param buffer [in] input buffer
     * @param size [in] buffer size
     * @return md5 hash value as string
     */
    static QString md5sum(const char* buffer, int size);
    /**
     * @brief will show attributes of a loaded QImage
     */
    void show();
    /**
     * @param will shrink image by using DEFAULT_SHRINK_WIDTH and DEFAULT_SHRINK_HEIGHT
     * @return false if no image is loaded
     */
    bool shrink();

protected:
    static ImgTest* _instance;
    explicit ImgTest();

private:
    QImage m_img;
    bool isLoaded = false;
};

#endif	// __ImgTest_H__
