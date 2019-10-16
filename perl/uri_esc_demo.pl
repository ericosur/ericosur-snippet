#!/usr/bin/perl
use URI::Escape::XS;

sub go($)
{
	my $str = shift;
	my $safe = encodeURIComponent($str);
	print $safe,"\n";
}


$path = q(@@@@ 程式設計技術\0001 技術文件工作\1999論文研討.rar);
go($path);

$str =<<EOL;
!*'();:@&=+$,/?%#[]'
EOL

go($str);
