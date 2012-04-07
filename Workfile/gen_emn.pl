#!/usr/bin/perl
# generate a EMN content by using the current time stamp
#
# refer to the tool from libwbxml: xml2wbxml
# for further translation from xml to wbxml
#

use strict;
use warnings;

use Win32::Clipboard;

# the mailbox
my $mailbox = q(rasmus.lai@indigoqm.tw);

# compose the time stamp
#my $timestamp = "2008-03-27T15:30:00Z";
my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
my $timestamp = sprintf "%04d-%02d-%02dT%02d:%02d:%02dZ",
	($year+1900), ($mon+1), $mday,
	$hour, $min, $sec;

#print STDERR $timestamp, "\n";

# the EMN content here
my $emn =<<EOL;
<?xml version="1.0"?>
<!DOCTYPE emn PUBLIC "-//OMA/DTD EMN 1.0//EN"
"http://www.openmobilealliance.com/tech/DTD/emn.dtd">
<emn mailbox="mailat:$mailbox"
timestamp=\"$timestamp\"
/>
EOL

# copy the generated content to clipboard
Win32::Clipboard->Set($emn);

print $emn;

=pod

=head1 NOTE

gen_emn.pl

This script would generate a specific XML for EMN.
The date/time field would change according to the current time.

=cut
