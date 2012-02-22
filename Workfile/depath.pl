#!/usr/bin/perl
#
# remove the ';c:\cygwin\bin' from environment
# and save the result into win32 clipboard
#
# 2007/11/15 by ericosur
#

use strict;
use warnings;

use Win32::Clipboard;

my $path = $ENV{"PATH"};
my $target = $ARGV[0] || qr(c:\\cygwin\\bin);

print "$target\n";

$path =~ s/;$target//i;
$path = "path=" . $path;

print "$path\n";
Win32::Clipboard::Set($path);	# set it to the clipboard

# not working after the script terminated
$ENV{"PATH"} = $path;

=pod

=head1 NAME

depath.pl - remove specified dir from path, default "c:\cygwin\bin"

=head1 SYNOPSIS

depath.pl

and then you need to paste the result to command line and execute it

=head1 DESCRIPTION

It removes the CYGWIN path from the current PATH environment variable
and stores the result into windows clipboard.

=head1 NOTE

You should press mouse right button the paste the result and execute it
under command line to change the PATH variable.

=cut
