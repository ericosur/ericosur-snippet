#ifndef __QFoo_H__
#define __QFoo_H__

#include <QObject>

class QFoo : public QObject
{
    Q_OBJECT

public:
    QFoo();

public slots:
    void sltTitle();
    void sltName();
    void sltNumber();

private:
};

#endif  // __QFoo_H__
