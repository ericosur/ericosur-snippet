#!/usr/bin/perl

use strict;
use v5.10;

#
# hexdump()
#
sub hexdump($)
{
	my $foo = shift;
	my $len = length($foo);
	my $ret;

	#print "hexdump(): len=", $len, "\n";
	for my $ii (0..$len-1) {
		$ret = $ret . sprintf("%02x ", ord(substr($foo, $ii, 1)));
	}
	#print "\n";
	return $ret;
}

=pod
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
=cut

sub parse_soldier()
{
	my $file = "SOLDIER.DAT";
	my $ofile = "SOLDIER-HACK.DAT";
	my $start_offset = 0;
	my $mission_offset = 8;
	my $kill_offset = 10;
	my $rank_offset = 14;
	my $NAME_OFFSET = 16;
	my $ATTR_OFFSET = 42;
	my $NAME_LEN = 25;
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
		my $soldier_name = substr($block, $NAME_OFFSET, $NAME_LEN);

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

            my $dif_len = $NAME_LEN - length($proc_name);
            if ($dif_len > 0) {
                $proc_name = $proc_name . "\x00" x $dif_len;
            } else {
                print "\n";
            }

            # check name length
            if ( length($proc_name) != $NAME_LEN ) {
                printf("=> (%d) [%-27s]\n", length($proc_name), $proc_name);
            }

            #printf("=> [%-27s] ", $proc_name);
			#printf("%-30s", $rank);

            substr($block, $NAME_OFFSET, $NAME_LEN) = $proc_name;
            die if (length($block) != $BLOCK_SIZE);

            # read it out again
            #my $nn = substr($block, $NAME_OFFSET, $NAME_LEN);
            #printf("=> [%-27s]\n", $nn);

            # modify power values
            my @attr_name = qw(TimeUnit Health Stamina Reaction Strength
                    FiringAcc ThrowingAcc MeleeAcc PsiStrength);
            my $num_attr = scalar(@attr_name);
            my $powers = substr($block, $ATTR_OFFSET, $num_attr);
            my $ret = hexdump($powers);
            #print "$ret\n";
            my $new_power = alter_power($ret);
            #print "$new_power\n";
            my $cmd = sprintf("H%d", $num_attr*2);
            $powers = pack($cmd, $new_power);
            #say hexdump($power_bin);
            substr($block, $ATTR_OFFSET, $num_attr) = $powers;

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

sub alter_power($)
{
    my $in = shift;
    my @toks = split(/ /, $in);
    my $ret;
    my $SET_TU = 199;
    my $cnt = 0;
    my $debug = 0;

    foreach my $tt (@toks) {
        if ($cnt == 0) {
            $tt = sprintf("%02x", $SET_TU);  # TU
        }
        my $vv = hex($tt);
        if ($vv > 100) {
            $ret = $ret . $tt;
        } else {
            while ($vv < 65) {
                $vv += 9;
            }
            $vv = int(sqrt($vv) * 10.0);
            $ret = $ret . sprintf("%02x",$vv);
        }
        if ($debug) {
            $ret = $ret . ' ';
        }
        ++ $cnt;
    }
    if ($debug) {
        print " $ret\n";
    }
    return $ret;
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

