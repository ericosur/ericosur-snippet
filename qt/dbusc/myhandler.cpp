#include "myhandler.h"

#include <QDebug>

MyHandler::MyHandler()
{

}

void MyHandler::handleSignal(const QString &str)
{
    qDebug() << "handleSignal(): got: " << str;
}
