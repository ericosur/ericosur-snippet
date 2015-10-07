#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "Id3Tag.h"
#include "myimageprovider.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    // register id3tag class
    qmlRegisterType<ID3TAG>("com.pega.rasmus.ID3TAG", 1, 0, "ID3TAG");
    // register my own image provider
    MyImageProvider *imageProvider = new MyImageProvider(QQmlImageProviderBase::Image);

//    QObject::connect(imageProvider, SIGNAL(valueChanged(int)), imageProvider, SLOT(setValue(int)));

    QQmlApplicationEngine engine;
    engine.addImageProvider("myprovider", imageProvider);

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
