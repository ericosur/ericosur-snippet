#!/usr/bin/perl

# to calc distance from x/z coordinates
# to find minimum distance from poi to base
use strict;
use warnings;
use v5.10;
use Data::Dump qw(dump);

sub load_pos($)
{
	my $file = shift;
	my @poss = ();

	open my $fh, $file or die;
	my $cnt = 0;
	my @pt = (0, 0);
	while (<$fh>) {
		my @pair = ();
		next if m/^#/;
		if ( m/^(-?\d+),(-?\d+)/ ) {
			@pair = ($1, $2);
			#say "($1,$2)";
			#my $d = get_dist(\@pair, \@pt);
			#push(@pair,$d);
			$poss[$cnt] = \@pair;
			$cnt ++;		
		}
	}
	close $fh;
	#say "items: ", scalar(@poss);
	return @poss;
}

# in: ref of (x,y) pair
sub show_pair($)
{
	my $pp = shift;
	my $str = "";
	my $pr = sprintf("(%d,%d)", $pp->[0], $pp->[1]);

	if (defined($pp->[2])) {
		$str = sprintf("%.3f", $pp->[2]);
		$str = $str . "\t" . $pr;
	} else {
		$str = $pr;
	}


	return $str;
}

sub show_pos($)
{
	my $rr = shift;
	my @allpos = @$rr;
	#my @pp;
	foreach my $ii (@allpos) {
		say show_pair($ii);
		#say get_dist($ii);
	}
}

# to calculate the distance to (px,py)
# in1: point #1
# in2: point #2
sub get_dist($$)
{
	my $rr = shift;
	my $pr = shift;
	my ($x,$y) = ($rr->[0],$rr->[1]);
	my ($px,$py) = ($pr->[0],$pr->[1]);
	my $dist = sqrt(($x-$px)**2 + ($y-$py)**2);
	return $dist;
}

sub set_homepos()
{
	my @names = qw(h1 h2 h3 v1 v2 v3 v4 v5);
	my $p = "((-87,-132), (587,1024), (1264,2935),
		(197,-392), (587,1024), (1088,2060), 
		(1264,2935), (2831,3772))";
	my @homes = ();
	my %hhome = ();

	while ( $p =~ m/\((-?\d+),(-?\d+)\)/g ) {
		#say "$1, $2";
		my @ps = ($1, $2);
		push(@homes, \@ps);
	}
	
	#dump(@homes);
	for (my $i=0; $i<scalar(@names); ++$i) {
		$hhome{$names[$i]} = $homes[$i];
	}
	#dump(%hhome);
	return %hhome;
}

sub each_dist($)
{
	my $rr = shift;
	my %hh = %$rr;
	my @kys = sort(keys(%hh));
	#dump(@kys);
	my $cnt = 0;

	for (my $ii=0; $ii<scalar(@kys)-1; ++$ii) {
		for (my $jj=$ii+1; $jj<scalar(@kys); ++$jj) {
			printf("%s vs %s\t", $kys[$ii], $kys[$jj]);	
			say get_dist($hh{$kys[$ii]}, $hh{$kys[$jj]});
			$cnt++;
		}
	}
	say "cnt: $cnt";
}

sub get_min_from_base_to_poi($$)
{
	my ($rbs, $rpoi) = @_;
	my %bs = %$rbs;
	my ($min, $minkk) = (9999, "null");

	foreach my $kk ( sort(keys(%bs)) ) {
		my $dist = get_dist($bs{$kk},$rpoi);
		if ($dist < $min) {
			$min = $dist;
			$minkk = $kk;
		}
		#say $bs{$kk};
		#say $pi[0];
		#say "to $kk: ", $dist;
	}
	#say "poi: ", show_pair($rpoi);
	#say "minkk: $minkk";
	#say "min: $min";
	printf("\"%s\",\"%s\",\"%s\"\n", show_pair($rpoi), $minkk, $min);
}

sub main()
{
	my $file = "pos.txt";
	#say "home pos: ($px, $py)";

	my @poi = load_pos($file);
	#show_pos(\@poi);

	my %bases = ();
	%bases = set_homepos();
	#each_dist(\%bases);

	say "poi,minkk,min";
	foreach my $pp (@poi) {	
		get_min_from_base_to_poi(\%bases, $pp);
	}
}

main;

