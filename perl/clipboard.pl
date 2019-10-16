#!/usr/bin/perl
#
# 把傳入的 ARGV[0] 存到剪貼簿裡面
#
# 把這個 perl script 轉成 batch, 放在 sendto 資料夾內
# 之後在檔案總案內的 「傳送到」使用，就可以把完整路徑
# 傳到剪貼簿裡面
#
# active perl 裡面有 pl2bat 可轉
#
# keywords: clipboard, full path, file name, sendto
#
# Oct 6 2007 by ericosur

die "run only at win32" if $^O ne 'MSWin32';
use if $^O eq 'MSWin32', 'Win32::Clipboard';

my $buf;

# if arguments exist
if (@ARGV)  {
	$buf = join(' ', @ARGV);
}
else {	# take content from STDIN
	while (<STDIN>)  {
		$buf .= $_;
	}
}

print $buf;
Win32::Clipboard::Set($buf);
