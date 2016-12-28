#include <QtCore>
#include <QDebug>
#include <QCoreApplication>
#include <iostream>
#include <QDataStream>
#include <QFile>
#include <QDateTime>
#include <QThread>

#include "qbar.h"
#include "qfoo.h"
#include "mymap.h"

using namespace std;

#define FOOFILE "/tmp/foo.dat"

void msgHandler(QtMsgType type, const QMessageLogContext& ctx, const QString& msg)
{
    Q_UNUSED(ctx);
    const char symbols[] = { 'I', 'E', '!', 'X' };
    QString output = QString("[%1] %2").arg( symbols[type] ).arg( msg );
    std::cerr << output.toStdString() << std::endl;
    if( type == QtFatalMsg ) abort();
}

void test()
{
    QDateTime curr = QDateTime::currentDateTime();
    qDebug() << "curr:" << curr.toString("yyMMddHHmmssz");
}

void test_datastream()
{
    QFoo slot;
    QBar *foo = new QBar;
    foo->setTitle("King");
    foo->setName("John");
    foo->setNumber("123");
    foo->save();
    qDebug() << "foo.save()";
    //foo.show();
    delete foo;

    QBar bar;
    qDebug() << "bar.show()...";
    bar.show();

    QObject::connect(&bar, SIGNAL(titleChanged()), &slot, SLOT(sltTitle()));
    QObject::connect(&bar, SIGNAL(nameChanged()), &slot, SLOT(sltName()));
    QObject::connect(&bar, SIGNAL(numberChanged()), &slot, SLOT(sltNumber()));

    //bar.setTitle("");
    //bar.setName("");
    //bar.setNumber("");
    qDebug() << "bar.load()...";
    bar.load();
    bar.show();
}

void maptest()
{
    MyMap* foo = new MyMap();
    foo->init();
    //foo->dump();
    foo->save();
    QThread::msleep(1000);
    delete foo;

    MyMap* bar = new MyMap();
    bar->dump();
    bar->load();
    bar->dump();

}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    qInstallMessageHandler(msgHandler);
    //QCoreApplication app(argc, argv);

    //test();
    //test_datastream();
    maptest();

    return 0;
}
