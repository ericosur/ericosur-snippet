#include <QApplication>
#include "mainwindow.h"
#include "TranslatorManager.h"

int main(int argc, char *argv[])
{
    Q_INIT_RESOURCE(multiLangTest);

    QApplication a(argc, argv);

    // Translator must be created before the application's widgets.
    TranslatorManager* manager = TranslatorManager::instance();
    Q_UNUSED(manager)

    // rasmus add
    QTranslator translator;
    translator.load("lang_zh_TW");
    a.installTranslator(&translator);

    MainWindow w;
    w.show();

    return a.exec();
}
