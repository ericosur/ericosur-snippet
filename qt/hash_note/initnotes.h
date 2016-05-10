/// file: initnotes.h
#ifndef INITNOTES_H
#define INITNOTES_H

#include <QHash>
#include <QString>

typedef QHash<QString, int> hash_note;

hash_note initHashnote();
extern hash_note myhash;

#endif // INITNOTES_H
