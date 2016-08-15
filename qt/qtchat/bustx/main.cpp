#include <QtCore>
#include <QDebug>
#include <QCoreApplication>
#include <iostream>
#include <unistd.h>
#include "dbusutil.h"

using namespace std;

ENUM_BUS g_session_bus = USE_SYSTEM_BUS;

void msgHandler(QtMsgType type, const QMessageLogContext& ctx, const QString& msg)
{
    Q_UNUSED(ctx);
    const char symbols[] = { 'I', 'E', '!', 'X' };
    QString output = QString("[%1] %2").arg( symbols[type] ).arg( msg );
    std::cerr << output.toStdString() << std::endl;
    if( type == QtFatalMsg ) abort();
}

void usage()
{
    cout << "bustx - send two kinds of signals to dbus" << endl
        << "options:" << endl
        << "\t-c    send COMMAND signal" << endl
        << "\t-m    send MESSAGE signal" << endl
        << "\t-h    this usage" << endl
        << "\t-n    assign name of sender" << endl
        << "\t-s    use session bus" << endl
        << endl
        << "option -c will override -s and -m" << endl;
}

void process_args(int argc, char* argv[])
{
    int c;
    const size_t MAX_CMD_LEN = 64;
    char cmd[MAX_CMD_LEN];
    char sender[MAX_CMD_LEN];
    bool has_sender = false;
    bool has_message = false;

    while (true) {
        c = getopt(argc, argv, "hc:m:n:s");
        if (c == -1)
            break;
        switch (c) {
        case 'h':
        case '?':
            usage();
            return;
        case 'c':
            memset(cmd, 0, MAX_CMD_LEN);
            strncpy(cmd, optarg, qMin(MAX_CMD_LEN, strlen(optarg)));
            send_dbus_signal_to_command(cmd);
            return;
        case 'm':
            has_message = true;
            memset(cmd, 0, MAX_CMD_LEN);
            strncpy(cmd, optarg, qMin(MAX_CMD_LEN, strlen(optarg)));
            break;
        case 'n':
            has_sender = true;
            memset(sender, 0, MAX_CMD_LEN);
            strncpy(sender, optarg, qMin(MAX_CMD_LEN, strlen(optarg)));
            break;
        case 's':
			g_session_bus = USE_SESSION_BUS;
            printf("use session bus");
            break;
        default:
            break;
        }
    }

    if (has_message) {
        send_dbus_signal_to_message(
            cmd,
            (has_sender ? sender : argv[0]) );
    }

    if (argc > optind) {
        for (int i = optind; i < argc; i++) {
            send_dbus_signal_to_message(
                argv[i],
                (has_sender ? sender : argv[0]) );
        }
    }
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    //qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    if (argc == 1) {
        usage();
        return 0;
    }

    process_args(argc, argv);

    return 0;
}
