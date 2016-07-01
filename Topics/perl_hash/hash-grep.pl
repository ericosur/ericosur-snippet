#!/usr/bin/perl

# demo to create hash from birth.txt
# and use grep() to query data

use strict;
use v5.10;

sub main()
{
    my $file = 'birth.txt';
    open my $fh, $file or die "cannot open $!\n";

    my %hash = ();
    while ( <$fh> ) {
    	next if /^#/;
    	if ( /(\w+)\s*=>\s*(\S+)/ )  {
    		if (exists $hash{$1})  {
    			say "$1 already exists, skipped";
    		}
    		else  {
    			$hash{$1} = $2;
    		}
    	}
    }
    close $fh;

    while ( my ($k, $v) = each(%hash) )  {
    	say "$k => $v";
    }

    say "\nPrint out matched items";
    my @match = grep {$_ gt '1980'}  values(%hash);
    for (@match)  {
    	say $_;
    }
}

main;
