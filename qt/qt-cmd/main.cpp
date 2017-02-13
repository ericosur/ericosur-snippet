#include <QCoreApplication>
#include <QProcess>
#include <QDebug>
#include <QDateTime>
#include <iostream>
#include <string.h>

#include "wait.h"
#include "retry.h"
#include "pass.h"

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

void gen_seed()
{
    qint64 current = QDateTime::currentMSecsSinceEpoch();
    qsrand((uint)(current % 0xffffffff));
}


int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    for (int i = 0; i < argc; i++) {
        //printf("%d: %s\n%s\n", i, argv[i], );
        qDebug() << i << ":" << argv[i] << endl
            << "HMAC-SHA1:" << hmacSha1(argv[i], "1234");
        QString md = md5sum(argv[i], strlen(argv[i]));
        //qDebug() << md;
        if ( md == CIPHER_HASH ) {
            qWarning() << "parameter matched!!";
            return 0;
        }
    }

    cout << "hello world" << endl;
    ///int ret = system("pwd");
    ///qDebug() << "ret:" << ret;

    //test();

    WaitOneSecond t1("t1", 2000), t2("t2", 4000);
    WaitOneSecond w("wait", 8000);
    RetryThread foobar;

    // after thread WaitOneSecond finised, it also quit this app
    QObject::connect(&t1, SIGNAL(finished()), &t2, SLOT(start()));
    QObject::connect(&t2, SIGNAL(finished()), &foobar, SLOT(sltNotifyStop()));
    QObject::connect(&w, SIGNAL(finished()), &foobar, SLOT(sltNotifyStop()));
    QObject::connect(&w, SIGNAL(finished()), &app, SLOT(quit()));

    w.start();
    t1.start();
    foobar.start();

    return app.exec();
}
