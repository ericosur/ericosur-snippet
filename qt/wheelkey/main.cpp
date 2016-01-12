#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "parsestatus.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QQmlApplicationEngine engine;

    ParseStatus ps;
    engine.rootContext()->setContextProperty("parse_status", &ps);
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
