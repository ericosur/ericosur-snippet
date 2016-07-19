/// file: yoseshm.h

#ifndef __YOSESHM_H__
#define __YOSESHM_H__

#include <QObject>
#include <QString>
#include <QByteArray>

typedef unsigned char byte;

class myShm : public QObject
{
    Q_OBJECT

public:
    static void saveToShm(uint32_t size, const void* buffer);
    static void readFromShm(uint32_t& size, void* buffer);
    static void removeShm();

public slots:
protected:
private:

};

#endif  // __YOSESHM_H__
