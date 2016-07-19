#ifndef __MYDATASOURCE_H__
#define __MYDATASOURCE_H__

#include <QObject>
#include <QString>
#include <QByteArray>

class myDataSource : public QObject
{
    Q_OBJECT

public:
    Q_INVOKABLE void loadAction();
    Q_INVOKABLE void checkAction();
    Q_INVOKABLE void quitAction();

    myDataSource();

public slots:
    void sltRead(const QString& s);
    void sltMd5sum(const QString& s);
    void sltWrite();

signals:
    void sigAskQuit();

protected:
    void readFromShared();
    void writeToShared();

private:
};

#endif  // __MYDATASOURCE_H__
