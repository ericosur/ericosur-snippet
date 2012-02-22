#!/usr/bin/perl

# copy from http://www.wellho.net/forum/Perl-Programming/How-to-create-a-file-with-specific-date-and-time.html

#%% Find all files more recent than a specified time

use Time::Local;

$hour = 9;
$minute = 15;
$second = 0;

$day = 1;
$month = 1;
$year = 2009;

@queue = ("./");

$when = timegm($second,$minute,$hour,$day,$month-1,$year%100);

while ($current = shift @queue) {
       opendir DH,$current;
       while ($symbol = readdir DH) {
               next if ($symbol =~ /^\.{1,2}$/);  # Skip current and parent directories
               $locate = $current."/".$symbol;
               next if (-l $locate);  # Don't follow links
               if (-d _) {    # save directories
                       push @queue,$locate ;
                       next ;
                       }
               $fstamp = (stat(_))[9];
               if ($fstamp > $when) {
                       $ts = gmtime($fstamp);
                       print "$ts - $locate\n";
                       }
               }
       }
