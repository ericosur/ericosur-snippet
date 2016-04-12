#include <QCoreApplication>

#include "readjson.h"

#define JSONFILE "/src/snippet/qt/json/a.json"

int main(int argc, char *argv[])
{
    //QCoreApplication a(argc, argv);

    ReadJson rj(JSONFILE);
    rj.loadFile();
    return 0;

    //return a.exec();
}
