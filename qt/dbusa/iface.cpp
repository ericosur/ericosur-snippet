// iface.cpp
#include "iface.h"
#include "ifadapter.h"

#include <QtDBus/QDBusConnection>
#include <QDebug>

interfacedescription::interfacedescription()
{
   new ifadapter(this); // Cleans itself up
   //QDBusConnection dbus = QDBusConnection::sessionBus(); // Use session bus
   QDBusConnection dbus = QDBusConnection::systemBus(); // Use session bus
   if (!dbus.isConnected()) {
       qDebug() << "dbus.isConnected() failed!";
   }
   dbus.registerObject("/",this); // Register object on the bus
   dbus.registerService("hu.MainUi"); // Expose interface to others
}


QString interfacedescription::read()
{
   qDebug() << "Request to read was received!";
   emit somethingHappened("Emitting DBus Signal Now!");
   return QString("Request to read was received!");
}


QString interfacedescription::write()
{
   qDebug() << "Request to write was received!";
   emit somethingHappened("Emitting DBus Signal Now!");
   return QString("Request to write was received!");
}


QString interfacedescription::SendMessage(const QString &cmd)
{
   qDebug() << "Message Received by Server!";
   emit somethingHappened("Emitting DBus Signal Now!");
   return QString("Echoing message received: %1").arg(cmd);
}
