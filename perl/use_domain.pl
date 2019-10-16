#!/usr/bin/perl
#
# Net::Domain
#
# 2007/01/10 by ericosur

use Net::Domain qw(hostdomain hostfqdn hostname);

printf "hostdomain(%s)\nhostfqdn(%s)\nhostname(%s)\n",
		hostdomain(),
		hostfqdn(),
		hostname();
