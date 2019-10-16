@echo off
set a=-GPSLatitude=25.07575 -GPSLatitudeRef=N
set b=-GPSLongitude=121.56157  -GPSLongitudeRef=E
set c=-GPSAltitude=20 -GPSAltitudeRef="Above Sea Level"
rem set d=-GPSMapDatum=WGS84
set misc=-overwrite_original

rem -GPSDestLatitude=43,22,2.84 -GPSDestLongitude=8,24,8.65
rem set eee=-GPSDestLongitudeRef=W -GPSDestLatitudeRef=N

perl "D:\tool\Exiftool\Image-ExifTool-7.08\exiftool" %a% %b% %c% %misc% %1


rem set a=-GPSLatitude=43,22,1.41 -GPSLatitudeRef=N
rem set b=-GPSLongitude=8,24,8.56  -GPSLongitudeRef=E
rem N25.07575 E121.56157
