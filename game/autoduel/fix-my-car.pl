#!/usr/bin/perl

use strict;
use v5.10;

my $SAVEFILE = "DRIVERS";
#
# hexdump()
#
sub hexdump($)
{
	my $foo = shift;
	my $len = length($foo);
	my $linebreak = 1;
	my $cnt = 0;
	my $ret;

	#print "hexdump(): len=", $len, "\n";
	for my $ii (0..$len-1) {
		if ($linebreak && $cnt % 16 == 15) {
			$ret = $ret . "\n";
			$cnt = 0;
		}
		$ret = $ret . sprintf("%02x ", ord(substr($foo, $ii, 1)));
		$cnt ++;
	}
	#print "\n";
	return $ret;
}

sub mypeek($$$)
{
	my ($buf,$psi, $len) = @_;
	my $ret = sprintf("%02x", ord(substr($buf, $psi, $len)));
	return $ret;
}

sub parse_soldier()
{
	my $file = $SAVEFILE;
#	my $ofile = "SOLDIER-HACK.DAT";
    my $buf_size = 200;
	my $start_offset = 0x3778;	# start offset
	my ($battery1, $battery2) = (34, 35);
    my $armor = 37;
    my $content;
# 0x379d
	open my $fh, $file or die;
	binmode $fh;
	seek($fh, $start_offset, 0);
	my $ret = read($fh, $content, $buf_size);
	close $fh;

    printf("ret = %d\nsize=%d\n", $ret, length($content));

    print hexdump($content);

    for (my $i=0; $i<13; $i++) {
		print mypeek($content, $armor+8*$i, 1), "\n";
    }
=pod
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
=cut
}



sub main()
{
	parse_soldier();
}

main;

