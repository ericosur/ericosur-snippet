#ifndef __LOAD_TEXT_H__
#define __LOAD_TEXT_H__

#include <QObject>
#include <QFile>
#include <QString>
#include <QDebug>

class LoadText : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString message READ text WRITE setText NOTIFY textChanged);

public:
    LoadText() {}
    ~LoadText() {}

    Q_INVOKABLE QString getTextWithId(int id);
    Q_INVOKABLE QString getText() {
        return m_text;
    }

    QString text();
    void setText(const QString& str);

signals:
    void textChanged();

private:
    QString m_text = "";
};

#endif  // __LOAD_TEXT_H__
