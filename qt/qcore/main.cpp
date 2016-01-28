#include <QCoreApplication>

#include "foothread.h"
#include "barcontrol.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    FooThread foo;
    BarControl bar;

    QObject::connect(&foo, SIGNAL(started()), &bar, SLOT(onStart()));
    QObject::connect(&foo, SIGNAL(finished()), &bar, SLOT(onFinish()));
    QObject::connect(&bar, SIGNAL(sigClose()), &foo, SLOT(onClose()));
    QObject::connect(&bar, SIGNAL(sigAppQuit()), &a, SLOT(quit()));

    foo.start();

    return a.exec();
}
