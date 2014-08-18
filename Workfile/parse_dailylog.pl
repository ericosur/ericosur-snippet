#!/usr/bin/perl

# parse DailyNote.txt into sections
#
# not applicable to new dailynote.txt
# it was used to refresh the format of old one.
#
# 2006/12/27 by ericosur

use strict;
use warnings;


my $file = "DailyNote.txt";
my $month = defined;
my $day = "15";

if ($month ne undef)  {
	print "$month, ";
}
elsif ($day ne undef)  {
	print "$day";
}
print "\n";

open IFH, $file or die "cannot open file: $!\n";

my $pattern = "^(\\w{3})\\s+(\\d+)\\s+(\\d+)\\s+(\\w{3})";

ONE:
while ( <IFH> )  {
	if ( /$pattern/ )  {

		#debug
		#print "$1/$2/$3 is $4\n";

		# compare the day
		if ($day eq $2)  {
			print $_;
		} else  {
			next ONE;
		}


		LINE: while ( <IFH> )  {
			if ( /$pattern/ )  {
				if ( $month eq defined )  {
					next ONE;
				}
				#else  {
				#	last ONE;
				#}
			} else  {
				print $_;
			}
		}
	}
}

close IFH;
