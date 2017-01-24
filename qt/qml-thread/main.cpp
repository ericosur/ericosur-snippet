#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QDebug>

#include <iostream>

#include "mycontroller.h"

using namespace std;

void msgHandler(QtMsgType type, const QMessageLogContext& ctx, const QString& msg)
{
    Q_UNUSED(ctx);
    QString prefix = "[" + QTime::currentTime().toString("HH:mm:ss.zzz") + "] ";
    const char symbols[] = { 'I', 'E', '!', 'X' };
    QString output = prefix + QString("[%1] %2").arg( symbols[type] ).arg( msg );
    std::cerr << output.toStdString() << std::endl;
    if( type == QtFatalMsg ) abort();
}

int main(int argc, char *argv[])
{
    qInstallMessageHandler(msgHandler);
    QApplication app(argc, argv);

    // register class MyController
    qmlRegisterType<MyController>("com.pega.rasmus.MyController", 1, 0, "MyController");

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    // connect ?
    //QObject::connect()

    return app.exec();
}
