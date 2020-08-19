#Gutenberg

##purpose
Try to extract words from gutenberg ebooks to
**compose a _not-so-good_ dictionary**.

##how to

The following scripts will take all wanted list automatically.

* [rmbom.pl](./rmbom.pl) remove bomb from downloaded books, translate:
```
pg*.txt -> nobomb*.txt
```

* [extract-word.pl](./extract-word.pl) extract words from books
```
nobomb*.txt -> extracted*.txt
```

* [combine-word.pl](./combine-word.pl) combine extracted words into one text file
```
extracted*.txt -> combined.txt
```

* [build-all.bat](./build-all.bat) will take all steps in one batch

##note
reference and books come from:
https://www.gutenberg.org/
