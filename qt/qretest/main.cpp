#include <QCoreApplication>
#include <QDebug>

#include "testcases.h"
#include "qibla.h"
#include "flock.h"

int main(int argc, char *argv[])
{
	Q_UNUSED(argc);
	Q_UNUSED(argv);


    int ret = util_file_lock(PIDFILE);
    if (ret) {
        qWarning() << Q_FUNC_INFO
            << "another qretest is already running, exit this one...";

        if ( util_test_file_lock(PIDFILE) != 0 ) {
            qDebug() << "util_test_file_lock(\"qretest.pid\")"
                << "qretest is running!";
        } else {
            qDebug() << "util_test_file_lock(\"qretest.pid\")"
                << "qretest not running";
        }
        return -1;
    }
    else {
        qDebug() << "qretest starts ===>";
    }


    QCoreApplication a(argc, argv);

    testSizeOfDataType();

    // unsigned char utf16be[32] = {0x4e, 0x00, 0x58, 0x34, 0x90, 0x4a, 0x62, 0x32};
    // qDebug() << translate_utf16be_to_qstring(utf16be);

    double longitude = 121.5, latitude = 25.119904;
    qDebug() << get_qibla_angle(longitude, latitude);


    return a.exec();
    //return 0;
}
