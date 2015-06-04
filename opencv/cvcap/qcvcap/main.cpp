#include <QApplication>
#include <QQmlApplicationEngine>

class MyClass : public QObject
{
    Q_OBJECT
public slots:
    void cppSloot(const QString &msg)  {
        //qDebug() << "called the C++ slot with message:" << msg;
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    QObject *item = engine.rootObjects();
    MyClass myClass;
    QObject::connect(item, SIGNAL(qmlSignal(QString)),
                     &myClass, SLOT(cppSloot(QString)));

    return app.exec();
}
