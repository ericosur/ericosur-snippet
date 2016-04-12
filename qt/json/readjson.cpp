/// file: readjson.cpp

// simple class to use QJsonDocument and QJsonObject

#include <QFile>
#include <QIODevice>
#include <QJsonDocument>
#include <QDebug>

#include "readjson.h"

ReadJson::ReadJson(const QString &f) :
    m_file(f)
{

}

bool ReadJson::loadFile()
{
    if (m_file == "") {
        qWarning("file name not specified");
        return false;
    } else {
        return loadFile(m_file);
    }
}

bool ReadJson::loadFile(const QString &filename)
{
    QFile f(filename);

    if (!f.open(QIODevice::ReadOnly)) {
        qWarning("Couldn't open save file.");
        return false;
    }

    QByteArray saveData = f.readAll();
    QJsonDocument loadDoc( QJsonDocument::fromJson(saveData) );
    read(loadDoc.object());

    return true;
}

void ReadJson::read(const QJsonObject &json)
{
    QJsonObject item = (((json["query"].toObject())["results"].toObject())["channel"].toObject())["item"].toObject();
    qDebug() << item;
    qDebug() << (item["condition"].toObject())["temp"].toString();
    qDebug() << (item["condition"].toObject())["text"].toString();
}
