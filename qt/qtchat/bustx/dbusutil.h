#ifndef __DBUSUTIL_H__
#define __DBUSUTIL_H__

#include <QString>
#include <QDBusConnection>
#include <QDBusMessage>

#define DUTIL_DBUS_PATH "/qtapp"
#define DUTIL_DBUS_IFACE "com.pega.rasmus"
#define DUTIL_COMMAND_SIGNAL_NAME "command"
#define DUTIL_MESSAGE_SIGNAL_NAME "message"

void send_dbus_signal_to_command(const QString& str);
void send_dbus_signal_to_message(const QString& str, const QString& sender_name="");

#endif  // __DBUSUTIL_H__
