finddup
=======

Simple scripts to find duplicated from given file list.

***___Need review this folder and update readme.___***

### How to Use ###

1. first, make a file list named __filelist.txt__
  ```
  dir /s /b /a-d d:\src > filelist.txt
  ```
2. run script, input filelist.txt and output filedata.ph
  ```
  perl mkduplist.pl
  ```
3. run 'finddup.pl', and output to STDOUT

### updated ###

md5_list.pl (need ''list.txt'', output to ''md5.txt'')
get_dup.pl (need ''md5.txt'', output to STDOUT)
