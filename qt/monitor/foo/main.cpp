#include <QCoreApplication>
#include <QDebug>

#include "flock.h"
#include "msgqsend.h"

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    if (util_file_lock("/tmp/foo.pid")) {
        qWarning() << Q_FUNC_INFO
            << "another foo is already running, exit this one...";
        return -1;
    }
    else {
        qDebug() << "foo starts ===>";
        send_msgq(MESGQKEY_MONITOR, MESGQKEY_MESSAGE_TYPE, "foo");
    }

    return app.exec();
}
