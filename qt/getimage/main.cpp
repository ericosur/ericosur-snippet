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
#include "imgtest.h"

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

int main(int argc, char *argv[])
{
    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    qDebug() << "getImgage - QImage tester";
    if (argc == 1) {
        ImgTest::getInstance()->load();
    } else {
        for (int i=1; i<argc; i++) {
            ImgTest::getInstance()->load(argv[i]);
        }
    }

    //return app.exec();
    return 0;
}
