#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include "loadtext.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;
    LoadText loadtext;

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
    engine.rootContext()->setContextProperty("mytext", &loadtext);

    return app.exec();
}
