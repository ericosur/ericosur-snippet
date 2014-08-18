#!/bin/sh
#gcc -o dcraw -O4 dcraw.c -lm -ljpeg -llcms
#gcc -o dcraw -O4 dcraw.c -lm -DNO_JPEG -DNO_LCMS

CC=i586-mingw32msvc-gcc

# for mingw32
#$CC -o dcraw -O4 dcraw.c -lm -lwsock32 -DNO_JPEG -DNO_LCMS
$CC -o dcraw -O4 dcraw.c -lm -DNO_JPEG -DNO_LCMS

