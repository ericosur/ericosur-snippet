#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "../yosemsg.h"
#include "mydatasource.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    myDataSource ds;
    engine.rootContext()->setContextProperty("mydatasource", &ds);

    YoseMsg msg;
    QObject::connect(&msg, SIGNAL(sigQuit()), &app, SLOT(quit()));
    QObject::connect(&msg, SIGNAL(sigRead(const QString&)), &ds, SLOT(sltRead(const QString&)));
    QObject::connect(&msg, SIGNAL(sigMd5sum(const QString&)), &ds, SLOT(sltMd5sum(const QString&)));
    QObject::connect(&msg, SIGNAL(sigWrite()), &ds, SLOT(sltWrite()));

    msg.start();

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
    return app.exec();
}
