/** \file main.cpp
**/

#include <QtCore>
#include <QDebug>
#include <QCoreApplication>

#include "mynoise.h"

int main(int argc, char** argv)
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);
    MyNoise::getInstance()->setup();
    MyNoise::getInstance()->startcommandloop();
    return 0;
}
