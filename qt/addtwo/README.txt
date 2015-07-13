refer to http://stackoverflow.com/questions/6127357/building-qt-creator-projects-from-command-line

$ cd path/to/project/
$ mkdir build/
$ cd build/
$ qmake ../proj.pro
$ make

HOW TO ADD TS/QM

$ lupdate addtwo.pro -ts lang_zh_TW.ts
$ lupdate addtwo.pro -ts lang_en_US.ts

$ subl lang_en_US.ts

$ lrelease addtwo.pro


