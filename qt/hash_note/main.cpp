#include <QCoreApplication>
#include <QDebug>
#include "initnotes.h"

void test()
{
    qDebug() << "C4: " << myhash["C4"] << "Db5" << myhash["Db5"];

}

int main(int argc, char *argv[])
{
    //Q_UNUSED(argc);
    //Q_UNUSED(argv);

    QCoreApplication a(argc, argv);
    myhash = initHashnote();

    test();

    //return a.exec();
    return 0;
}
