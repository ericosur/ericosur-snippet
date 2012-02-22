July 25 2006 by ericosur

1. first, make a file list using 'dir'
> dir /s/b/a-d d:\src > filelist.txt

2. run mkduplist.pl, this script need file
   'filelist.txt'and generate 'filedata.ph'

3. run 'finddup.pl', and output to STDOUT



Feb 12 2008

md5_list.pl (need ''list.txt'', output to ''md5.txt'')
get_dup.pl (need ''md5.txt'', output to STDOUT)

