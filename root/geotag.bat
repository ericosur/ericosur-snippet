@echo off

rem use gpsPhoto.pl to geotag

perl gpsPhoto.pl --gpsfile 1.gpx --gpsfile 2.gpx --gpsfile 3.gpx --image-file-time=exif --overwrite-geotagged --timeoffset=-28800 --maxtimediff=600 --dir=c:\Users\ericosur\Pictures\nex5\

goto end

rem exiftool -AllDates-='0:0:0 8:0:0' -overwrite_original *.jpg
rem gpsphoto.pl -dir=D:\TEMP\123 -timeoffset=-28800 -gpsfile=1.gpx -gpsfile=2.GPX -maxtimediff=1000 -kml=2.kml

rem exiftool "-AllDates+='5:10:2 10:48:0" -overwrite_original *.nef

rem exiftool -TagsFromFile a.jpg -GPSLatitude -GPSLatitudeRef -GPSLongitude -GPSLongitudeRef -GPSAltitude -GPSAltitudeRef dst.cr2

rem exiftool -GPSLatitude=43,22,1.41 -GPSLongitude=8,24,8.56 -GPSLatitudeRef=N -GPSLongitudeRef=W -GPSAltitude=5 -GPSAltitudeRef="Above Sea Level" -GPSMapDatum=WGS84 -GPSDestLatitude=43,22,2.84 -GPSDestLongitude=8,24,8.65 -GPSDestLongitudeRef=W -GPSDestLatitudeRef=N -overwrite_original dst.jpg

:end
