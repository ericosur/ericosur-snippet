#!/usr/bin/perl
=pod

=head1 DESCRIPTION

copy from http://www.wellho.net/forum/Perl-Programming/How-to-create-a-file-with-specific-date-and-time.html

Find all files more recent than a specified time

=cut

use strict;
use Time::Local;

my ($hour, $minute, $second) = (9, 15, 0);
my ($day, $month, $year) = (1, 1, 2009);
my @queue = ("./");

my $when = timegm($second,$minute,$hour,$day,$month-1,$year%100);

while (my $current = shift @queue) {
       opendir DH,$current;
       while (my $symbol = readdir DH) {
               next if ($symbol =~ /^\.{1,2}$/);  # Skip current and parent directories
               my $locate = $current."/".$symbol;
               next if (-l $locate);  # Don't follow links
               if (-d _) {    # save directories
                       push @queue,$locate ;
                       next ;
                       }
               my $fstamp = (stat(_))[9];
               if ($fstamp > $when) {
                       my $ts = gmtime($fstamp);
                       print "$ts - $locate\n";
		}
	}
       }
