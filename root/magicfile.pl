#!/usr/bin/perl
#
# using simple magic number from file to recognize file type
# support wildcard
#

use strict;
use warnings;

my $count = 0;	# total processed files count
my $bmp_count = 0;	# windows bitmap files count

sub main();
sub process($);
sub get_filename_from_list($);
sub is_windows_bmp($);

# only four file type recognized
my @magic_number = (
		{ format_name => 'bmp', magic_number => '424d' },
		{ format_name => 'gif', magic_number => '47494638' },
		{ format_name => 'jpeg', magic_number => 'ffd8ffe0' },
		{ format_name => 'jpeg', magic_number => 'ffd8ffe1' },
		{ format_name => 'png', magic_number => '89504e47' },
	);

# total, bmp, gif, jpeg, png, unknown
my %count = ();

sub main()
{
	if (@ARGV)  {
		foreach (@ARGV)  {
			if ( /\*|\?/ )  {			# if contains '*' or '?'
				#print "glob...'$_'\n";
				my @filelist = glob($_);
				foreach ( @filelist )  {
					process($_) if ( -f $_ );	# file only
				}
			}
			elsif ( /@/ ) {
				s/@//;
				get_filename_from_list($_);
			}
			else  {		# without wildcard
				process($_);
			}
		}
		# show the result
		foreach (keys %count)  {
			printf "%s => %s\n", $_, $count{$_};
		}
#		printf "%d bitmap files, %d files checked\n", $bmp_count, $count;
	}
	else  {
	    print <<EOL;
By inspecting magic number in the head of image files to guess the file type
EOL

		printf "\n%s <filename> [\@list file] [filenames...] \n", $0;
	}
}


# just take one argument and print it out
sub process($)
{
	my $file = shift;
#	print "$file: ";

	# only files are accepted
	if (-f $file)  {
		++ $count{total};
		match_magic_number($file);
	}
}


sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;
	while (<FH>)
	{
		s/[\r\n]//;
		#print $_;
		process($_);
	}
	close FH;
}


sub match_magic_number($)
{
	my $ifile = shift;
	my $ifh;
	my $buf;
	my $matched = 0;

	my $common_magic_number_length = 4;

	# get 4 bytes from file to inspact
	open $ifh, $ifile or die;
	binmode($ifh);
	read($ifh, $buf, $common_magic_number_length, 0);
	close $ifh;

    print $ifile, " ";

	foreach my $mn (@magic_number)  {
		#print "try ", $mn->{format_name},"\n";
		my $len = length($mn->{magic_number})/2;
		my $fmt = sprintf("H%d", $len*2);
		my $cmp_magic = pack($fmt, $mn->{magic_number});
		$common_magic_number_length = length($cmp_magic);
		if ($len != $common_magic_number_length)  {
			$buf = substr($buf, 0, $len);
			printf "%d vs %d buf truncated.\n", $len, $common_magic_number_length;
		}
		if ($cmp_magic eq $buf)  {
			++ $count{ $mn->{format_name} };
			$matched = 1;
			print "matched: ", $mn->{format_name};
			last;
		}
	}
    print "\n";
	if ($matched == 0)  {
		++ $count{ unknown };
	}
}

main();
