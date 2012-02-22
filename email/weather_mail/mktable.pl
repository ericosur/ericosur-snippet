#!/usr/bin/perl

use strict;
use warnings;

sub parse_date($)
{
	my $date = shift;

	print $date,"\n";
}

sub parse_temp($)
{
	my $temp = shift;

	print $temp,"\n";
}

sub parse_wet($)
{
	my $wet = shift;
	print $wet,"\n";
}


sub parse_press($)
{
	my $press = shift;
	print $press;
}

sub main()
{
	my $file = "small.txt";
	open my $fh, $file or die;

	my ($mm, $dd, $hh);
	my $dt = qr(\"([^\"]+)\");

	while (<$fh>)  {
		if ( m/($dt),($dt),($dt),($dt)/ )  {
			if (defined($1))  {
				parse_date($1);
			}
			if (defined($2))  {
				parse_temp($2);
			}
			if (defined($3))  {
				parse_wet($3);
			}
			if (defined($4))  {
				parse_press($4);
			}
		}
	}

	close $fh;
}

main;
