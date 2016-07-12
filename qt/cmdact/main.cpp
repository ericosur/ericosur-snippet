#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include "msgqcommand.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QQmlApplicationEngine engine;

    MyCtrl myctrl;
    engine.rootContext()->setContextProperty("myctrl", &myctrl);

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
