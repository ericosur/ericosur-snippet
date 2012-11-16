#include <QtGui/QApplication>
#include "hellowin.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    HelloWin w;
    w.show();
    return a.exec();
}
