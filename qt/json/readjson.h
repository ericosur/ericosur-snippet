#ifndef READJSON_H
#define READJSON_H

#include <QString>
#include <QJsonObject>

class ReadJson {
public:
    ReadJson(const QString& f);
    bool loadFile();
    bool loadFile(const QString& filename);
    void read(const QJsonObject &json);
private:
    QString m_file;
};

#endif // READJSON_H
