//#include <QCoreApplication>

#include <QDebug>
#include <QString>

#include "util.h"


int main(int argc, char *argv[])
{

    if (argc > 1) {
        if (hasAPETag(argv[1])) {
            //qDebug() << argv[1] << " has APE tag";
			// print file name if true
            qDebug() << argv[1];
        }
    }

//    QCoreApplication a(argc, argv);

//    return a.exec();
}
