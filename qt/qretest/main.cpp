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

void test3()
{
    char s[] =
"system: CIS002-0.01.001.201609082206\x0a"
"uboot: 40\x0a"
"mcu:201608030004\x0a"
"lcd:201609130008\x0a"
"board id:2\x0a";

    QRegularExpression re("(?<sys>system: [A-Za-z0-9.-]+)");
    QRegularExpressionMatch match = re.match(s);
    if (match.hasMatch()) {
        QString pos = match.captured("sys");
        qDebug() << pos;
    }
}

void test_qchar()
{
	QChar c1 = QChar(0x4e2d);
	QChar c2 = QChar(0x6587);
	qDebug() << "digit val:" << c1.digitValue();
	qDebug() << "unicode:" << QString::number(c1.unicode(), 16);
	QString s = QString(c1) + c2;
	qDebug() << "s:" << s;
}

int main(int argc, char *argv[])
{
	Q_UNUSED(argc);
	Q_UNUSED(argv);
//    QCoreApplication a(argc, argv);

    //testRegexp();
    //test2();
    test3();
    test_qchar();
    //return a.exec();
    return 0;
}

