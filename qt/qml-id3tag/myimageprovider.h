#ifndef MYIMAGEPROVIDER_H
#define MYIMAGEPROVIDER_H

#include <QQuickImageProvider>
//class QNetworkAccessManager;

class MyImageProvider : public QQuickImageProvider
{
public:
    MyImageProvider(ImageType type, Flags flags = 0);
    ~MyImageProvider();
    QImage requestImage(const QString& id, QSize* size, const QSize& requestedSize);

protected:

public slots:
    //void setValue(int v);

signals:
    //Q_SIGNAL void signalNewFrameReady(int frameNumber);
    //Q_SIGNAL void valueChanged(int v);

private:
    int m_value;
};

#endif // MYIMAGEPROVIDER_H
