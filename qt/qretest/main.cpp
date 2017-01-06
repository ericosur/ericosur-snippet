#include <QCoreApplication>
#include <QDebug>

#include "testcases.h"
#include "qibla.h"
#include "flock.h"
#include "flock_broker.h"
#include "simplenotify.h"

void doTests()
{
    testSizeOfDataType();

    // unsigned char utf16be[32] = {0x4e, 0x00, 0x58, 0x34, 0x90, 0x4a, 0x62, 0x32};
    // qDebug() << translate_utf16be_to_qstring(utf16be);

    double longitude = 121.5, latitude = 25.119904;
    qDebug() << get_qibla_angle(longitude, latitude);

    testblacklist();
}

int main(int argc, char *argv[])
{
	Q_UNUSED(argc);
	Q_UNUSED(argv);

    QCoreApplication app(argc, argv);

    int ret = util_file_lock(PIDFILE);
    if (ret) {
        qWarning() << Q_FUNC_INFO
            << "another qretest is already running, exit this one...";

        if ( util_test_file_lock(PIDFILE) != 0 ) {
            qDebug() << PIDFILE << "is locked by another process";
        } else {
            qDebug() << PIDFILE << "is NOT locked by another process, should not be here...";
            return -1;
        }

        FlockBroker::getInstance()->startLockWait();
        // QObject::connect(FlockBroker::getInstance()->getWaitUnlock(), SIGNAL(finished()),
        //     &app, SLOT(quit()));
    }
    else {
        qDebug() << "qretest starts ===>";
        doTests();
    }

    FlockBroker::getInstance()->startWatchFile();
    // SimpleNotify sn("/tmp/statusbarui.dat");
    // QObject::connect(&sn, SIGNAL(sigNotify()), &app, SLOT(quit()));
    // sn.start();

    return app.exec();
}
