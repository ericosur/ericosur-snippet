#include "dbusutil.h"
#include <QDebug>

bool check_dbus_connection()
{
    if (QDBusConnection::sessionBus().isConnected()) {
        return true;
    } else {
        qDebug() << "Cannot connect to the D-Bus session bus";
        return false;
    }
}

void print_dbussend_command(const QString& str, const QString& sender_name="")
{
    QString cmd;

    if (sender_name == "") {
        cmd = QString::asprintf("dbus-send --session --type=signal %s %s.%s "
            "string:\"%s\"",
            DUTIL_DBUS_PATH, DUTIL_DBUS_IFACE, DUTIL_COMMAND_SIGNAL_NAME,
            str.toUtf8().data());
    } else {
        cmd = QString::asprintf("dbus-send --session --type=signal %s %s.%s "
            "string:\"%s\" string:\"%s\"",
            DUTIL_DBUS_PATH, DUTIL_DBUS_IFACE, DUTIL_MESSAGE_SIGNAL_NAME,
            sender_name.toUtf8().data(), str.toUtf8().data());
    }

    qDebug() << cmd;
}

void send_dbus_signal_to_command(const QString& str)
{
    if ( !check_dbus_connection() ) {
        return;
    }

    //emit message(m_nickname, messageLineEdit->text());
    QDBusMessage msg = QDBusMessage::createSignal(DUTIL_DBUS_PATH,
        DUTIL_DBUS_IFACE, DUTIL_COMMAND_SIGNAL_NAME);
    msg << str;
    QDBusConnection::sessionBus().send(msg);

    print_dbussend_command(str);
}

void send_dbus_signal_to_message(const QString& str, const QString& sender_name)
{
    if ( !check_dbus_connection() ) {
        return;
    }

    //emit message(m_nickname, messageLineEdit->text());
    QDBusMessage msg = QDBusMessage::createSignal(DUTIL_DBUS_PATH,
        DUTIL_DBUS_IFACE, DUTIL_MESSAGE_SIGNAL_NAME);
    msg << sender_name << str;
    QDBusConnection::sessionBus().send(msg);

    print_dbussend_command(str, sender_name);
}
