@echo off

echo build file list
dir /s /b *.jpg > list.txt

echo get model info from EXIF
perl D:\ericosur-google\model_analysis\get_exif_model.pl

echo sum up the model statics
perl D:\ericosur-google\model_analysis\ana_model.pl

