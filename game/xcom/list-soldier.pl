#!/usr/bin/perl

use strict;
use v5.10;

my @attr_name = qw(TimeUnit Health Stamina Reaction Strength FiringAcc
		ThrowingAcc MeleeAcc PsiStrength PsiSkill Rank);

sub show_attr($)
{
	my $attr = shift;

	#say "size of \@attr_name:", scalar(@attr_name);

	my @vals = split(//, $attr);
	for (my $i = 0; $i < scalar(@attr_name); ++$i) {
		printf("%d,", ord($vals[$i]));
	}
	print "\n";
}

sub parse_soldier()
{
	my $file = "soldier.dat";
	my $start_offset = 0;
	my $mission_offset = 8;
	my $kill_offset = 10;
	my $rank_offset = 14;
	my $name_offset = 16;
	my $attr_offset = 42;
	my $name_len = 25;

	my $block_size = 68;
	my $fsize = -s $file;
	my $content;

	#say "fsize: ", $fsize;

	open my $fh, $file or die;
	binmode $fh;
	read($fh, $content, $fsize);
	close $fh;
	#say "len of content: ", length($content);

	#my $num_of_soldier = ord(substr($content, 0x0e, 1));
	#say "num: ", $num_of_soldier;
	for (my $i=0; ; ++$i) {
		my $addr = $start_offset + $block_size * $i;
		my $piece = substr($content, $addr, $block_size);
		#say "len of peice: ", length($piece);
		my $soldier_name = substr($piece, $name_offset, $name_len);
		if ( ord(substr($soldier_name, 0, 1)) != 0 ) {
			$soldier_name =~ s/\x00//g;
			printf("\"%s\",", $soldier_name);

			my $mission = ord(substr($piece, $mission_offset, 1));
			my $rank = ord(substr($piece, $rank_offset, 1));
			my $kills = ord(substr($piece, $kill_offset, 1));
			show_rank($mission, $rank, $kills);

			show_attr( substr($piece, $attr_offset, scalar(@attr_name)) );
		} else {
			last;
		}
	}
}

sub show_rank($$$)
{
	my ($mission, $rank, $kills) = @_;
	my $real_rank = $rank - 20 - $mission;
	my $rank_name;

	printf("%d,", $mission);
	#printf("%d,", $real_rank);

	if ($real_rank >= 10) {
		$rank_name = "CDR";
	} elsif ($real_rank >= 6) {
		$rank_name = "COL";
	} elsif ($real_rank >= 3) {
		$rank_name = "CPT";
	} elsif ($real_rank >= 1) {
		$rank_name = "SGT";
	} elsif ($kills > 0) {
		$rank_name = "Squ";
	} elsif ($real_rank >= 0) {
		$rank_name = "Rec";
	}

	printf("\"%s\",", $rank_name);
	printf("%d,", $kills);
}

sub print_header()
{
	print "name,mission,rank,kills,";
	foreach my $pp (@attr_name) {
		print $pp,",";
	}
	print "\n";
}

sub main()
{
	print_header();
	parse_soldier();
}

main;

