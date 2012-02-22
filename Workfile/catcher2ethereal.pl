#!/usr/bin/perl

use strict;

use Time::Local;

# Reference:
# Ethereal's log format:
# http://lists.linux-wlan.com/pipermail/linux-wlan-devel/2003-September/002701.html

# History:
# 2006/01/20 First version.
# 2008/05/05 cleanup by rasmus.lai@indigomobile.com.tw

# 需打開MOD_SNDCP來錄Log，在以下訊息內的peer_buffer中，以「0x45 0x00」開頭到結尾的資料即為
# IP Packet資料，加以擷取後存成Ethereal的格式即可。
my @msg_wanted = qw(
	MSG_ID_TCPIP_TCM_DATA_REQ
	MSG_ID_TCPIP_TCM_DATA_IND
	MSG_ID_SN_UNITDATA_REQ
	MSG_ID_SN_UNITDATA_IND);

# #####################################
# 1: 檢查參數是否正確
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
# 印檔頭
# #####################################
binmode(STDOUT);
# 24 bytes header of Ethereal's log format.
my $out = pack "H48", "D4C3B2A1020004000000000000000000ffff000001000000";
print $out;
# #####################################

# #####################################
# 掃描整個Log檔，將找到的以下訊息取出內部的IP Packet資料予以印出：
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
	# 在進一步處理之前，決定是否為要處理的訊息。
	my $flag = 0;
	for (my $i=0; $i <= $#msg_wanted; $i++) {
		if (/@msg_wanted[$i]/) {
			$flag = 1;
			# 取出Frame值、在後面印出Ethereal給每個Packet的檔頭時可以作為Time Stamp值，方便辨識。
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
	# 收集以ASCII字元表示的IP Packet資料
	while (<INPUT>) {
		# 將TAB、空白、和減號字元都去掉
		s/[\t \-\n]//g;
		last if $_ eq "";

		$ASCII_Data = $ASCII_Data . $_;
	}
	# IP Packet
	# 只收錄"4500"到結尾的資料
	$ASCII_Data =~ /4500.*/;
	$ASCII_Data = $&;

	#####################################
	# 進行列印動作
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
