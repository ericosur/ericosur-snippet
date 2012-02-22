#!/usr/bin/perl

# trim spaces at tail of line
# -- Aug 9 1998 by Eric
# init version

while ( <> ) {
#    my $line = $_;
#    chop($line);
#    print STDOUT "[$line]\n";
    s/\s+\n$//;

    print STDOUT "$_";
};
