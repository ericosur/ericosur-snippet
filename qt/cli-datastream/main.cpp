#include <QtCore>
#include <QDebug>
#include <QCoreApplication>
#include <QDateTime>
#include <QThread>

#include "mymap.h"

void test()
{
    QDateTime curr = QDateTime::currentDateTime();
    qDebug() << "curr:" << curr.toString("yyMMddHHmmssz");
}

void maptest()
{
//     MyMap* foo = new MyMap();
//     foo->init();
//     foo->dump();
//     foo->save();
// //    QThread::msleep(1000);
//     delete foo;

    MyMap* bar = new MyMap();
    qDebug() << "bar->dump()";
    bar->dump();
    // bar->load();
    // bar->dump();

}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    //QCoreApplication app(argc, argv);

    maptest();

    return 0;
}
