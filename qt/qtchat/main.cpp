#include <QDebug>
#include <QDBusConnection>
#include "chat.h"


int main(int argc, char **argv)
{
    QApplication app(argc, argv);
    bool ret = false;

    g_session_bus = USE_SYSTEM_BUS;
    //g_session_bus = USE_SESSION_BUS;
    if (argc > 1 && strcmp(argv[1], "session")==0) {
        g_session_bus = USE_SESSION_BUS;
        ret = QDBusConnection::sessionBus().isConnected();
        qDebug() << "use session bus:" << ret;
    } else {
        ret = QDBusConnection::systemBus().isConnected();
        qDebug() << "use system bus:" << ret;
    }

    if (!ret) {
        qWarning("Cannot connect to the D-Bus session bus.\n"
                 "Please check your system settings and try again.\n");
        return 1;
    }

    ChatMainWindow chat;
    chat.show();
    return app.exec();
}
