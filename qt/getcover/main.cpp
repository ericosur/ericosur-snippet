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

void process_one_file(const QString& fn)
{
    QString tbfn;
    if (GetCover::isFileExisted(fn)) {
        qDebug() << "get thumbnail for:" << fn;
        bool ret = TbHash::getInstance()->getThumbnail(fn, tbfn);
        if (ret) {
            qDebug() << "tbfn:" << tbfn;
        }
        qDebug() << "ret:" << (ret?"ok":"nok");
    } else {
        qDebug() << "not found:" << fn;
    }
}

void read_from_list()
{
#define LISTFILE "/tmp/list.txt"
#define DEFAULT_BUFFER_SIZE   (1024)

    FILE* ptr = fopen(LISTFILE, "r");
    if (ptr == NULL) {
        perror("fopen");
        return;
    }
    char line[DEFAULT_BUFFER_SIZE];

    int cnt = 0;
    while (!feof(ptr)) {
        char* p = fgets(line, DEFAULT_BUFFER_SIZE-1, ptr);
        (void)p;
        QString fn(line);
        fn.chop(1);
        process_one_file(fn);
        cnt ++;
    }
    fclose(ptr);
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    TbHash::getInstance()->load();
    if (argc == 1) {
        qDebug() << "no argument provided, try to use list.txt";
        read_from_list();
        TbHash::getInstance()->save();
        return 0;
    }

    for (int i=1; i<argc; i++) {
        QString fn = argv[i];
        process_one_file(fn);
    }
    TbHash::getInstance()->save();

    //return app.exec();
    return 0;
}
