#ifndef __READ_THREAD_H__
#define __READ_THREAD_H__

#include <QObject>
#include <QThread>
#include <QString>
#include <QDebug>

#include "fileitem.h"
#include "util.h"
#include "commonutil.h"

class ReadThread : public QThread
{
    Q_OBJECT

public:
    ReadThread();

    void setReadItemType(ItemType it) {
        mItemType = it;
    }
    ItemType getReadItemType() {
        return mItemType;
    }

    void run();

protected:

private:
    FileItem* fi = NULL;
    ItemType mItemType = NO_ITEM;
};

#endif // __READ_THREAD_H__
