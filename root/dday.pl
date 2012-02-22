#!/usr/bin/perl
#
# some date/time functions from activeState
#

use ActiveState::DateTime qw(is_leap_year
		days_in_month
		check_date month_name_short
		month_name_long
		gmt_offset);

# get date of today
my (undef,undef,undef,$day,$month,$year,undef,undef,undef) = localtime;
$year += 1900;
$month += 1;

printf "yyyy/mm/dd => %04d/%02d/%02d\n", $year, $month, $day;
if (is_leap_year($year)) {
	print "($year) is leap year\n";
}

my $max_days = days_in_month($year, $month);

if (check_date($year, $month, $day)) {
	print "check day ok\n";
}

my $short_month_name = month_name_short($month);

my $long_month_name = month_name_long($month);

my $offset = gmt_offset();

print "=> short_month_name, long_month_name, offset =>\n";
print "$short_month_name, $long_month_name, $offset\n";
