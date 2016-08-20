#include <QCoreApplication>
#include <QProcess>
#include <QDebug>
#include <iostream>

#include "wait.h"

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
	QCoreApplication app(argc, argv);

    for (int i = 0; i < argc; i++) {
    	printf("%d: %s\n", i, argv[i]);
    }

    cout << "hello world" << endl;
    int ret = system("pwd");
    qDebug() << "ret:" << ret;

    test();

    WaitOneSecond w;
    // after thread WaitOneSecond finised, it also quit this app
    QObject::connect(&w, SIGNAL(finished()), &app, SLOT(quit()));
    w.start();

    return app.exec();
}
