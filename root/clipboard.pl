#!/usr/bin/perl
#
# ��ǤJ�� ARGV[0] �s��ŶKï�̭�
#
# ��o�� perl script �ন batch, ��b sendto ��Ƨ���
# ����b�ɮ��`�פ��� �u�ǰe��v�ϥΡA�N�i�H�⧹����|
# �Ǩ�ŶKï�̭�
#
# active perl �̭��� pl2bat �i��
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
