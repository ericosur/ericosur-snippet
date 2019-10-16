#!/usr/bin/perl
use strict;

sub help()
{
	print "$0 <filename to split>\n";
	exit(1);
}

my $file = $ARGV[0] or help();
my $ifh;
my $count = 0;
my $pat = 'Rar!';

print $file,"\n";
open $ifh, "< $file" or die;
binmode $ifh;
open my $ofh, "> out.bin" or die;
binmode $ofh;

local $/ = $pat;
my $cc = 0;
while (<$ifh>) {
	# do stuff with the "line" in $_
	# chomp will remove "the string to match";
	if ($cc != 0)  {
		print $ofh $pat;
		print $ofh $_;
	}
	$cc ++;
}

close $ifh;
close $ofh;

__END__

local $/ = "the string to match";

while (<fileHandle>) {
  #do stuff with the "line" in $_
  #chomp will remove "the string to match";
}

while (<$ifh>)  {
	$count ++;
	if (m/Rar!/)  {
		print "found at $count\n";
	}
}
