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
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    qDebug() << "hello world";
    ImgTest::getInstance()->load();
    
    //return app.exec();
    return 0;
}
