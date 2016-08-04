#include <QtCore>
#include <QDebug>
#include <QCoreApplication>
#include <iostream>
#include <QDataStream>
#include <QFile>

#include "qbar.h"

using namespace std;

#define FOOFILE "/tmp/foo.dat"

void msgHandler(QtMsgType type, const QMessageLogContext& ctx, const QString& msg)
{
    const char symbols[] = { 'I', 'E', '!', 'X' };
    QString output = QString("[%1] %2").arg( symbols[type] ).arg( msg );
    std::cerr << output.toStdString() << std::endl;
    if( type == QtFatalMsg ) abort();
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    QBar foo;
    foo.setTitle("King");
    foo.setName("John");
    foo.setNumber("123");
    foo.save();
    foo.show();

    QBar bar;
    bar.setTitle("");
    bar.setName("");
    bar.setNumber("");
    bar.load();
    bar.show();

    return 0;
}
