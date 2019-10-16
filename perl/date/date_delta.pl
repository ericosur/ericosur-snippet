use strict;
use v5.10;

use Date::Calc qw(Delta_Days);

#
# get the current date/time to compose filename
#
sub get_date
{
        my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
        my $date = sprintf "%04d-%02d-%02d", $year+1900, $mon + 1, $mday;
        return ($year+1900, $mon+1, $mday);
}

sub main()
{
	my ($yy, $mm, $dd) = get_date();
	my ($syy,$smm,$sdd) = (2012,2,10);
#	printf("%s-%s-%s\n", $yy,$mm,$dd);
	my $days = Delta_Days(2012,2,10,$yy,$mm,$dd);
	printf("date delta = %d since %d-%d-%d\n", $days, $syy, $smm, $sdd);
}

main;

