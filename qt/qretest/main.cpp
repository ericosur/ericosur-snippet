#include <QCoreApplication>
#include <QString>
#include <QRegularExpression>
#include <QDebug>

#include "qibla.h"

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


void localre(const QString& re, const QString& str)
{
    QRegularExpression regexp(re);
    QRegularExpressionMatch match = regexp.match(str);
    if (match.hasMatch()) {
        qDebug() << Q_FUNC_INFO << match.captured(1);
    } else {
        qDebug() << Q_FUNC_INFO << "no matched";
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

    localre("system: ([A-Za-z0-9.-]+)", s);
    localre("uboot: ([A-Za-z0-9.-]+)", s);
    localre("mcu:([A-Za-z0-9.-]+)", s);
    localre("lcd:([A-Za-z0-9.-]+)", s);
    localre("board id:([A-Za-z0-9.-]+)", s);
    // QString _sysinfo;
    // QRegularExpression re("system: (?<sys>[A-Za-z0-9.-]+)");
    // QRegularExpressionMatch match = re.match(s);
    // if (match.hasMatch()) {
    //     _sysinfo = match.captured("sys");
    //     qDebug() << Q_FUNC_INFO << _sysinfo;
    // } else {
    //     qDebug() << Q_FUNC_INFO << "no matched";
    // }

    // QRegularExpression re2("uboot: ([A-Za-z0-9.-]+)");
    // QRegularExpressionMatch match = re2.match(s);
    // if (match.hasMatch()) {
    //     qDebug() << match.captured(1);
    // }

}

QString translate_utf16be_to_qstring(const unsigned char utf16be[32])
{
    const int MAXLEN = 32;
    QString str = "";
    for (int i = 0; i < MAXLEN/2; i+=2) {
        //printf("i: %02x %02x\n", utf16be[i], utf16be[i+1]);
        ushort uc = (utf16be[i] << 8) | utf16be[i+1];
        if (uc == 0) {
            break;
        }
        //printf("uc: %04x\n", uc);
        QChar cc = QChar(uc);
        //qDebug() << cc;
        str = str + QString(cc);
    }

	//qDebug() << "str:" << str;
    return str;
}

/// https://en.wikipedia.org/wiki/Percent-encoding
void test4()
{
    QString s = "I%60m Lengend%21";
    QRegularExpression re("(%([A-Fa-f0-9][A-Fa-f0-9]))");
    QRegularExpressionMatchIterator i = re.globalMatch(s);
    while (i.hasNext()) {
        QRegularExpressionMatch match = i.next();
        QString all = match.captured(1);
        QString key = match.captured(2);
        bool ok;
        int _hex = key.toInt(&ok, 16);
        if (ok) {
            char value = (char)_hex;
            QString after = QString(value);
            qDebug() << "all:" << all << "key:" << key << ":" << after;
            s.replace(all, after);
            qDebug() << "s:" << s;
        }
    }
}

int main(int argc, char *argv[])
{
	Q_UNUSED(argc);
	Q_UNUSED(argv);
//    QCoreApplication a(argc, argv);

    //testRegexp();
    //test2();
    test3();
    //test4();

    // unsigned char utf16be[32] = {0x4e, 0x00, 0x58, 0x34, 0x90, 0x4a, 0x62, 0x32};
    // qDebug() << translate_utf16be_to_qstring(utf16be);

    double longitude = 121.5, latitude = 25.119904;
    qDebug() << get_qibla_angle(longitude, latitude);

    //return a.exec();
    return 0;
}
