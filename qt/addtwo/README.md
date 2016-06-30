# Qt addtwo sample code

## files

  [mytranslation.hpp](./mytranslation.hpp)  class to load specified translation

  [kill_unfinish.pl](./kill_unfinish.pl)  perl script to remove **unfinished** string in ts files

## build qt project from command line

refer to http://stackoverflow.com/questions/6127357/building-qt-creator-projects-from-command-line

```
cd path/to/project/
mkdir build/
cd build/
qmake ../proj.pro
make
```

## How to add qt translation resource

```
lupdate addtwo.pro -ts lang_zh_TW.ts
lupdate addtwo.pro -ts lang_en_US.ts
```

add translated string token into ts files

```
lrelease addtwo.pro
```

add qm into qml.qrc for qrc loading
