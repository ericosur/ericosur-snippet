#!/usr/bin/perl
#
# use package Date::Calc
#
# 2007/01/17 by ericosur

use strict;
use warnings;

use Date::Calc qw(:all);

sub show_msg($$)
{
	my $msg = shift;
	my $var = shift;

	print $msg, ": ", $var, "\n";
}

sub main
{
	#  Today
	my ($year,$month,$day) = Today();
	printf "%d/%d/%d\n", $year, $month, $day;

	$_ = Days_in_Year($year, $month);
	show_msg("Days_in_Year", $_);

	$_ = Days_in_Month($year, $month);
	show_msg("Days_in_Month", $_);

	$_ = Weeks_in_Year($year);
	show_msg("Weeks_in_Year", $_);

	show_msg("leap year", $year) if (leap_year($year));

	$_ = Day_of_Year($year,$month,$day);
	show_msg("Day_of_Year", $_);

	$_ = Date_to_Days($year,$month,$day);
	show_msg("Date_to_Days", $_);

	$_ = Day_of_Week($year,$month,$day);
	show_msg("Day_of_Week", $_);

	($year,$month,$day) = Today();
	my $week;
	($week,$year) = Week_of_Year($year,$month,$day);
	show_msg("Week_of_year", $week);

}

main;

=pod

=head1 NAME

	datecalc.pl

=head1 DESCRIPTION

	use use Date::Calc;

=cut
