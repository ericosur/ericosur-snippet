#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "colormaker.h"
#include "Id3Tag.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    qmlRegisterType<ColorMaker>("an.qt.ColorMaker", 1, 0, "ColorMaker");
    qmlRegisterType<ID3TAG>("com.pega.rasmus.ID3TAG", 1, 0, "ID3TAG");

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    ColorMaker cm;
    qDebug() << "main thread id : " << QThread::currentThreadId();
    emit cm.testSignal();
    qDebug() << "Finish calling testSignal";

    return app.exec();
}
