/// file: util.cpp

#include <taglib/taglib.h>
#include <taglib/tmap.h>
#include <taglib/tstring.h>
#include <taglib/id3v1tag.h>
#include <taglib/id3v2tag.h>
#include <taglib/mpegfile.h>
#include <taglib/id3v2frame.h>


#include "util.h"

bool hasAPETag(const QString& fn)
{
    TagLib::MPEG::File file(fn.toStdString().c_str());
    if (!file.isValid()) {
        return false;
    }
    return file.hasAPETag();
}
