#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include <QDebug>
#include <QScreen>
#include "loadtext.h"

void show_geometry()
{
    QString msg = QString("width: %1, height: %2").
        arg(QGuiApplication::primaryScreen()->geometry().width()).
        arg(QGuiApplication::primaryScreen()->geometry().height());
    qDebug() << Q_FUNC_INFO << msg;
}


int main(int argc, char *argv[])
{
    //QTextCodec *codec = QTextCodec::codecForName("UTF-8");
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;
    LoadText loadtext;

    engine.rootContext()->setContextProperty("mytext", &loadtext);
    qmlRegisterType<LoadText>("com.rasmus", 1, 0, "LoadText");
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    show_geometry();

    return app.exec();
}
