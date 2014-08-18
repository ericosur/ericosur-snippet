#!/usr/bin/env perl

use strict;
use v5.10;

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


sub parse_file()
{
	my $ifile = 'all-cmb.txt';
	my $ofile = 'all-desk.txt';
	open my $ifh, $ifile or die 'cannot open $ifile';
	open my $ofh, ">", $ofile or die 'cannot open $ofile';

	# parse line
	while (<$ifh>)  {
		my @cd = ();
		my $cf = "";
		s/[\r\n]//;
		while ( m/(\d+)/g )  {
			$cf .= $cardface{$1}," ";
			push @cd, $1;
		}
		my $rt = check_hand(@cd);
		print $ofh "$cf\t$rt\n";
	}

	close $ifh;
	close $ofh;
}


# input (1,2,3,4,5)
sub check_hand(@)
{
	my %pp = ();
	my %ss = ();
	my $is_joker = 0;
	my $is_same_suit = 0;
	my $dbg = 0;
	my $rt;

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
			$rt = "(1) 5 cards!";
		}
		else  {
			$rt = "(3) 4 cards!";
		}
		goto exitfunc;
	}

	# 判別 straight 以及 royal straight flush
	if ($is_joker && ($pp{A} == 1 && $pp{K} == 1
						&& $pp{Q} == 1 && $pp{J} == 1))  {
		if ($is_same_suit)  {
			$rt = "(2) royal straight flush!";
		}
		else  {
			$rt = "(5) straight!";
		}
		goto exitfunc;
	}

	# 判別 3 cards
	if ($pp{A} == 3 || $pp{K} == 3 || $pp{Q} == 3 || $pp{J} == 3)  {
		if ($pp{A} == 2 || $pp{K} == 2 || $pp{Q} == 2 || $pp{J} == 2)  {
			$rt = "(4) full house";
		}
		else  {
			$rt = "(6) 3 cards";
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

=pod
		$rt = "(7) 2 pairs";
=cut

#=pod
		# 不確定是否鬼牌可以充作一張，升級為 full house
		if ($is_joker)  {
			$rt = "(4) full house";
		}
		else {
			$rt = "(7) 2 pairs";
		}
#=cut

		goto exitfunc;
	}

	# 判別 1 pair
	if ( $pp{A}==1 || $pp{K}==1 || $pp{Q}==1 || $pp{J}==1 )  {

=pod
		$rt = "(8) 1 pair";
=cut
#=pod
		# 不確定鬼牌可升級 1pair 到 3cards
		if ($is_joker)  {
			$rt = "(6) 3 cards";
		}
		else {
			$rt = "(8) 1 pair";
		}
#=cut
		goto exitfunc;
	}

exitfunc:
	#show_pt(\%pp);
	say $rt;
	say "check_hand() <======";
	return $rt;
}

sub main()
{
	parse_file();
}

main;

