#!/usr/bin/perl

use strict;

sub main()
{
	my $file = $ARGV[0] || "out.txt";
	my $ifh;

	open $ifh, $file or die;
	my @pair = ();

	while (<$ifh>)  {
		push @pair, $_;
	}

	close $ifh;

	my $max = scalar @pair;
	print "size from file: $max\n";

	go(\@pair);
}


sub cleanup($)
{
	my $inarr = shift;
	my @outarr = ();

	foreach (@$inarr)  {
		if (substr($_, 0, 1) eq 'x')  {
			#print '.';
			next;
		}
		push @outarr, $_;
	}

	#print "cleanup(): $#outarr\n";
	return @outarr;
}

sub go($)
{
	my $arr_ref = shift;
	my @arr = @$arr_ref;
	my $size = $#arr + 1;
	my $jj;
	my $pass = 0;

	print "init size: $size\n";

	while ( $size > 1)  {

		$pass ++;
		print "pass($pass), size($size)\n";

		for (my $jj=0; $jj<$size-1; ++$jj)  {

			if ( (substr($arr[$jj], 0, 1) eq '+') && (substr($arr[$jj+1], 0, 1) eq '-') )  {
				#print $arr[$jj];
				#print $arr[$jj+1];
				#print '-' x 60, "\n";
				substr($arr[$jj], 0, 1) = 'x';
				substr($arr[$jj+1], 0, 1) = 'x';
				$jj++;
			}
		}

		@arr = cleanup(\@arr);
		$size = $#arr + 1;
		print "pass($pass), after cleanup, size($size)\n";

		# 防止迴圈不會收斂
		goto EOP if ($pass > 10 || $size < 10);

	}	# end of while
EOP:

	print "remaining...\n";	# 還在迴圈內的項目嫌疑最大
	foreach (@arr)  {
		print;
	}

}


main;
