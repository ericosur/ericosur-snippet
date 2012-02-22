#!/usr/bin/perl
#
# to process 2to3 result
#

$file = '1.txt';
open my $ifh, $file or die;
my $cnt = 0;
my $flag = 0;


while (<$ifh>)  {
	#print $_;
	if ( m/^---/ )  {
		if ($flag == 1)  {	# already in section ?
			$flag = 0;
			$cnt ++;
			close $ofh;
		}

		$flag = 1;
		$ofile = sprintf("d%02d.diff", $cnt);
		print "output to $ofile\n";
		open $ofh, "> $ofile" or die;
		print $ofh $_;
		#print $_;
	}
	else  {
		if ($ofh)  {
			print $ofh $_;
			#print $_;
		}
		else  {
			print "no output file handler\n";
		}
	}
}

close $ifh;
close $ofh;
