#include <QCoreApplication>
#include <QtDBus>
#include <QDebug>
#include "iface.h"
#include "ifadapter.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    qDebug() << "init dbus server..";
    new interfacedescription();


    return a.exec();
}
