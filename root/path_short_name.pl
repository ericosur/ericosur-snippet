#!/usr/bin/perl
#
# 分析目前 path 內的路徑，將長檔名格式路徑
# 找出來並列出對應的短檔名路徑
#
# 結果會放入 clipboard
#
# 增加說明性訊息
#
# 2007/01/10 by ericosur
#
# there is a more advanced version: "uniq_short_path.pl"
#

use Win32;
use strict;
use warnings;

use Env qw(@PATH);
use Win32::Clipboard;

#my $dname = Win32::DomainName();
my @result;
my $count = 0;

foreach (@PATH)  {
	$count ++;
#	printf "%d - %s\n", $count, $_;
	if ( -d $_ )  {
		my $short = Win32::GetShortPathName($_);
		my $long = Win32::GetLongPathName($_);
		print STDERR "$_\n  ==>\n$short\n" if ($_ ne $short);
		push @result, $short;
	}
	else  {
		print STDERR "$count: <$_> position not found\n";
	}
}

my $my_inc = join ';', @result;
print "\nThe altered path is:\n";
print "$my_inc\n";

# copy the result into clipboard for further paste
print STDERR "\nAltered path already put into clipboard\n";
Win32::Clipboard::Set($my_inc);
