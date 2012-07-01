#!/usr/bin/perl

use strict;
use warnings;
use v5.10;
use Storable;

my $min = 1000;
my $max = 9999;
my %num = ();
my @fprime = ();
my @hards = ();

#
# try to list the numbers of which factors are not 2,3,5,7,11
#


# to init %num with numbers and state = 1
sub init()
{
    my $i;
    for ( $i=$min; $i<=$max; ++$i )  {
        $num{$i} = 1;
    }
}

# to mark 0 if $num % %out is 0
sub filter($)
{
    my $out = shift;

    for (my $i=$min; $i<=$max; ++$i)  {
        if ($num{$i} && ($i % $out) == 0)  {
            $num{$i} = 0;
        }
    }
}

# to sort hash key
sub Ascending($$)
{
	my ($a, $b) = @_;
	$a <=> $b;
}

# to list specified hash
sub show($)
{
	my $ref = shift;
	my $cnt = 0;
	my $cnt_1 = 0;
	my $cnt_2 = 0;
	foreach my $kk (sort Ascending keys %$ref)  {
	    if ($$ref{$kk})  {
		    ++$cnt;
		    say $kk, "\t", $$ref{$kk};
		    if ($$ref{$kk}==1)  {   # the primes + numbers not taken out
		        push(@hards,$kk);
		    }
		    ++$cnt_2 if ($$ref{$kk}==2); # true primes
		}
	}
	say "cnt: $cnt";
	say "cnt_1: $cnt_1";
	say "cnt_2: $cnt_2";
}

sub main()
{
    init();

    my $store_file = 'fourdigit.dat';
	if ( -e $store_file )  {
		print STDERR "load from stored data file\n";
		@fprime = @{ retrieve($store_file) };   # direct to hash
	}
	else {
	    die "no prime table exists!";
	}

    #show(\%num);
    filter(2);
    filter(3);
    filter(5);
    filter(7);
    filter(11);
    #show(\%num);

    foreach my $vv (@fprime) {
        if ( $num{$vv} == 0 )  {
            say "$vv is deleted";
        } elsif ( $num{$vv} == 1 )  {
            $num{$vv} = 2;
        } elsif ( $num{$vv} == 2 )  {
            say "duplicated?";
        }
    }
    show(\%num);
    output_hards();


}

sub output_hards()
{
    open my $ofh, "> hards.txt" or die;
    foreach my $nn (@hards)  {
        print $ofh $nn,"\n";
    }
    close $ofh;
}

main;
