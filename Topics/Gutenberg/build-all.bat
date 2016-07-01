@echo off
tar xvJf pgfiles.tar.xz
mv backup/*.txt ./
rmdir backup
perl rmbom.pl
perl extract-word.pl
perl combine-word.pl

rm pg*.txt
rm nobomb*.txt
rm extracted*.txt
