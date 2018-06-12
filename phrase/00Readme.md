# phrase

---

[TOC]

---

## reference

[main.txt](./main.txt) is downloaded from [phrash dictionary](https://github.com/samejack/sc-dictionary)

*mygrep.pl* will filter out:
  * start with 0-9 a-z A-Z and chinese number characters.
  * more than 4 zh characters

and outputs two files:
  * out.txt - plain text one phrase one line,
  * storable.dat - perl storable data file, containing a perl array. You may use
  *listarr.pl* to pick 10 random phrase from array.

## helper scripts and setting.json

[mygrep.pl](./mygrep.pl) will filter out unwanted lines from main.txt
[listarr.pl](./listarr.pl) read from storage.dat and pick some items to ofile

* common:
    * ifile: path to phrase dictionary, one phrase/word one line
    * ofile: output text file
    * datafile: perl storage data file
* listarr.pl:
    * ofile: output json file
    * repeat: number of picked items
