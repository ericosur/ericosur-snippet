@echo off
rem Create drop-down shadow with ImageMagick

convert -depth 8 -threshold 0 -negate tree.jpg -bordercolor #ffffff -border 20x20 -gaussian 0x7 -shave 15x15 tmp.jpg
composite -geometry +2+2 -gravity northwest tree.jpg tmp.jpg out.jpg

del tmp.jpg

:end
