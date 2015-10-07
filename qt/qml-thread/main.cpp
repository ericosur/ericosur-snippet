#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "mycontroller.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // register class MyController
    qmlRegisterType<MyController>("com.pega.rasmus.MyController", 1, 0, "MyController");

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    // connect ?
    //QObject::connect()

    return app.exec();
}
