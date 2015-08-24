#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "Id3Tag.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    // register id3tag class
    qmlRegisterType<ID3TAG>("com.pega.rasmus.ID3TAG", 1, 0, "ID3TAG");

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
