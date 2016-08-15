#include "dbusutil.h"
#include <QDebug>

QDBusConnection get_bus()
{
    if (g_session_bus == USE_SESSION_BUS) {
        qDebug() << "session bus...";
        return QDBusConnection::sessionBus();
    } else if (g_session_bus == USE_SYSTEM_BUS) {
        qDebug() << "system bus...";
        return QDBusConnection::systemBus();
    } else {
        return QDBusConnection("qtchat");
    }
}

bool check_dbus_connection()
{
    bool ret = false;

    if (g_session_bus == USE_SESSION_BUS) {
        ret = QDBusConnection::sessionBus().isConnected();
        qDebug() << "is sessionbus connected?"
            << (ret ? "yes" : "no");
    } else if (g_session_bus == USE_SYSTEM_BUS) {
        ret = QDBusConnection::systemBus().isConnected();
        qDebug() << "is systembus connected?"
            << (ret ? "yes" : "no");
    }

    return ret;
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
    get_bus().send(msg);

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
    get_bus().send(msg);

    print_dbussend_command(str, sender_name);
}
