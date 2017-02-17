#include <QCoreApplication>
#include <QDebug>

#include "flowctrl.h"
#include "commonutil.h"

int main(int argc, char *argv[])
{
    qInstallMessageHandler(myMessageOutput);
    QCoreApplication app(argc, argv);

    qDebug() << app.applicationName() << "starts...";
    FlowControl::getInstance()->start();

    return app.exec();
}
