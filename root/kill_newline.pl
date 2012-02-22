#!/usr/bin/perl -w

#@ 由於 DOS 的 dir /b 是以 \r\n 作換行
#@ 只用 chomp 只會把 \n 去掉，而不會把 \r 去掉
#@ 所以要再多作一個動作去除 \r


while ( <> )
{
    chomp;
    s/\r//;
    print "$_\n";
}

#
# 2006/12/27 by ericosur
# now I use the stupid way:
# s/\n//;
# s/\r//;
#
