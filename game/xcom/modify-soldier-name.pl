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
	my $ofile = "sold-hack.dat";
	my $start_offset = 0;
	my $mission_offset = 8;
	my $kill_offset = 10;
	my $rank_offset = 14;
	my $name_offset = 16;
	my $attr_offset = 42;
	my $name_len = 25;
	my $MAX_SOLDIER = 250;  # $block_size * $MAX_SOLDIER = $fsize

	my $BLOCK_SIZE = 68;
	my $fsize = -s $file;
	my $content;

	#say "fsize: ", $fsize;

	open my $fh, $file or die;
	binmode $fh;
	read($fh, $content, $fsize);
	close $fh;
	my $buf;
	#say "len of content: ", length($content);

	#my $num_of_soldier = ord(substr($content, 0x0e, 1));
	#say "num: ", $num_of_soldier;
	for (my $i=0; $i<$MAX_SOLDIER; ++$i) {
		my $addr = $start_offset + $BLOCK_SIZE * $i;
		my $block = substr($content, $addr, $BLOCK_SIZE);
		#say "len of peice: ", length($block);
		my $soldier_name = substr($block, $name_offset, $name_len);

		if ( ord(substr($soldier_name, 0, 1)) != 0 ) {
			#$soldier_name =~ s/\x00//g;
			#printf("[%-27s]", $soldier_name);

			my $mission = ord(substr($block, $mission_offset, 1));
			my $rank = ord(substr($block, $rank_offset, 1));
			my $kills = ord(substr($block, $kill_offset, 1));
			my $rank = get_rank($mission, $rank, $kills);

            #my $real_name = $soldier_name;
            #$real_name =~ s/(CDR |COL |CPT |SGT |SQD |ROK )+//;
            $soldier_name =~ m/([A-Z][a-z]+ [A-Z][a-z]+)/;
            my $real_name = $1;
            my $proc_name = sprintf("%s %s", $rank, $real_name);

            my $dif_len = $name_len - length($proc_name);
            if ($dif_len > 0) {
                $proc_name = $proc_name . "\x00" x $dif_len;
            } else {
                print "\n";
            }

            # check name length
            if ( length($proc_name) != $name_len ) {
                printf("=> (%d) [%-27s]\n", length($proc_name), $proc_name);
            }

            #printf("=> [%-27s] ", $proc_name);
			#printf("%-30s", $rank);

            substr($block, $name_offset, $name_len) = $proc_name;
            die if (length($block) != $BLOCK_SIZE);
            # read it out again
            my $nn = substr($block, $name_offset, $name_len);
            #printf("=> [%-27s]\n", $nn);
			#show_attr( substr($block, $attr_offset, scalar(@attr_name)) );
		} else {
		    #print "none\n";
			#last;
		}
        $buf = $buf . $block;
	}

	open my $ofh, "> $ofile" or die;
	binmode $ofh;
	print $ofh $buf;
	close $ofh;
}

sub get_rank($$$)
{
	my ($mission, $rank, $kills) = @_;
	my $real_rank = $rank - 20 - $mission;
	my $rank_name;

	#printf("%d,", $mission);
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
		$rank_name = "SQD";
	} elsif ($real_rank >= 0) {
		$rank_name = "ROK";
	}

	#printf("\"%s\",", $rank_name);
	return $rank_name;
	#printf("%d,", $kills);
}

sub main()
{
	parse_soldier();
}

main;

