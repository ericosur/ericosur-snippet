#!/usr/bin/perl

use strict;
use v5.010;

my $file = "DRIVERS";
my $ofile = "DRIVERS-HACK";
my $bfile = "DRIVERS.BAK";

sub get_date()
{
	# compose date/time string for subject
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d%02d%02d-%02d%02d-", $year+1900, $mon + 1, $mday, $hour, $min;
	return $date;
}

sub open_savefile($)
{
	my $file = shift;
	my $fsize = -s $file;
	my $buffer;

	die "zero file size?" if ($fsize <= 0);
	say "fsize = ", $fsize;
	open my $fh, $file or die "file not found?";
    binmode($fh);
    read($fh, $buffer, $fsize);
	close $fh;

	return ($buffer, $fsize);
}

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

# in: buffer
# in: position
# in: len
sub mypeek($$$)
{
	my ($buf,$psi, $len) = @_;
	my $ret = sprintf("%02x", ord(substr($buf, $psi, $len)));
	return $ret;
}

#
#
#
sub mybyte($)
{
	my $inval = shift;
    my $val = pack("H02", $inval);
    return $val;
}

# in: buffer
# current use absolute offset to fix, it may change if add new
# player/car
sub fix_mycar()
{

	my ($buf, $bufsize) = open_savefile($file);

	my $carhead = 0x3778;
	my $armor = 0x379d;
	my $field = 8;
    my $armor_count = 10;
    my $i;
    my $wep_cnt = 0x3802;

    #my $tmp = substr($buf, $carhead, 128);
    #print hexdump($tmp);
    #print "\n";

    # fix armors
    for ($i=0; $i<$armor_count; $i++) {
        substr($buf, $armor+$i*$field, 1) = mybyte(63);
    }
    # refill
    substr($buf, $wep_cnt, 1) = mybyte(63);

    #my $tmp = substr($buf, $carhead, 128);
    #print hexdump($tmp);
    #print "\n";

    # write to file
    my $ofh;
    open $ofh, "> $ofile" or die;
    binmode($ofh);
    print $ofh $buf;
    close $ofh;
}

sub main()
{
	my $daily_backup = get_date() . $file;
    my $cmd;

    # backup first
    $cmd = sprintf("copy /y %s %s", $file, $daily_backup);
    say $cmd;
    system($cmd);

    # do hacking
    fix_mycar();

    # rotate
    unlink $bfile if (-e $bfile);
    rename $file, $bfile;
    rename $ofile, $file;

    my $money = "291826";
    say pack("H02", substr($money, 0, 2));
}


sub change_money_format()
{
    my $money = "291826";

    print "money: $money (big endian) => ";
    for (my $i=length($money)/2-1; $i>=0; --$i) {
	    my $p1 = substr($money, 0+2*$i, 2);
	    printf("%02x ", $p1);
	}
	print "\n";
}

change_money_format;
#main;
