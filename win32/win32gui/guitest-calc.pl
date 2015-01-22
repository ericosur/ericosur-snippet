use strict;
use Win32::GuiTest qw(:ALL);
use Data::Dump qw(dump);


my @hwd = FindWindowLike(undef, "¤pºâ½L");
dump(@hwd);
my $hw = $hwd[0];
my @ar = GetChildWindows($hw);
my $text;
foreach my $child (@ar)  {
	$text = GetWindowText($child);
	print $text,"\n" if $text;
}
