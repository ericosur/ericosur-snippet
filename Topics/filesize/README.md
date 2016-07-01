# Filesize #

The purpose for this sub-project is to calculate the total size
from a given file list.

How to use:

```
dir /s/b d:\path > list.txt
add_size.pl list.txt filesize.txt
calc_total_size.pl filesize.txt
```
