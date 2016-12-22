#include "mainwindow.h"
#include "keyeater.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    MainWindow w;

    app.installEventFilter(KeyEater::getInstance());
    w.show();

    return app.exec();
}
