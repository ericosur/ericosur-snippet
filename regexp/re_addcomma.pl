#!/usr/bin/perl
use strict;

#
# demo how to use regular exporess to add '','' into numbers in lines
#

my $pat = qr[(?<=\d)(?=(?:\d\d\d)+(?!\d))];

### my $data =<<EOL;

# use the trick to parse into lines in place
my @str = ( << "EOL" =~ /^\s*(.+)/gm );
there is 1 car
there is 123 cats
there is 12345 dogs
there is 1234567 frog
there is 12345678 zebra
EOL

### my @str = split /\n/, $data;
foreach (@str)
{
	my $bk = $_;

	if ( s!$pat!,!g )
	{
		print "$bk  --> $_\n";
#		print $1,"\n";		# the $1 is null
	}
	else
	{
		print $_, "\n";
	}
}
