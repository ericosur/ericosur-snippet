#include <QCoreApplication>
#include <QDBusConnection>
#include <QDebug>

#include "clientIf.h"
#include "myhandler.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QDBusConnection dbus = QDBusConnection::systemBus(); // Use session bus
    if (!dbus.isConnected()) {
        qDebug() << "dbus.isConnected() failed!";
    }

    clientIf *client = new clientIf("hu.MainUi", "/", dbus, 0);
    MyHandler rx;
    QObject::connect(client, SIGNAL(somethingHappened(QString)), &rx, SLOT(handleSignal(QString)));

    qDebug() << "call read()";
    client->read();

    qDebug() << "send msg()";
    client->SendMessage("hello world!");


    return a.exec();
}

