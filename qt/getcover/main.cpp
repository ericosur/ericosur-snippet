/**
    \file: main.cpp
    \brief: entry point and test function
**/

#include <QtCore>
#include <QDebug>
#include <QCoreApplication>
#include <QStringList>
#include <QTime>
#include <iostream>
#include <QFile>
#include <unistd.h>

#include "tbhash.h"
#include "getcover.h"

using namespace std;

void msgHandler(QtMsgType type, const QMessageLogContext& ctx, const QString& msg)
{
    Q_UNUSED(ctx);
    QString prefix = "[" + QTime::currentTime().toString("HH:mm:ss.zzz") + "] ";
    const char symbols[] = { 'I', 'E', '!', 'X' };
    QString output = prefix + QString("[%1] %2").arg( symbols[type] ).arg( msg );
    std::cerr << output.toStdString() << std::endl;
    if( type == QtFatalMsg ) abort();
}

void print_help()
{
    fprintf(stderr,
            "getcover [options] [audio media files]\n"
            "\t-h  help message\n"
            "\t-t  turn off hash table (default:on)\n"
            "\t-n  Not output thumbnail file (default: on)\n"
            "\t-f  specify list file\n"
    );
}

void process_one_file(const QString& fn)
{
    QString tbfn;
    if (GetCover::isFileExisted(fn)) {
        qDebug() << "get thumbnail for:" << fn;
        if ( TbHash::getInstance()->getThumbnail(fn, tbfn) )  {
            qDebug() << "getThumbnail() tbfn:" << tbfn;
        } else {
            qDebug() << "getThumbnail() nok";
        }
    } else {
        qDebug() << "not exists:" << fn;
    }
}

void read_from_list(const QString& listfn)
{
#define DEFAULT_BUFFER_SIZE   (1024)

    FILE* ptr = fopen(listfn.toUtf8(), "r");
    if (ptr == NULL) {
        perror("fopen");
        return;
    }
    char line[DEFAULT_BUFFER_SIZE];
    int cnt = 0;
    while (!feof(ptr)) {
        char* p = fgets(line, DEFAULT_BUFFER_SIZE-1, ptr);
        if (p == NULL) {
            break;
        }
        QString fn(line);
        fn.chop(1);
        process_one_file(fn);
        cnt ++;
    }
    fclose(ptr);
    QString msg = QString("%1 records processed").arg(cnt);
    qDebug() << msg;
}

int main(int argc, char *argv[])
{
    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    if (argc == 1) {
        print_help();
        exit(-1);
    }
    bool use_hashtable = true;
    QString listfn;

    while(1) {
        int cmd_opt = getopt(argc, argv, "htnwf:");
        if (cmd_opt == -1) {
            //qDebug() << "cmd_opt == -1";
            break;
        }
        switch (cmd_opt) {
        case 'h':
            print_help();
            exit(2);
            break;
        case 't':
            use_hashtable = false;
            qDebug() << "use thumbnail hash table?" << (use_hashtable?"yes":"no");
            break;
        case 'n':
            TbHash::getInstance()->setDoWrite(false);
            qDebug() << "no write...";
            break;
        case 'f':
            listfn = optarg;
            qDebug() << "use list file:" << listfn;
            break;
        default:
            break;
        }
    }

    if (use_hashtable) {
        TbHash::getInstance()->load();
    }
    if (listfn != "") {
        read_from_list(listfn);
    }
    // if still cli arguments available
    if (argc > optind) {
        for (int i = optind; i < argc; i++) {
            QString clifn = argv[i];
            process_one_file(clifn);
        }
    }

    if (use_hashtable) {
        TbHash::getInstance()->save();
    }

    //return app.exec();
    return 0;
}
