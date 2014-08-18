#!/usr/bin/perl
#
# code snippet from
# http://www.perlmonks.org/?node_id=410615
#

use strict;
use warnings;

use POSIX ();

my $dir = ".";

opendir(DIR, $dir);
my @dir = grep { !/^\.+$/ } readdir(DIR);
closedir(DIR);

foreach (@dir)
{
   my $file = "$dir/$_";
   my $mtime = (stat($file))[9];
   print "Last change:\t"
      . POSIX::strftime("%Y%m%d", localtime($mtime))
      . "\n";
}
