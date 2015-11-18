#ifndef MYHANDLER_H
#define MYHANDLER_H

#include <QObject>

class MyHandler : public QObject
{
    Q_OBJECT
public:
    MyHandler();
    ~MyHandler() {}

private:


//signals:


public slots:
    void handleSignal(const QString& str);

};

#endif // MYHANDLER_H

