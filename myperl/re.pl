#!/usr/bin/perl
#
# re.pl
#
# July 17 2002 by Eric
# ���ӧ@ regular expression ������
# �qstdin��J

my $line;

$line = 0;

LOOP:
  while ( <STDIN> )  {
    chop;

    $line++;

    s/\s*$//;
#    if ( /\/\// )
#    {
        print "$line: <$_>\n";
#    }

#    (print "$line: $_\n", next LOOP) if $_ =~ /\bvoid\b/;
#    (print "$line: $_\n", next LOOP) if $_ =~ /\bint\b/;
    #(print "$line: $_\n", next LOOP) if $_ =~ /.*\(.*\)\;$/;
}
