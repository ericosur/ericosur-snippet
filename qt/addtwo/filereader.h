#ifndef __FILE_READER_H__
#define __FILE_READER_H__

#include <QObject>
#include <QString>
#include <QDebug>

#include <QImage>

class FileReader : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString filename READ getFilename)

public:
    FileReader(const QString& fn);
    ~FileReader();

    QString getFilename() const {
        return m_filename;
    }

    Q_INVOKABLE QString queryString(const QString& query);

protected:
    void readTextfile();

private:
    QString m_filename;
    QStringList m_strlist;

};


#endif // __FILE_READER_H__
