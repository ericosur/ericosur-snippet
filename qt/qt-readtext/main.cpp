#include <QtCore>
#include <QDebug>

#include <iostream>

#define DATAFILE    "strings.txt"

using namespace std;

void test(const QString& fn)
{
    QStringList stringList;
    QFile data(fn);
    if (data.open(QFile::ReadOnly)) {
        QTextStream textStream(&data);
        while (true) {
            QString line = textStream.readLine();
            if (line.isNull()) {
                break;
            }
            else {
                //qDebug() << line;
                stringList.append(line);
            }
        }
        qDebug() << stringList;
    } else {
        qDebug() << "cannot open file";
    }
}


int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    cout << "try to read from " << DATAFILE << "\n";
    QString fn = DATAFILE;
    test(fn);

    return 0;
}
