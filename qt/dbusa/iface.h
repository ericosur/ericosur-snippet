#ifndef __IFACE_H__
#define __IFACE_H__
// iface.h

#include <QObject>

class interfacedescription : public QObject
{
    Q_OBJECT

public:
   interfacedescription();

public slots:
   QString read();
   QString write();
   QString SendMessage(const QString &cmd);

Q_SIGNALS:
   void somethingHappened(const QString &signalMessage);
};

#endif
