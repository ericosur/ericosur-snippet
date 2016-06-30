#Gutenberg

##purpose:
try to extract words from gutenberg ebooks

##how to:
* remove bomb from downloaded books
```
rmbom.pl
```
pg*.txt -> nobomb*.txt

* extract words from books
```
extract-word.pl
```
nobomb*.txt -> extracted*.txt

* combine extracted words into one text file
```
combine-word.pl
```
extracted*.txt -> combined.txt

##note
reference and books come from:
http://www.gutenberg.org/
