#include <QtCore>
#include <QDebug>

#include <iostream>

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
    }
}


int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    QString fn = "strings.txt";
    test(fn);

    return 0;
}
