#ifndef __LOAD_TEXT_H__
#define __LOAD_TEXT_H__

#include <QObject>
#include <QFile>
#include <QString>
#include <QMap>
#include <QDebug>

class LoadText : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString message READ message WRITE setMessage NOTIFY messageChanged)

public:
    enum LangType {
        LangNull = 0,
        LangEn = 1,
        LangAr,
        LangPt,
        LangFr,
        LangEs,
        LangRu,
        LangUk,
        LangJa,
    };

    Q_ENUMS(LangType)

public:
    LoadText();
    ~LoadText() {}

    Q_INVOKABLE QString getTextWithId(LangType id);

    QString message();
    void setMessage(const QString& str);
    QString readTextfile(const QString& fn);

signals:
    void messageChanged();

private:
    QMap<LangType, QString> m_map;
    QString m_text = "";
};

#endif  // __LOAD_TEXT_H__
