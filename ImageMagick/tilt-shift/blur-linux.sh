#!/bin/sh

# copy from image magick tips site

IN=in.jpg
TMP=tmp.jpg
OUT=out.jpg

convert $IN -sigmoidal-contrast 15x40% $TMP
convert $TMP -sparse-color Barycentric '0,0 black 0,%h white' -function polynomial 4,-4,1 blur.jpg
convert $TMP blur.jpg -compose Blur -set option:compose:args 10 -composite $OUT

