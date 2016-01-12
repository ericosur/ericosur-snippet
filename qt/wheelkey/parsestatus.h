#ifndef PARSESTATUS_H
#define PARSESTATUS_H

#include <QObject>
#include <QMap>

class ParseStatus : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString keyprev READ getkeyprev WRITE setkeyprev NOTIFY colorChanged)
    Q_PROPERTY(QString keynext READ getkeynext WRITE setkeynext NOTIFY colorChanged)
    Q_PROPERTY(QString keyhome READ getkeyhome WRITE setkeyhome NOTIFY colorChanged)
    Q_PROPERTY(QString keymode READ getkeymode WRITE setkeymode NOTIFY colorChanged)
    Q_PROPERTY(QString keyphone READ getkeyphone WRITE setkeyphone NOTIFY colorChanged)
    Q_PROPERTY(QString keyvolup READ getkeyvolup WRITE setkeyvolup NOTIFY colorChanged)
    Q_PROPERTY(QString keyvoldown READ getkeyvoldown WRITE setkeyvoldown NOTIFY colorChanged)
    Q_PROPERTY(QString keymute READ getkeymute WRITE setkeymute NOTIFY colorChanged)
    Q_PROPERTY(QString keyback READ getkeyback WRITE setkeyback NOTIFY colorChanged)
    Q_PROPERTY(QString keynavi READ getkeynavi WRITE setkeynavi NOTIFY colorChanged)
    Q_PROPERTY(QString message READ getmessage NOTIFY colorChanged)

public:
    ParseStatus();
    ~ParseStatus() {}

    Q_INVOKABLE void loadStatus();
    Q_INVOKABLE void dumpStatus();

    const QString getkeyprev() const;
    void setkeyprev(const QString& s);
    const QString getkeynext() const;
    void setkeynext(const QString& s);
    const QString getkeyhome() const;
    void setkeyhome(const QString& s);
    const QString getkeymode() const;
    void setkeymode(const QString& s);
    const QString getkeyphone() const;
    void setkeyphone(const QString& s);
    const QString getkeyvolup() const;
    void setkeyvolup(const QString& s);
    const QString getkeyvoldown() const;
    void setkeyvoldown(const QString& s);
    const QString getkeymute() const;
    void setkeymute(const QString& s);
    const QString getkeyback() const;
    void setkeyback(const QString& s);
    const QString getkeynavi() const;
    void setkeynavi(const QString& s);
    const QString getmessage() const;

signals:
    void colorChanged();

private:
    QMap<QString, QString> m_map;
};

#endif // PARSESTATUS_H
