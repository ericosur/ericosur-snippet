#include <QCoreApplication>
#include <QString>
#include <QRegularExpression>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QString s = "v=0/t=1/title = hello world/Message=How are you?/Foo3=bar4";
    QRegularExpression re("(?<key>[A-Za-z][A-Za-z0-9_]*)\\s*=\\s*(?<val>[^/]+)");
    QRegularExpressionMatchIterator i = re.globalMatch(s);
    while (i.hasNext()) {
        QRegularExpressionMatch match = i.next();
        QString key = match.captured("key");
        QString val = match.captured("val");
        qDebug() << "match: " << key << "=" << val;
    }
    //return a.exec();
    return 0;
}
