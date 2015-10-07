#include <QtCore>
#include <QDebug>
#include <QCryptographicHash>

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


QString get_info()
{
    QByteArray user = qgetenv("USER");
    QByteArray host = qgetenv("HOSTNAME");
    QString s = QString(user) + "@" + QString(host) + " ";
    s = s + QString(__DATE__) + " " + QString(__TIME__);
    //qDebug() << "s: " << s;

    return s;
}

QString getFilenameHash(const QString& fn)
{
    QCryptographicHash hash( QCryptographicHash::Md5 );
    hash.addData(fn.toStdString().c_str(), fn.length());
    QString result = hash.result().toHex().data();
    return result;
}

// ifn: input video filename
QString extractOneFrameFromVideo(const QString& ifn)
{
    QString ofn = getFilenameHash(ifn);
    QString cmd = QString("avconv -ss 0:0:10 -i %1 -vsync 1 -t 0.01 %2.png")
                    .arg(ifn).arg(ofn);

    QProcess process;
    process.start(cmd);
    // will it block???
    process.waitForFinished(-1); // will wait forever until finished

    // just for debug
    // QString stdout = process.readAllStandardOutput();
    // QString stderr = process.readAllStandardError();
    // qDebug() << "stdout: " << stdout;
    // qDebug() << "stderr: " << stderr;
    // just for debug

    return ofn;
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    QString fn = "clip.mp4";
    qDebug() << "output: " << extractOneFrameFromVideo(fn);

    return 0;
}
