#!/usr/bin/perl

my $bom = pack("CCC",0xef,0xbb,0xbf);

sub remove_bom($)
{
	my $str = shift;
	$str =~ s/\xef\xbb\xbf//;
	return $str;
}

sub main
{
	my $iff = $ARGV[0] or die "please specify file name!";
	open my $ifh, $iff or die;
	while (<$ifh>)  {
		my $line = remove_bom($_);
		print $line;
	}
	close $ifh;
}

main;
