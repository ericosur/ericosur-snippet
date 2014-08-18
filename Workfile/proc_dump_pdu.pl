#!/usr/bin/perl
#
# process hex byte text dumped from catcher
# here is a demo data attached after this script line 91
#
# Usage: proc_dump_pdu.pl  <dumped file>  > output file
#
# add a stupid guessing function to fetch possible tag position
# It could be extended to parse such PDU.
#

# reference: OMA-MMS-ENC-V1_2-20050301-A.pdf
# content type in numeric:
# WAP-230-WSP-20010705-a.pdf
# refer to http://www.wapforum.org/wina/wsp-content-type.htm

use strict;
use warnings;

my $debug = 0;

# [in] ascii value for octet link 7f 2c (in hex form)
# [in] the output handle
sub print_octet($$)
{
	my ($ch, $ofh) = @_;

	if ($ch =~ m/[0-9A-Fa-f]{2}/)  {
		$ch = '0x' . $ch;
		print $ofh chr(hex($ch));
	}
	else  {
		print STDERR "invalide char: %s\n", $ch;
	}
}

# [in] octet in hex form like ''8c'' ''96''
# [in] the byte count
sub mms_pdu_lookup($$)
{
	my ($ch, $ps) = @_;
	$ps --;	# differ by one
	my %lookup = (
		'83' => 'X-Mms-Content-Location',
		'84' => 'Content-Type',
		'85' => 'Date',
		'86' => 'X-Mms-Delivery-Report',
		'87' => 'X-Mms-Delivery-Time',
		'89' => 'From',
		'8A' => 'X-Mms-Message-Class',
		'8B' => 'Message-ID',
		'8C' => 'X-Mms-Message-Type',
		'8E' => 'X-Mms-Message-Size',
		'96' => 'Subject',
		'97' => 'To',
		'99' => 'X-Mms-Retrieve-Status',
		'9A' => 'X-Mms-Retrieve-Text',
		'92' => 'X-Mms-Response-Status',
		'93' => 'X-Mms-Response-Text',
	);

	if ($lookup{$ch})  {
		printf STDERR "%08Xh: %s => %s\n", $ps, $ch, $lookup{$ch};
	}
}

#
# main procedure here
#

my $file = $ARGV[0] || '-';
my $fh;

binmode STDOUT;

if ($file eq '-')  {
	$fh = \*DATA;
}
else  {
	open $fh, $file or die;
}

my $byte_count = 0;

# process each line like:
# 	0 - 15 = b3 03 03 00 80 00 00 00 - 00 00 00 00 a4 d5 47 00
while (<DATA>) {
#	s/\n//;
	s/(.*) =//;
	s/-//;
	s/^\s+//;
	next if /^#/;
	next if /^$/;

	if ($debug)  {
		print;
		next;
	}

	for my $cc (split /\s+/)  {
		++ $byte_count;
		print_octet($cc, \*STDOUT);
		mms_pdu_lookup($cc, $byte_count);
	}
}

close $fh;
print STDERR "total byte count = $byte_count\n";


__DATA__
Local Parameter =
	NULL =
