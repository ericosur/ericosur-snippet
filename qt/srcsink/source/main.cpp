#include <QCoreApplication>
#include <QDebug>
#include "core.h"
#include "commonutil.h"

int main(int argc, char *argv[])
{
    qInstallMessageHandler(myMessageOutput);
    QCoreApplication app(argc, argv);

    qDebug() << app.applicationName() << "starts ===>";


    // MsgRxThread msgrx;
    // QObject::connect(&msgrx, SIGNAL(finished()),

    Core::getInstance()->test();

    return app.exec();
}
