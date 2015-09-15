#include <QtCore>
#include <QDebug>
//#include <QApplication>
#include <iostream>

using namespace std;

void test()
{
    QProcess process;
    process.start("du -chs /home/rasmus/gcode/snippet/");
    process.waitForFinished(-1); // will wait forever until finished

    QString stdout = process.readAllStandardOutput();
    QString stderr = process.readAllStandardError();

    qDebug() << "stdout: " << stdout;
    qDebug() << "stderr: " << stderr;
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    cout << "hello world" << endl;
    system("pwd");

    test();

    return 0;
}