Peer Message =
	0 - 15 = b3 03 03 00 80 00 00 00 - 00 00 00 00 a4 d5 47 00
	16 - 31 = 7f 03 00 00 00 00 00 00 - 7f 03 00 00 00 00 00 00
	32 - 47 = 07 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	48 - 63 = 00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	64 - 79 = 00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	80 - 95 = 00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	96 - 111 = 00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	112 - 127 = 00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	128 - 143 = 00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00 00
	144 - 159 = 00 06 03 9f d2 f1 c7 c7 - 0a 61 04 0d 23 f1 f3 26
	160 - 175 = 3c 2e 19 89 bc 49 77 ca - 80 18 40 80 00 00 00 00
	176 - 191 = 01 01 08 0a 29 94 84 69 - 00 29 78 75 48 54 54 50
	192 - 207 = 2f 31 2e 31 20 32 30 30 - 20 4f 4b 0d 0a 53 65 72
	208 - 223 = 76 65 72 3a 20 52 65 73 - 69 6e 2f 32 2e 31 2e 36
	224 - 239 = 0d 0a 43 6f 6e 74 65 6e - 74 2d 54 79 70 65 3a 20
	240 - 255 = 61 70 70 6c 69 63 61 74 - 69 6f 6e 2f 76 6e 64 2e
	256 - 271 = 77 61 70 2e 6d 6d 73 2d - 6d 65 73 73 61 67 65 0d
	272 - 287 = 0a 43 6f 6e 74 65 6e 74 - 2d 4c 65 6e 67 74 68 3a
	288 - 303 = 20 36 34 33 0d 0a 44 61 - 74 65 3a 20 54 75 65 2c
	304 - 319 = 20 30 38 20 41 70 72 20 - 32 30 30 38 20 30 36 3a
	320 - 335 = 31 39 3a 34 31 20 47 4d - 54 0d 0a 56 69 61 3a 20
	336 - 351 = 31 2e 31 20 77 61 70 2d - 61 70 31 2e 66 61 72 65
	352 - 367 = 61 73 74 6f 6e 65 2e 63 - 6f 6d 2e 74 77 3a 38 30
	368 - 383 = 38 30 0d 0a 43 6f 6e 6e - 65 63 74 69 6f 6e 3a 20
	384 - 399 = 63 6c 6f 73 65 0d 0a 57 - 61 72 6e 69 6e 67 3a 20
	400 - 415 = 32 31 34 20 20 4d 53 50 - 2d 50 52 4f 58 59 20 54
	416 - 431 = 72 61 6e 73 66 6f 72 6d - 61 74 69 6f 6e 41 70 70
	432 - 447 = 6c 69 65 64 0d 0a 0d 0a - 8c 84 98 31 31 38 32 31
	448 - 463 = 35 34 30 31 00 8d 90 8b - 31 31 38 32 31 35 34 30
	464 - 479 = 30 40 6d 6d 73 2e 6d 6e - 63 30 30 31 2e 6d 63 63
	480 - 495 = 34 36 36 2e 67 70 72 73 - 00 85 04 47 fb 08 00 89
	496 - 511 = 19 80 2b 38 38 36 39 38 - 39 39 31 37 32 32 31 2f
	512 - 527 = 54 59 50 45 3d 50 4c 4d - 4e 00 97 30 39 38 39 39
	528 - 543 = 31 37 32 32 31 2f 54 59 - 50 45 3d 50 4c 4d 4e 00
	544 - 559 = 96 54 65 73 74 00 8a 80 - 8f 81 86 81 90 81 84 1b
	560 - 575 = b3 89 61 70 70 6c 69 63 - 61 74 69 6f 6e 2f 73 6d
	576 - 591 = 69 6c 00 8a 3c 4d 4d 4d - 4d 3e 00 02 2d 83 08 1b
	592 - 607 = 61 70 70 6c 69 63 61 74 - 69 6f 6e 2f 73 6d 69 6c
	608 - 623 = 00 85 73 2e 73 6d 69 6c - 00 81 ea c0 22 3c 4d 4d
	624 - 639 = 4d 4d 3e 00 8e 73 2e 73 - 6d 69 6c 00 3c 73 6d 69
	640 - 655 = 6c 3e 0a 3c 68 65 61 64 - 3e 0a 3c 6c 61 79 6f 75
	656 - 671 = 74 3e 0a 3c 72 6f 6f 74 - 2d 6c 61 79 6f 75 74 20
	672 - 687 = 68 65 69 67 68 74 3d 22 - 34 30 70 78 22 20 77 69
	688 - 703 = 64 74 68 3d 22 39 36 70 - 78 22 2f 3e 0a 0a 3c 72
	704 - 719 = 65 67 69 6f 6e 20 66 69 - 74 3d 22 6d 65 65 74 22
	720 - 735 = 20 68 65 69 67 68 74 3d - 22 31 30 30 25 22 20 69
	736 - 751 = 64 3d 22 49 6d 61 67 65 - 22 20 6c 65 66 74 3d 22
	752 - 767 = 30 25 22 20 74 6f 70 3d - 22 30 25 22 20 77 69 64
	768 - 783 = 74 68 3d 22 31 30 30 25 - 22 2f 3e 0a 0a 3c 72 65
	784 - 799 = 67 69 6f 6e 20 66 69 74 - 3d 22 73 63 72 6f 6c 6c
	800 - 815 = 22 20 68 65 69 67 68 74 - 3d 22 31 30 30 25 22 20
	816 - 831 = 69 64 3d 22 54 65 78 74 - 22 20 6c 65 66 74 3d 22
	832 - 847 = 30 25 22 20 74 6f 70 3d - 22 30 25 22 20 77 69 64
	848 - 863 = 74 68 3d 22 31 30 30 25 - 22 2f 3e 0a 0a 3c 2f 6c
	864 - 879 = 61 79 6f 75 74 3e 0a 0a - 3c 2f 68 65 61 64 3e 0a
	880 - 895 = 0a 3c 62 6f 64 79 3e 0a - 3c 70 61 72 20 64 75 72
	896 - 911 = 3d 22 35 30 30 30 6d 73 - 22 3e 0a 3c 74 65 78 74
	912 - 927 = 20 72 65 67 69 6f 6e 3d - 22 54 65 78 74 22 20 73
	928 - 943 = 72 63 3d 22 66 37 66 65 - 30 32 30 31 2e 74 78 74
	944 - 959 = 22 3e 0a 3c 70 61 72 61 - 6d 20 6e 61 6d 65 3d 22
	960 - 975 = 66 6f 72 65 67 72 6f 75 - 6e 64 63 6f 6c 6f 72 22
	976 - 991 = 20 76 61 6c 75 65 3d 22 - 23 30 30 30 30 30 30 22
	992 - 1007 = 2f 3e 0a 3c 2f 74 65 78 - 74 3e 0a 0a 3c 2f 70 61
	1008 - 1023 = 72 3e 0a 0a 3c 2f 62 6f - 64 79 3e 0a 0a 3c 2f 73
	1024 - 1039 = 6d 69 6c 3e 31 04 11 83 - 81 ea 85 66 37 66 65 30
	1040 - 1055 = 32 30 31 2e 74 78 74 00 - c0 22 3c 66 37 66 65 30
	1056 - 1071 = 32 30 31 2e 74 78 74 3e - 00 8e 66 37 66 65 30 32
	1072 - 1082 = 30 31 2e 74 78 74 00 46 - 61 6c 6c
