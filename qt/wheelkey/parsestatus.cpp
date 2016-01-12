/// parsestatus.cpp
///

#include <QDebug>
#include <QString>
#include <QFile>
#include <QRegularExpression>

#include "parsestatus.h"

#define STATUS_FILE "/Users/ericosur/wheelkey.status"

ParseStatus::ParseStatus()
{
    loadStatus();
}

void ParseStatus::loadStatus()
{
    qDebug() << "parsestatus::loadStatus()";

    QRegularExpression re("^([a-zA-Z_-]+)\\s+(.+)$");
    //QStringList stringList;
    QFile data(STATUS_FILE);
//    if (data.exists()) {
//        qDebug() << "data.exists";
//    } else {
//        qDebug() << "data not exists";
//    }
    if (data.open(QFile::ReadOnly)) {
        QTextStream textStream(&data);
        while (true) {
            QString line = textStream.readLine();
            if (line.isNull()) {
                // no more lines
                break;
            } else {
                //qDebug() << "line: " << line;
                //stringList.append(line);
                QRegularExpressionMatch match = re.match(line);
                if (match.hasMatch()) {
                    QString key = match.captured(1);
                    QString value = match.captured(2);
                    //qDebug() << "key: " << key << " value: " << value;
                    m_map.insert(key, value);
                }
            }
        }
    } else {
        qDebug() << "QFile open failed";
    }
    emit colorChanged();
}

void ParseStatus::dumpStatus()
{
    QMapIterator<QString, QString> i(m_map);
    while (i.hasNext()) {
        i.next();
        qDebug() << i.key() << ":" << i.value();
    }
}

const QString ParseStatus::getkeyprev() const
{
    return m_map.value("key-prev", "steelblue");
}
void ParseStatus::setkeyprev(const QString& s)
{
    m_map.insert("key-prev", s);
    emit colorChanged();
}
const QString ParseStatus::getkeynext() const
{
    return m_map.value("key-next", "steelblue");
}
void ParseStatus::setkeynext(const QString& s)
{
    m_map.insert("key-next", s);
    //qDebug() << "key-next:" << m_map.value("key-next");
    emit colorChanged();
}
const QString ParseStatus::getkeyhome() const
{
    return m_map.value("key-home", "steelblue");
}
void ParseStatus::setkeyhome(const QString& s)
{
    m_map.insert("key-home", s);
    emit colorChanged();
}
const QString ParseStatus::getkeymode() const
{
    return m_map.value("key-mode", "steelblue");
}
void ParseStatus::setkeymode(const QString& s)
{
    m_map.insert("key-mode", s);
    emit colorChanged();
}
const QString ParseStatus::getkeyphone() const
{
    return m_map.value("key-phone", "steelblue");
}
void ParseStatus::setkeyphone(const QString& s)
{
    m_map.insert("key-phone", s);
    emit colorChanged();
}
const QString ParseStatus::getkeyvolup() const
{
    return m_map.value("key-volup", "steelblue");
}
void ParseStatus::setkeyvolup(const QString& s)
{
    m_map.insert("key-volup", s);
    emit colorChanged();
}
const QString ParseStatus::getkeyvoldown() const
{
    return m_map.value("key-voldown", "steelblue");
}
void ParseStatus::setkeyvoldown(const QString& s)
{
    m_map.insert("key-voldown", s);
    emit colorChanged();
}
const QString ParseStatus::getkeymute() const
{
    return m_map.value("key-mute", "steelblue");
}
void ParseStatus::setkeymute(const QString& s)
{
    m_map.insert("key-mute", s);
    emit colorChanged();
}
const QString ParseStatus::getkeyback() const
{
    return m_map.value("key-back", "steelblue");
}
void ParseStatus::setkeyback(const QString& s)
{
    m_map.insert("key-back", s);
    emit colorChanged();
}
const QString ParseStatus::getkeynavi() const
{
    return m_map.value("key-navi", "steelblue");
}
void ParseStatus::setkeynavi(const QString& s)
{
    m_map.insert("key-navi", s);
    emit colorChanged();
}
const QString ParseStatus::getmessage() const
{
    return m_map.value("message", "no message yet");
}
