#!/usr/bin/perl

use strict;

use Time::Local;

# Reference:
# Ethereal's log format:
# http://lists.linux-wlan.com/pipermail/linux-wlan-devel/2003-September/002701.html

# History:
# 2006/01/20 First version.
# 2008/05/05 cleanup by rasmus.lai@indigomobile.com.tw

# �ݥ��}MOD_SNDCP�ӿ�Log�A�b�H�U�T������peer_buffer���A�H�u0x45 0x00�v�}�Y�쵲������ƧY��
# IP Packet��ơA�[�H�^����s��Ethereal���榡�Y�i�C
my @msg_wanted = qw(
	MSG_ID_TCPIP_TCM_DATA_REQ
	MSG_ID_TCPIP_TCM_DATA_IND
	MSG_ID_SN_UNITDATA_REQ
	MSG_ID_SN_UNITDATA_IND);

# #####################################
# 1: �ˬd�ѼƬO�_���T
if ($#ARGV != 0) {
  die "Usage: Log2MSCMTK.pl log-filename";
}

my ($logfile) = @ARGV;
if (! -r $logfile) {
  die "Can't read log file: $logfile\n";
}
if (! -f $logfile) {
  die "Log file $logfile is not a plain file\n";
}
# #####################################

# #####################################
open(INPUT,"<$logfile") or die "Can't open log file: $logfile\n";
# #####################################

# #####################################
# �L���Y
# #####################################
binmode(STDOUT);
# 24 bytes header of Ethereal's log format.
my $out = pack "H48", "D4C3B2A1020004000000000000000000ffff000001000000";
print $out;
# #####################################

# #####################################
# ���y���Log�ɡA�N��쪺�H�U�T�����X������IP Packet��Ƥ��H�L�X�G
# MSG_ID_TCPIP_TCM_DATA_IND
#
# #####################################
my $line = 0;
my $TimeStamp;
my $ASCII_Data;
my $IP_Len;

while (<INPUT>) {
	chop;
	++ $line;
	# �b�i�@�B�B�z���e�A�M�w�O�_���n�B�z���T���C
	my $flag = 0;
	for (my $i=0; $i <= $#msg_wanted; $i++) {
		if (/@msg_wanted[$i]/) {
			$flag = 1;
			# ���XFrame�ȡB�b�᭱�L�XEthereal���C��Packet�����Y�ɥi�H�@��Time Stamp�ȡA��K���ѡC
			# 10:53:06:250 2008/05/02
			m[(\d{2})\:(\d{2})\:(\d{2}):\d{3} (\d{4})\/(\d{2})\/(\d{2})];

			#$TimeStamp=$&;
			#@items=split(/[: \/]/, $TimeStamp);
			printf STDERR "line(%d): %d %d %d %d %d %d\n", $line, $1, $2, $3, $4, $5, $6;

			# $TIME = timelocal($sec, $min, $hours, $mday, $mon, $year);
			$TimeStamp = timelocal($3, $2, $1, $6, $5, $4);

			last;
     	}
	}

	next if $flag == 0;

	while (<INPUT>) {
		last if /Peer_Message/;
	}

	$ASCII_Data = "";
	# �����HASCII�r����ܪ�IP Packet���
	while (<INPUT>) {
		# �NTAB�B�ťաB�M��r�����h��
		s/[\t \-\n]//g;
		last if $_ eq "";

		$ASCII_Data = $ASCII_Data . $_;
	}
	# IP Packet
	# �u����"4500"�쵲�������
	$ASCII_Data =~ /4500.*/;
	$ASCII_Data = $&;

	#####################################
	# �i��C�L�ʧ@
	#####################################
	# Ethereal header for IP packet
	# Timestamp uses 8 bytes.
	$out = pack("Lxxxx", $TimeStamp);
	print $out;
	$IP_Len = length($ASCII_Data) / 2 + 14;
	$out = pack("L", scalar($IP_Len));
	print $out;
	print $out;

	# Ethernet II header
	# Destination Mac: 6 bytes +
	# Source Mac: 6 bytes +
	# Type: 2 bytes
	# = 14 bytes
	$out = pack "H28", "0a5f200002000000020000000800";
	print $out;

	$out = pack "H*", $ASCII_Data;
	print $out;
	#####################################
}
