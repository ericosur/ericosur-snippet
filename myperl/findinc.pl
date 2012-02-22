#!/usr/bin/perl
#
# findinc.pl
#
# July 17 2002 by Eric
#    列出原始碼所用到的 #include files
#    從 stdin 輸入
#

my $line;

$line = 0;
while ( <STDIN> )
{
    chop;

    next unless /^\s*#\s*include\s+([<"]\S+[>"])/;
    print "$1\n";
    $line ++;
}
print "\n$line include files\n";
