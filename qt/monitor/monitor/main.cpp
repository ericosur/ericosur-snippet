#include <QCoreApplication>
#include <QDebug>
#include "core.h"
#include "flock.h"

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    if ( util_file_lock("/tmp/monitor.pid") ) {
        qWarning() << Q_FUNC_INFO
            << "another monitor is already running, exit this one...";
        return -1;
    } else {
        qDebug() << "monitor starts ===>";
    }

    // MsgRxThread msgrx;
    // QObject::connect(&msgrx, SIGNAL(finished()),

    Core::getInstance();

    return app.exec();
}
