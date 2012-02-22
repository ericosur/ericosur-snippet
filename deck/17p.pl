#!/usr/bin/env perl

use strict;
use 5.010;

my $debug = 0;

my %cardface = (
	0, "jj",
	1, "SA",
	2, "SK",
	3, "SQ",
	4, "SJ",
	5, "HA",
	6, "HK",
	7, "HQ",
	8, "HJ",
	9, "CA",
	10, "CK",
	11, "CQ",
	12, "CJ",
	13, "DA",
	14, "DK",
	15, "DQ",
	16, "DJ"
);


sub fill_array()
{
    my @arr = ();

    for (0..16)  {
        push @arr, $_;
    }
    return @arr;
}


sub shuffle(\@)
{
    my $aref = shift;
    my @arr = @$aref;

    if ($debug)  {
        print "before...\n";
        show_array(@arr);
    }

    my $n = scalar @arr;
    print "n = $n\n" if $debug;
    while ($n > 1)  {
        my $k = int(rand($n));
        $n --;
        if ($debug)  {
            printf "arr[%d], arr[%d] (%d,%d)\t", $n, $k, $arr[$n], $arr[$k];
        }
        ($arr[$n], $arr[$k]) = ($arr[$k], $arr[$n]);
    }

    if ($debug)  {
        print "\nafter...\n";
        show_array(@arr);
    }
}


sub shuffle_ref(\@)
{
    my $aref = shift;

    if ($debug)  {
        print "before...\n";
        show_array(@$aref);
    }
    my $n = scalar @$aref;

    print "n = $n\n" if $debug;

    my $cnt = 0;
    while ($n > 1)  {
        my $k = int(rand($n));
        $n --;
        if ($debug)  {
            printf "arr[%d], arr[%d] (%d,%d)\t", $n, $k, $$aref[$n], $$aref[$k];
        }
        ($$aref[$n], $$aref[$k]) = ($$aref[$k], $$aref[$n]);
#        printf "%d(%d,%d) => ", ++$cnt, $n, $k;

#        draw_array($aref, $n, $k);   #show_array(@$aref);
    }
    if ($debug)  {
        print "\nafter...\n";
        show_array(@$aref);
    }
}


sub show_array_as_num(@)
{
    foreach (@_)  {
        printf "%02d  ", $_;
    }
    print "\n";
}


sub show_array_as_card(@)
{
	foreach (@_)  {
		print $cardface{$_}, "  ";
	}
}

# arg1: ref of pt

# arg2: is_joker?
sub is_straight($$)
{
	my $aref = shift;
	my $is_joker = shift;
	my %h = %$aref;
	if ($h{A} == 1 && $h{K} == 1 && $h{Q} == 1 && $h{J} == 1)  {
		if ($is_joker)  {
			say "(5) straight!";
		}
		else  {

		}
	}
}

sub show_pt($)  {
	my $aref = shift;
	my %here = %$aref;
	for my $k (keys %here)  {
		say "$k: $here{$k}";
	}
}

# input (1,2,3,4,5)
sub check_hand(@)
{
	my %pp = ();
	my %ss = ();
	my $is_joker = 0;
	my $is_same_suit = 0;
	my $dbg = 1;

	say "check_hand() =>";
	foreach (@_)  {
		# 點數
		my $pt = substr($cardface{$_}, 1, 1);
		if ($pt eq 'j')  {	# 有鬼牌
			$is_joker = 1;
			say "joker!" if $dbg;
		}
		else  {
			#print "<$pt> ";
			$pp{$pt} ++;
		}
		# 花色
		my $st = substr($cardface{$_}, 0, 1);
		if ($st ne 'j')  {	# 跳過鬼牌
			$ss{$st} ++;
		}
	}

	if ($ss{H} == 4 || $ss{D} == 4 || $ss{S} == 4 || $ss{C} == 4)  {
		$is_same_suit = 1;
		say "all same suit!";
	}

	if ( $pp{A} == 4 || $pp{K} == 4 || $pp{Q} == 4 || $pp{J} == 4)  {
		if ($is_joker)  {
			say "(1) 5 cards!";
		}
		else  {
			say "(3) 4 cards!";
		}
		goto exitfunc;
	}

	# 判別 straight 以及 royal straight flush
	if ($is_joker && ($pp{A} == 1 && $pp{K} == 1
						&& $pp{Q} == 1 && $pp{J} == 1))  {
		if ($is_same_suit)  {
			say "(2) royal straight flush!";
		}
		else  {
			say "(5) straight!";
		}
		goto exitfunc;
	}

	# 判別 3 cards
	if ($pp{A} == 3 || $pp{K} == 3 || $pp{Q} == 3 || $pp{J} == 3)  {
		if ($pp{A} == 2 || $pp{K} == 2 || $pp{Q} == 2 || $pp{J} == 2)  {
			say "(4) full house";
		}
		else  {
			say "(6) 3 cards";
		}
		goto exitfunc;
	}

	# 判別 2 pairs
	if (   ($pp{A}==2 && $pp{K}==2)
		|| ($pp{A}==2 && $pp{Q}==2)
		|| ($pp{A}==2 && $pp{J}==2)
		|| ($pp{K}==2 && $pp{Q}==2)
		|| ($pp{K}==2 && $pp{J}==2)
		|| ($pp{Q}==2 && $pp{J}==2))  {
		if ($is_joker)  {
			say "(4) full house";
		}
		else {
			say "(7) 2 pairs";
		}
		goto exitfunc;
	}

	# 判別 1 pair
	if ( $pp{A}==1 || $pp{K}==1 || $pp{Q}==1 || $pp{J}==1 )  {
		if ($is_joker)  {
			say "(6) 3 cards";
		}
		else {
			say "(8) 1 pair";
		}
		goto exitfunc;
	}

exitfunc:
	show_pt(\%pp);
	say "check_hand() <======";
}


sub main()
{
	my @ar = fill_array();
	#show_array_as_num(@ar);
	#show_array_as_card(@ar);

	shuffle_ref(@ar);
	show_array_as_card(@ar);

	my @p1 = ();
	my @p2 = ();
	for (1 .. 5)  {
		push(@p1, pop(@ar));
		push(@p2, pop(@ar));
	}
	say '=' x 70;
	show_array_as_card(@p1);
	say;
	check_hand(@p1);
	say;
	#say '-' x 40;
	show_array_as_card(@p2);
	check_hand(@p2);

}

main;
