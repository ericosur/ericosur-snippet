#include <QCoreApplication>
#include "radioadapter.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);


    QDBusConnection bus = QDBusConnection::sessionBus();
    RadioControl myRadio;
    RadioControlAdaptor myRadioAdaptor(&myRadio);

    if (!bus.registerService("local.radiocontrol")) {
            qDebug() << bus.lastError().message();
            exit(1);
    }
    bus.registerObject("/", &myRadio);


    return a.exec();
}

