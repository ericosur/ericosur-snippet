#ifndef __KEY_EATER_H__
#define __KEY_EATER_H__

#include <QObject>
#include <QEvent>
#include <QKeyEvent>

class KeyEater : public QObject
{
    Q_OBJECT

public:
    static KeyEater* getInstance();

protected:
    static KeyEater* _instance;
    KeyEater();

    bool eventFilter(QObject *obj, QEvent *event);
};



#endif // __KEY_EATER_H__
