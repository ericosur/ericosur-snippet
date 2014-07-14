#!/usr/bin/env perl

# ref: http://search.cpan.org/~drolsky/DateTime-1.10/lib/DateTime.pm

use strict;
use DateTime;

sub show($$)
{
	my ($hh, $ff) = @_;
    printf("%s %s\n", $hh, $ff);
}

my $dt = DateTime->new(
	year => 2012,
	month => 2,
	day => 10,
	hour => 16,
	minute => 44,
	second => 0,
	time_zone => 'Asia/Taipei',
);

show("hms:", $dt->hms);

show("ce_year:", $dt->ce_year());
show("era_name:", $dt->era_name());
show("era_abbr:", $dt->era_abbr());
show("christian_era:", $dt->christian_era());
show("secular_era:", $dt->secular_era());
show("year_with_era:", $dt->year_with_era());
show("year_with_christian_era:", $dt->year_with_christian_era());

show("day_of_week:", $dt->day_of_week());
show("day_name:", $dt->day_name());
show("day_of_year:", $dt->day_of_year());
show("quarter:", $dt->quarter());
show("weekday_of_month:", $dt->weekday_of_month());
show("ymd sep=/:", $dt->ymd("/"));
show("week:", $dt->week());
show("week_year:", $dt->week_year());
show("week_of_month:", $dt->week_of_month());

show("jd:", $dt->jd());
show("mjd:", $dt->mjd());

show("time_zone:", $dt->time_zone());
show("time_zone_long_name:", $dt->time_zone_long_name());
show("time_zone_short_name:", $dt->time_zone_short_name());
show("epoch:", $dt->epoch());


