#ifndef __QBAR_H__
#define __QBAR_H__

#include <QObject>
#include <QString>

class QBar : public QObject
{
	Q_OBJECT
public:
    Q_PROPERTY(QString title READ title WRITE setTitle NOTIFY titleChanged)
    Q_PROPERTY(QString name READ name WRITE setName NOTIFY nameChanged)
    Q_PROPERTY(QString number READ number WRITE setNumber NOTIFY numberChanged)

    QString title() const;
    void setTitle(const QString& s);
    QString name() const;
    void setName(const QString& s);
    QString number() const;
    void setNumber(const QString& s);
public:
    QBar();

    void load();
    void save();
    void show();

    friend QDataStream& operator<<(QDataStream& ds, const QBar& obj);
    friend QDataStream& operator>>(QDataStream& ds, QBar& obj);

signals:
    void titleChanged();
    void nameChanged();
    void numberChanged();

private:
    QString m_title;
    QString m_name;
    QString m_number;
};


#endif	// __QBAR_H__
