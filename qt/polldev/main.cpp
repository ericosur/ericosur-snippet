/**
 * main.cpp
 */

#include "core.h"

#include <QCoreApplication>
#include <QTime>
#include <QDebug>
#include <iostream>
#include <unistd.h>

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

void helpMessage()
{
    fprintf(stderr, "built at: %s %s\n", __DATE__, __TIME__);
    fprintf(stderr,
            "testopt [options] <message>\n"
            "-h  help message\n"
            "-i  launch ipodui directly\n"
            "-m  launch mediaui directly\n"
            "-s  start poll thread (default)\n"
        );
}


int main(int argc, char *argv[])
{
    qInstallMessageHandler(msgHandler);
    QCoreApplication app(argc, argv);

    int cmd_opt = 0;
    bool bHelp = false;
    bool bStart = true;
    bool bIpod = false;
    bool bMedia = false;

    while (true) {
        if ( (cmd_opt = getopt(argc, argv, "hims")) == -1 ) {
            // something wrong
            break;
        }
        switch (cmd_opt) {
        case 'h':
            bHelp = true;
            break;
        case 'i':
            bIpod = true;
            // will not process the other parameters
            break;
        case 'm':
            bMedia = true;
            // will not process the other parameters
            break;
        case 's':
            // it is default
            bStart = true;
            // will not process the other parameters
            break;
        default:
            qDebug() << "unknown switch:" << cmd_opt;
            break;
        }
    }

    if (bHelp) {
        helpMessage();
        return 0;
    }

    if (bIpod) {
        qDebug() << "launch ipodui...";
        Core::getInstance()->launchIpod();
        return 0;
    }

    if (bMedia) {
        qDebug() << "launch mediaui...";
        Core::getInstance()->launchMedia();
        return 0;
    }

    if (bStart) {
        Core::getInstance()->start();
    }

    return app.exec();
}
