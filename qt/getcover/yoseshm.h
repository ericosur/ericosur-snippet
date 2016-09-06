/**
    \file yoseshm.h
    \brief raw shm functions
**/


#ifndef __YOSESHM_H__
#define __YOSESHM_H__

#include <QObject>
#include <QString>
#include <QByteArray>

#define SHMKEY  0x0111C0DE

typedef unsigned char byte;

class myShm : public QObject
{
    Q_OBJECT

public:
    static void saveToShm(uint32_t size, const void* buffer);
    static void readFromShm(uint32_t& size, void* buffer);
    static void removeShm();

};

#endif  // __YOSESHM_H__
