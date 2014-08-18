#!/usr/bin/perl
#
# re.pl
#
# July 17 2002 by ericosur
# 拿來作 regular expression 的測試
# 從stdin輸入

my $line;

$line = 0;

print "please input from STDIN...\n";

LOOP:
  while ( <STDIN> )  {
    chop;

    $line++;

    next if /^\s*\/\//;
#    if ( /\/\// )
#    {
        print "$line: $_\n";
#    }

#    (print "$line: $_\n", next LOOP) if $_ =~ /\bvoid\b/;
#    (print "$line: $_\n", next LOOP) if $_ =~ /\bint\b/;
    #(print "$line: $_\n", next LOOP) if $_ =~ /.*\(.*\)\;$/;
}
