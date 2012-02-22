use strict;
use 5.010;

use Date::Calc qw(Delta_Days);

my $days = Delta_Days(2011,1,1,2011,6,17);

say $days;
