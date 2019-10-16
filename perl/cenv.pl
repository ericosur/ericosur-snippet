#!/usr/bin/perl
#!/bin/perl

#
# demo for using Env module to get environment variables
#
# Usually we use $ENV{"PATH"} to get the 'path' variable
# Here demos the other way to do so.
#
# refer to sp.pl
#
# 2006/12/27 by ericosur

use strict;
use warnings;

#use Data::Dump qw(dump);

use Env qw($PROMPT @PATH $PATH @PATHEXT);

# the @PATH is the splitted version of $PATH

print "@ prompt = ${PROMPT}\n" if $PROMPT;

my $len = @PATH;
printf "@ %d entries in the PATH:\n", $len;

#print "original path: $PATH";
#print "\n";
foreach (@PATH)
{
    if (-d $_)  {
        print $_ . "\n";
    }
    else  {
        print "path not exist???  $_\n";
    }
}

if (@PATHEXT)  {
    print '-' x 25, '@ pathext @', '-' x 25, "\n";
    for (@PATHEXT)  {
        print "$_\n" if $_;
    }
}


=pod

=head1 NAME

cenv.pl

=head1 DESCRIPTION

This script demostrates how to "use Env" to fetch environment variables
without parsing it. For example, the PATH would be stored into @PATH for
instantly using.

=head1 SYNTAX

Just run and see the result.

=cut
