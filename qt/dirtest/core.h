#ifndef __CORE_H__
#define __CORE_H__

#include <QObject>
#include <QString>
#include <QStringList>

class Core : public QObject
{
    Q_OBJECT

public:
    static Core* _instance;
    static Core* getInstance();

    void start(const QString& startpath);
    qlonglong imageSpace(const QString &path);

//signals:
    //void sigQuit();

//public slots:
    // void sltWaitFinished();
    // void sltUsbDetected();
    // void sltIpodDetected();

protected:
    Core();

private:
    QStringList filters;
};

#endif  // __CORE_H__
