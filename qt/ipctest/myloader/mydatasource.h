#ifndef __MYDATASOURCE_H__
#define __MYDATASOURCE_H__

#include <QObject>
#include <QString>
#include <QSharedMemory>
#include <QByteArray>

class myDataSource : public QObject
{
    Q_OBJECT

public:
    Q_INVOKABLE void loadAction();
    Q_INVOKABLE void checkAction();

    myDataSource();

public slots:
    void sltRead(const QString& s);
    void sltMd5sum(const QString& s);
    void sltWrite();

protected:
    void readFromShared();
    void writeToShared();

private:
    QSharedMemory *m_shared;
    QByteArray *m_arr;
};

#endif  // __MYDATASOURCE_H__
