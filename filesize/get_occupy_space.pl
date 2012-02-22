#!/usr/bin/perl
#
# at cmd, `dir /s/q`
# search for specific user name like ''administrator''
# count the number of files and the total size of
# those files (refer to 'tdir.pl')
#
# Jun 9 2005 by ericosur

use strict;
use warnings;

sub parse_line($);

my $total_bytes = 0;
my $name = $ARGV[0] || 'Administrator';
my $count = 0;
my $in_file = '_dir_list.txt';
my $file_pattern = $ARGV[1] || '*pl';

printf "..... search files belong to %s\n", $name;

if (-e $in_file )
{
	print "..... open $in_file for reading\n";
	open FH, "< $in_file" or die "opening $!\n";

	while (<FH>)
	{
		my ($gotname, $size) = parse_line($_);
		$count ++ if $gotname;
		$total_bytes += $size;
	}

	close FH;
}
else
{
	print "..... Take current working directory for processing [$file_pattern]\n";
	my $res = `cmd /c dir /q $file_pattern`;
	my @lines = split /\n/, $res;

	foreach (@lines)
	{
		my ($gotname, $size) = parse_line($_);
		$count ++ if $gotname;
		$total_bytes += $size;
	}
}

print "Total $count files belong to $name\n";
printf "total count = %d Bytes", $total_bytes;


sub parse_line($)
{
	my $line = shift;
	my $fsize = 0;
	my $got = 0;
	my $fname;

	return (0, 0) if ( $line =~ m/(^\s+|^$)/ );
	if ( $line =~ m/^[\d\/]+\s+\d\d\:\d\d\s+([\d,]+)\s+(.*?)\s+(.*)/ )
	{
		$fsize = $1;
		$fname = $3;
		$got = 1 if ( $2 =~ m/$name/i );
		$fsize =~ s/,//g;
	}

#	print "($got, $fsize, $fname)\n";
	return ($got, $fsize);
}

#
# in CMD, 'dir /q' looks like:
# 2005/06/09  10:57                  200 BUILTIN\Administrators sortlist.pl
# 2005/06/09  10:53                  221 BUILTIN\Administrators sp.pl
#
