#!/usr/bin/perl
use strict;
use Fcntl qw(SEEK_END SEEK_CUR SEEK_SET);

# 如果要破壞 zip 內資料的內容，可以尋找 PK 0x03 0x04
# POS+22 (filename len) , skip filename 找地方破壞


my $in_file = $ARGV[0] || 'src.zip';
my $out_file = $in_file;
my $in_fsize = -s $in_file;
my $plan_fsize = $in_fsize;	# int($in_fsize * 0.9);
my $SIGNATURE = 'PK' . chr(0x01) . chr(0x02);

$out_file =~ s[(.*?)\.zip][_$1.zip];
unlink $out_file if -e $out_file;

printf "%s(%d), %s(%d)\n",
	$in_file, $in_fsize,
	$out_file, $plan_fsize;

open IN_FILE, $in_file;
binmode IN_FILE;

#open OUT_FILE, "> $out_file";
#binmode OUT_FILE;

sysseek IN_FILE, 0, SEEK_SET;

my $readbuf;
my $readsize;
my $total_write = 0;
my $damage_length = 0x40;
my $damage_char = chr(0xBF) . chr(0xE0);
my $damage_buf;

for (1..$damage_length/2)
{
	$damage_buf .= $damage_char;
}

$readsize = sysread IN_FILE, $readbuf, $in_fsize;

# to find the local file signature
while ( $readbuf =~ m/$SIGNATURE/g )
{
	my $local_pos = pos $readbuf;
	printf "%08x: ", $local_pos;
	get_local_info($local_pos);
}

#substr($readbuf, 0xa0, $damage_length) = $damage_buf;

#syswrite OUT_FILE, $readbuf, $plan_fsize;


close IN_FILE;
#close OUT_FILE;


#
#
#
sub get_local_info($)
{
	my $poss = shift;
	my $res;
# crc-32 (+10)
	$res = get_offset($poss, 12, 4);
	printf "crc %08x\t", $res;
	$res = get_offset($poss, 16, 4);
	printf "u %8d\t", $res;
	$res = get_offset($poss, 20, 4);
	printf "c %8d\n", $res;

}

#
#
#
sub get_offset($$)
{
	my $sign_pos = shift;
	my $offset = shift;
	my $len = shift;

	my $var = substr $readbuf, $sign_pos+$offset, $len;

	my @list = unpack "V*", $var;
	my $var = $list[0];

	return $var;
}
