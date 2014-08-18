#!/usr/bin/perl
#@
#@ wildcard.pl
#@ demo how to use file globbing...
#@ a more flexible way to use wildcard file names
#@
#@ you may use
#@ wildcard.pl 1.cpp 2.cpp a*.cpp cs*.cpp ...
#@
#@ Oct 21 2004 by ericosur

#
# Feb 19 2008
# for a more structured wildcard subroutine, refer to "smaller.pl"
#

use strict;
use warnings;

my $count = 0;

sub main();
sub process($);
sub get_filename_from_list($);

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

		printf "%d files checked\n", $count;
	}
	else  {
		printf "\n%s <filename> [\@list file] [filenames...] \n", $0;
	}
}
#
# most completely glob / argv here
#


# just take one argument and print it out
sub process($)
{
	my $arg = shift;
	print "$arg\n";
	++ $count;
}


sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;
	while (<FH>)
	{
		tr/\r\n//;
		#print $_;
		process($_);
	}
	close FH;
}


main();

=pod

=head1 NAME

	wildcard.pl

=head1 DESCRIPTION

	A useful procedure to deal with wildcard arguments.

=head1 USAGE

	Wildcard.pl a*.txt b??k.txt script.pl @filelist.txt

	The filelist.txt would be taken as a file list.
	You may use ''dir /b > filelist.txt'' to produce a file list.

=cut
