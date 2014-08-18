#!/usr/bin/perl
#
# unicode in the string
# 2006/12/27 by ericosur
#

my $count = 0;

sub main()
{
	$str = "\x{597D}";	# unicode ''好''
	show($str, 'unicode');

	$str = "\xa6\x6e";	# big5 ''好''
	show($str, 'big5');

	$str = "\xba\xc3";	# gb ''好'' also
	show($str, 'GB');

	$str = "好";	# this string would depend the file encoding
	show($str, 'file');
}

sub show()
{
	my ($str, $type) = @_;

	$count ++;
	printf "%d(%s): %s\n", $count, $type, $str;
}

main();
