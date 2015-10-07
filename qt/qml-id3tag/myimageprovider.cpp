#include "myimageprovider.h"

#include <QDebug>

#include "Id3Tag.h"
#include "myid3data.h"

MyImageProvider::MyImageProvider(ImageType type, Flags flags) :
    QQuickImageProvider(type,flags)
    , m_value(0)
{
}

MyImageProvider::~MyImageProvider()
{
}

/*
void MyImageProvider::setValue(int v)
{
//    static int nextFrameNumber = 0;
//    emit signalNewFrameReady(nextFrameNumber++);
    if (v != m_value) {
        emit valueChanged(v);
        m_value = v;
    }
}
*/

/*
void MyImageProvider::signalNewFrameReady(int frameNumber)
{
    (void)frameNumber;
}
*/

QImage MyImageProvider::requestImage(const QString &id, QSize *size, const QSize &requestedSize)
{
    qDebug() << "requestImage(): id: " << id;
    (void)requestedSize;
    //qDebug() << "reequestedSize: " << requestedSize.width() << " " << requestedSize.height();

    //QImage res = QImage(QString("/home/ericosur/gcode/snippet/qt/qml-flip/prev.jpg"));
    QImage res;
    size->setHeight(500);
    size->setWidth(500);

    MyId3Data *id3 = NULL;
    if ( m_cache.contains(id) ) {
        id3 = m_cache.object(id);
        if (id3 != NULL) {
            res = id3->get_img();
        } else {
            //qDebug() << "requestImage(): no img";
            res = QImage(NULL); // TODO: use default image
        }
    } else {
        //qDebug() << "requestImage(): img not load...";
        res = QImage(NULL); // TODO: use default image
    }

    return res;
}
