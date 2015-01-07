#!/usr/bin/perl

use strict;
use warnings;

my @total = ();

# from 0000 to 9999
sub list_all
{
	my $str;
	for (0..9999)  {
		$str = sprintf "%04d", $_;
		if (is_duplicate($str))  {	# no duplicated number
			next;
		}
#		if (is_lead_zero($str))  {	# no start with 0
#			next;
#		}
		#print $str,"\n";
		push @total, $str;
	}
}

sub is_duplicate($)
{
	my $value = shift;

	if (length($value) ne 4)  {
		#die "length is not 4";
        return 1;
	}

	my %dup = ();
	for (split //, $value)  {
		$dup{$_} ++;
		#print "$_\t";
	}
	#print "\n";
	for (keys %dup)  {
		#print $_, ":", $dup{$_}, "\n";
		if ($dup{$_} > 1)  {
			return 1;
		}
	}
	return 0;
}

sub is_lead_zero
{
	my $value = shift;

	if ( $value =~ m/^0\d{3}/ )  {
		return 1;
	} else  {
		return 0;
	}
}

# [in] answer
# [in] guess
# [out] (aa, bb)
sub get_ab
{
	my ($ans, $guess) = @_;
	my ($a, $b) = (0, 0);

	for my $i (0..3)  {
		for my $j (0..3)  {
			my $mm = substr($guess, $i, 1);
			my $nn = substr($ans, $j, 1);
			if ($mm eq $nn)  {
				if ($i eq $j)  {
					$a ++;
				}
				else  {
					$b ++;
				}
			}
		}
	}
	my $result = sprintf "%dA%dB", $a, $b;
	return $result;
}

sub main()
{
	my %all_guess = ();
    my %bguess = ();
	my $ans;

    do {
        $ans = int(rand(10000));
    } until ( !is_duplicate($ans) );
	list_all();
	for (@total)  {
		my $res = get_ab($ans, $_);
		$all_guess{$res} ++;
        #$bguess{$res} = ('a');
        #push($bguess{$res}, $res);
	}

	# print out the result
	my $cnt = 0;
	my %foo = ();
	for (keys %all_guess)  {
		#printf "%s: %d\n", $_, $all_guess{$_};
		$cnt += $all_guess{$_};
		$foo{ $all_guess{$_} } = $_;
	}
    if ($#total+1 != $cnt) {
        print "cnt = $cnt\n";
    }
    printf("for answer: %s\n", $ans);
	print "total = ", $#total+1,"\n";

	for (sort {$a <=> $b} keys %foo)  {
		printf "%s: %s (%.2g%%)\n", $foo{$_}, $_, ($_*100/$cnt);
	}
}

main;
