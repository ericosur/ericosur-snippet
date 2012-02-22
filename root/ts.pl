#!/usr/bin/perl

=pod

=head1 NAME

Count the number of the lines containing trailing white spaces in the file

=head1 NOTE

init version Aug 7 1998 by ericosur

=cut


use strict;
use warnings;

sub process
{
  LOOP:
    foreach ( @_ ) {
        my $file_name = $_;
        open(FILE, $file_name) or die "Can't open $file_name: $!";
        print STDERR "Read from [$file_name]:\n";
        my $cnt = 0;
        my $line = 0;
      READLINE:
        while (<FILE>) {
            $line++;
            if ( /\s+\n$/ ) {
                $cnt ++;
                # print STDOUT "#$line: $_";
            }
        }
        print "$0: space trailing lines = $cnt\n" if $cnt != 0;
    }
}

# main procedure start here
@ARGV = ('-') unless @ARGV;
process(@ARGV);
