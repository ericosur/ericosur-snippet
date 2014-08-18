#!/usr/bin/perl
#
# findinc.pl
#
# July 17 2002 by Eric
#    �C�X��l�X�ҥΨ쪺 #include files
#    �q stdin ��J
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
