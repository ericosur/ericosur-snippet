#!/usr/bin/env perl
#
# Copyright (c) 2001 Rajesh Vaidheeswarran. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the same terms as Perl itself.
#
# $Id: whitespace,v 1.1 2001/05/15 21:36:36 rv Exp $

use Getopt::Std;
use Whitespace;
use strict;

my $majorversion = 1;
my $minorversion = 0;
my %opts;
my $prog = $0;
$prog =~ s/.*\///;
$prog =~ s/\.pl$//;

getopts("cv", \%opts);
my $cleanup = $opts{'c'} ? 1 : undef;
my $ver = $opts{'v'} ? 1 : undef;

if ($ver) {
    printf "$prog v%d.%d\n", $majorversion, $minorversion;
    print "Copyright 2000-2001 Rajesh Vaidheeswarran\n";
    print "All rights reserved.\n\n";
    print "This program is free software; you can redistribute it " .
	  "and/or modify\n";
    print "it under the same terms as Perl itself.\n\n";
    exit 0;
}

my $ret = 0;
my %errors = (
	      'leading' => 'Leading whitespace',
	      'trailing' => 'Trailing whitespace',
	      'indent' => 'Indentation whitespace',
	      'spacetab' => 'Space followed by Tab',
	      'eol' => 'End-of-line whitespace'
	      );

unless (@ARGV) {
    warn "Usage: $prog [[-v] | [-c] filename ...]\n";
    warn "       -c - cleanup\n";
    warn "       -v - show version and exit\n";
    exit 1;
}

my %data = ();

my $file;
foreach $file (grep { ! -d } @ARGV) {
    $data{$file} = {'handle' => new Whitespace($file)};
    my $h = $data{$file}->{'handle'};
    $data{$file}->{'stat'} = $h->detect();
}

foreach $file (sort keys %data) {
    my $ws = $data{$file}->{'handle'};
    my $stat = $data{$file}->{'stat'};
    if (!defined $stat) {
	print STDERR $ws->error() . "\n";
    } else {
	$ret += $stat;
	my $status = $ws->status();
	if (defined $status) {
	    foreach (sort keys %$status) {
		print STDERR "$file: " . $errors{$_} . "\n" if $status->{$_};
	    }
	}
	if (defined $cleanup) {
	    $stat = $ws->cleanup();
	    if (defined $stat) {
		print STDERR "$file: failed to cleanup ($stat).\n"
		    if $stat != 0;
		print STDOUT "$file clean.\n" if $stat == 0;
	    } else {
		print STDERR "[" . $ws->error() . ", cleanup failed.]\n";
	    }
	}
    }
}
exit $ret;

__END__;

=head1 NAME

whitespace - To clean up bogus whitespaces in program sources and other text.

=head1 SYNOPSIS

B<whitespace> [B<-c>] files...

=head1 DESCRIPTION

B<whitespace> uses the B<Whitespace> perl module to detect and
potentially cleanup bogus whitespaces (defined by the module).

=head1 OPTIONS

=over 10

=item B<-c>

Cleanup the given files, if any bogus whitespaces are present.

=head1 PREREQUISITES

This script requires the B<Whitespace> perl module.

=head1 SCRIPT CATEGORIES

String Processing / Language Text Processing / Parsing and Searching

=head1 AUTHOR

Rajesh Vaidheeswarran E<lt>rv@gnu.orgE<gt>

=head1 LICENSE

Copyright (C) 2000-2001 Rajesh Vaidheeswarran

All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the same terms as Perl itself.

=cut
