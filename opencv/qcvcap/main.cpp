#include <QApplication>
#include <QQmlContext>
#include <QQmlApplicationEngine>

#include "core.h"


int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    QList<QObject*> item = engine.rootObjects();
    Core myClass;
    // QObject::connect(item.at(0), SIGNAL(qmlSignal(QString)),
    //                  &myClass, SLOT(cppSloot(QString)));

    engine.rootContext()->setContextProperty("myobject", &myClass);

    return app.exec();
}
