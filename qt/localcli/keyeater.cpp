#include "keyeater.h"

KeyEater* KeyEater::_instance = NULL;
KeyEater* KeyEater::getInstance()
{
    if (_instance == NULL) {
        _instance = new KeyEater;
    }
    return _instance;
}

KeyEater::KeyEater()
{

}

bool KeyEater::eventFilter(QObject *obj, QEvent *event)
{
    if (event->type() == QEvent::KeyPress) {
        QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
        qDebug("Ate key press %d/%d", keyEvent->key(), keyEvent->nativeScanCode());
        return true;
    } else {
        // standard event processing
        return QObject::eventFilter(obj, event);
    }
}
