#include <QApplication>
#include <QQmlApplicationEngine>

#include <QDebug>
#include <QLocale>
#include <QTranslator>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // rasmus add
    QLocale ql = QLocale::system();
    QString locname = "en_US";
    qDebug() << "system locale: " << ql.name();
    QString ts = ":/lang_" + locname + ".qm";
    qDebug() << "ts: " << ts;
    QTranslator trn;
    bool ret = trn.load(ts);
    if (ret) {
        ret = app.installTranslator(&trn);
        if (!ret)
            qDebug() << "installTranslator(): " << ret;
    } else {
        qDebug() << "load translator " << ts << " failed";
    }
    // rasmus add

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
