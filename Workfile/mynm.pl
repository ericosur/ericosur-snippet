#!/usr/bin/perl
#
# call 'nm' to list symbol in lib file,
# delete the unnecessary symbols
#

use strict;
use warnings;
use 5.010;

my $count = 0;

sub process($)
{
	my $fn = shift;
	say $fn;
	$count ++;
	my $cmd = 'nm ' . $fn;
	my $op = `$cmd`;
	foreach ( split /\n/, $op )  {
		next if m/\st\s/;
		next if m/\$debug_frame/;
		say $_;
	}
}


sub get_filename_from_list($)
{
	my $list_file = shift;

	open my $fh, $list_file or die;
	while (<$fh>)
	{
		tr/\r\n//;
		#print $_;
		process($_);
	}
	close $fh;
}


sub main()
{
	#
	# most completely glob / argv here
	#
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

		printf STDERR "%d files checked\n", $count;
	}
	else  {
		printf STDERR "\n%s <filename> [\@list file] [filenames...] \n", $0;
	}
}

main; 
