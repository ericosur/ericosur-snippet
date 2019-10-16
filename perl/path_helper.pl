#!/usr/bin/perl
#!/bin/perl

#
# path_helper.pl <filename.txt>
#
# file contains a list for path for merging together
# output to the console and copy it to the clipboard
#
# (you may use sp.pl to split the current ''path'' variable
# and output it to a file. After editing it, use this script
# to merge them together.)
#

use strict;
use warnings;

use Win32::Clipboard;

my $file;
my $path_line;
my $fh;

$file = $ARGV[0] || "p.txt";

open $fh, $file or die "cannot open $file: $!\n";

while (<$fh>)  {
	next if m/^[#;:]/;	# as comment line
	s/\r//;
	s/\n//;
	s/\\$//;
	my $dir = $_;

	if ( -d $_ )  {
		if ($path_line)  {
			$path_line = $path_line . ";" . $_;
		}
		else  {
			$path_line = $_ ;
		}
	}
	else  {
		print "Such path is not exist: " . $_ . "\n";
	}
}
close $fh;

Win32::Clipboard::Set($path_line);	# set it to the clipboard
printf ">>>%s<<<\n", $path_line;


__END__;

my @foo = split /;/, $path_line;
for (@foo)
{
	print;
	print "\n";
}

# use ''reg'' to query the registry for all environment variables
# reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
