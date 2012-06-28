#!/usr/bin/perl

use strict;
use 5.010;
use utf8;
#use feature 'unicode_strings';

my $debug = 1;

sub read_iso3166()
{
	my $ff = 'two-alpha.txt';
	my %two_full = ();
    my %full_two = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if ( m/^(..)\s+(.+)$/ )  {
			my $two = $1;
			my $full = $2;
			if ( defined($two) && defined($full) ) {
			    $two_full{$two} = $full;
			    $full_two{$full} = $two;
			}
			if ($debug) {
			    print("($full) => ($two)\n");
			}
		}
	}
	close $fh;
	say STDERR "read_iso3166(): size of two_full: ", scalar(keys(%two_full));
	say STDERR "read_iso3166(): size of full_two: ", scalar(keys(%full_two));
}

sub read_iso31661alpha2()
{
	my $ff = 'iso-3166-1-alpha-2.txt';
	#my %two_full = ();
    my %full_two = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if ( m/^(.+);(..)$/ )  {
			my $full = $1;
			my $two = $2;
			if ( defined($two) && defined($full) ) {
			    #$two_full{$two} = $full;
			    $full_two{$full} = $two;
			}
			if ($debug) {
			    print("($full) => ($two)\n");
		    }
		}
	}
	close $fh;
	#say STDERR "size of two_full: ", scalar(keys(%two_full));
	say STDERR "read_iso31661alpha2(): size of full_two: ", scalar(keys(%full_two));

	return %full_two;
}

sub read_iso31661alpha3()
{
	my $ff = 'iso-3166-1-alpha-3.txt';
	#my %three_full = ();
    my %full_three = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if ( m/^(...)\s+(.+)$/ )  {
			my $three = $1;
			my $full = $2;
			if ( defined($three) && defined($full) ) {
			    #$three_full{$three} = $full;
			    # upper case name of nations
			    $full_three{uc($full)} = $three;
			}
			if ($debug) {
			    print("($full) => ($three)\n");
		    }
		}
	}
	close $fh;
	#say STDERR "read_iso31661alpha3(): size of three_full: ", scalar(keys(%three_full));
	say STDERR "read_iso31661alpha3(): size of full_two: ", scalar(keys(%full_three));

	return %full_three;
}

sub main()
{
    my %two = ();
    my %three = ();
    #read_iso3166();
    %two = read_iso31661alpha2();
    %three = read_iso31661alpha3();

    say "==========> using alpha2 countries";
    my @notfound3 = ();
    foreach my $fn (keys(%two)) {
        if ( not defined($three{$fn}) ) {
            push(@notfound3, $fn);
        }
        #say $fn, "\t", $two{$fn}, "\t", $three{$fn};
    }

    say "notfound3: ", scalar(@notfound3);
    foreach my $fn (@notfound3) {
        say "notfound3: ", $fn;
    }

    say "==========> using alpha3 countries";
    my @notfound2 = ();
    foreach my $fn (keys(%three)) {
        if ( not defined($two{$fn}) ) {
            push(@notfound2, $fn);
        }
        #say $fn, "\t", $two{$fn}, "\t", $three{$fn};
    }
    say "notfound2: ", scalar(@notfound2);
    foreach my $fn (@notfound2) {
        say "notfound2: ", $fn;
    }
}

main;
