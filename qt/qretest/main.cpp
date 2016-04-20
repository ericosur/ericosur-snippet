#include <QCoreApplication>
#include <QString>
#include <QRegularExpression>
#include <QDebug>

void testRegexp()
{
    QString s = "v=0/t=1/title = hello world/Message=How are you?/Foo3=bar4";
    QRegularExpression re("(?<key>[A-Za-z][A-Za-z0-9_]*)\\s*=\\s*(?<val>[^/]+)");
    QRegularExpressionMatchIterator i = re.globalMatch(s);
    while (i.hasNext()) {
        QRegularExpressionMatch match = i.next();
        QString key = match.captured("key");
        QString val = match.captured("val");
        qDebug() << "match: " << key << "=" << val;
    }
}

/*
RF,Kpa,230,C,30,OK*4F
RR,Kpa,230,C,30,OK*4F
LR,Kpa,230,C,30,OK*4F
LF,Kpa,230,C,30,OK*4F
*/
void test2()
{
    QRegularExpression re("(?<pos>[LR][RF]),"
                          "(?<punit>(Kpa|Psi|Bar)),"
                          "(?<press>\\d+\\.?\\d*),"
                          "(?<tunit>(C|F)),"
                          "(?<temp>\\d+),"
                          "(?<batt>(OK|LOW))");
    QString s = "RF,Kpa,230,C,30,OK*4F";
    QRegularExpressionMatch match = re.match(s);
    if (match.hasMatch()) {
        QString pos = match.captured("pos");
        QString punit = match.captured("punit");
        QString press = match.captured("press");
        QString tunit = match.captured("tunit");
        QString temp = match.captured("temp");
        QString batt = match.captured("batt");
        qDebug() << pos << punit << press << tunit << temp << batt;
    }
}

int main(int argc, char *argv[])
{
//    QCoreApplication a(argc, argv);

    testRegexp();
    test2();

    //return a.exec();
    return 0;
}

