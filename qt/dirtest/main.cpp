#include <QCoreApplication>
#include <QTime>
#include <QDebug>
#include <iostream>
#include "core.h"

using namespace std;

bool verbose = true;
void msgHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
{
    Q_UNUSED(context);
    QString txt;
    QString prefix = "[" + QTime::currentTime().toString("HH:mm:ss.zzz") + "] ";

    switch (type) {
        case QtDebugMsg:
            txt = prefix + QString("D: %1").arg(msg);
            if (verbose)
                cout << txt.toUtf8().data() << endl;
            break;
        case QtWarningMsg:
            txt = prefix + QString("W: %1").arg(msg);
            cout << txt.toUtf8().data() << endl;
            break;
        case QtCriticalMsg:
            txt = prefix + QString("C: %1").arg(msg);
            cout << txt.toUtf8().data() << endl;
            break;
        case QtInfoMsg:
            txt = prefix + QString("I: %1").arg(msg);
            if (verbose)
                cout << txt.toUtf8().data() << endl;
            break;
        case QtFatalMsg:
            txt = prefix + QString("F: %1").arg(msg);
            cout << txt.toUtf8().data() << endl;
            abort();
    }
}

int main(int argc, char *argv[])
{
    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    if (argc > 1) {
        Core::getInstance()->start(argv[1]);
    } else {
        Core::getInstance()->start("/home/rasmus/Pictures/");
    }



    //return app.exec();
}
