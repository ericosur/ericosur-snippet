#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtQml>

#include <QStringList>

#include "msgqcommand.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QQmlApplicationEngine engine;

    MyCtrl myctrl;
    engine.rootContext()->setContextProperty("myctrl", &myctrl);

//////////////////////////////////////////
    QStringList dataList;
    dataList.append("Item 1");
    dataList.append("Item 2");
    dataList.append("Item 3");
    dataList.append("Item 4");

    engine.rootContext()->setContextProperty("myModel", QVariant::fromValue(dataList));
//////////////////////////////////////////

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
    return app.exec();
}
