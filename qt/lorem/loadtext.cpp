#include "loadtext.h"

LoadText::LoadText()
{
    m_map.insert(LangEn, "en_US");
    m_map.insert(LangAr, "ar_AE");
    m_map.insert(LangPt, "pt_PT");
    m_map.insert(LangFr, "fr_FR");
    m_map.insert(LangEs, "es_ES");
    m_map.insert(LangRu, "ru_RU");
    m_map.insert(LangUk, "uk_UK");
    m_map.insert(LangJa, "ja_JP");
}

QString LoadText::message()
{
    return m_text;
}

void LoadText::setMessage(const QString& str)
{
    if (str == m_text) {
        // do nothing
        qWarning() << "do nothing...";
        return;
    }
    m_text = str;
    emit messageChanged();
}

QString LoadText::getTextWithId(LangType id)
{
    QString fn;
    QString content;
    qDebug() << Q_FUNC_INFO << "id:" << id;
    if (m_map.contains(id)) {
        fn = QString(":/txt/%1.txt").arg(m_map.value(id));
        content = readTextfile(fn);
#ifdef Q_WS_WIN
        //content = content.toLocal8Bit();
#endif
    }
    QString str = QString("get with id: %1\n%2").arg(fn)
            .arg(content);
    setMessage(str);
    //qDebug() << "str:" << str;

    return str;
}

QString LoadText::readTextfile(const QString& fn)
{
    qDebug() << "fn:" << fn;
    QFile data(fn);
    QString str;
    if (data.open(QFile::ReadOnly | QFile::Text)) {
        QTextStream textStream(&data);
        while (true) {
            QString line = textStream.readLine();
            if (line.isNull()) {
                break;
            }
            else {
                //qDebug() << line;
                str = str + line;
            }
        }
    }
    return str;
}
