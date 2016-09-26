//#include <QCoreApplication>

#include <QDebug>
#include <QString>

#include "util.h"


int main(int argc, char *argv[])
{

    if (argc == 1) {
        qDebug() << "please specify mp3 names...";
        return -1;
    }
    for (int i=1; i<argc; ++i) {
        // qDebug() << "media:" << argv[i]
        //     << "hasApe?" << ( hasAPETag(argv[i]) ? "yes" : "no" );
        getTags(argv[i]);
    }


//    QCoreApplication a(argc, argv);
//    return a.exec();
    return 0;
}
