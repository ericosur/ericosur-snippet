#include "idhash.h"

#include <stdio.h>

void IdHash::dumpToFile(const QString& fn)
{
    qDebug() << Q_FUNC_INFO << "to file:" << fn;
    FILE* fptr = fopen(fn.toUtf8().constData(), "w");
    if (fptr == NULL) {
        qWarning() << "cannot output to file:" << fn;
        return;
    }
    foreach (QString key, mFile2IdHash.keys()) {
        fprintf(fptr, "\"%s\",\"%d\"\n", key.toUtf8().constData(),
            mFile2IdHash.value(key));
    }
    fclose(fptr);

    if (mFile2IdHash.size() != mId2FileHash.size()) {
        qWarning() << "size mismatched!!!";
    }
    qDebug() << Q_FUNC_INFO << "end of dump...";
}
