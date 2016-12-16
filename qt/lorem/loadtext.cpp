#include "loadtext.h"

QString LoadText::text()
{
    return "hello world";
}

void LoadText::setText(const QString& str)
{
    if (str == m_text) {
        // do nothing
        qWarning() << "do nothing...";
        return;
    }
    m_text = str;
    emit textChanged();
}

QString LoadText::getTextWithId(int id)
{
    QString str = QString("get with id: %1").arg(id);
    setText(str);
    qDebug() << "str:" << str;

    return str;
}
