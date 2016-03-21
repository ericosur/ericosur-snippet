#include <QApplication>
#include <QQmlApplicationEngine>

#include <QDebug>
#include <QLocale>
#include <QTranslator>

#include <QtQml>
#include "mytranslation.hpp"
#include "filereader.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // rasmus add
    QLocale ql = QLocale::system();
    qDebug() << "system locale: " << ql.name();
    // try to load a specified locale translation file:
    QString locname = "fr_FR";
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

    qmlRegisterType<MyTranslation>("com.pega.rasmus", 1, 0, "MyTranslation");
    MyTranslation mt;

    qmlRegisterType<FileReader>("com.pega.rasmus", 1, 0, "FileReader");

    QQmlApplicationEngine engine;
    //engine.rootContext()->setContextProperty("MyTranslation", &mt);
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
