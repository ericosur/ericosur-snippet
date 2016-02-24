#include "filereader.h"

#include <stdio.h>
#include <string.h>

#include <QDebug>
#include <QFile>


FileReader::FileReader() :
    m_filename("")
{
    //readTextfile();
}

FileReader::~FileReader()
{
}

void FileReader::readTextfile()
{
    QFile data(m_filename);
    if (data.open(QFile::ReadOnly)) {
        QTextStream textStream(&data);
        while (true) {
            QString line = textStream.readLine();
            if (line.isNull()) {
                break;
            }
            else {
                //qDebug() << line;
                m_strlist.append(line);
            }
        }
    }
}

QString FileReader::queryString(const QString& query)
{
    QRegExp rx(query);

    for (int i = 0; i < m_strlist.size(); ++i) {
        QString str = m_strlist.at(i);
        if ( str.contains(rx) ) {

        }
    }
    return QString("");
}
