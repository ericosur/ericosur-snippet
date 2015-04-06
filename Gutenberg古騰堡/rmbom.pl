#!/usr/bin/perl

=pod

=head1 DESCRIPTION

remove 0xef 0xbb 0xbf from beginning of text file

=cut

my $bom = pack("CCC",0xef,0xbb,0xbf);

sub remove_bom($)
{
	my $str = shift;
	$str =~ s/\xef\xbb\xbf//;
	return $str;
}

sub process_file($)
{
	my $iff = shift;
	my $off = $iff;

	$off =~ s/pg/nobomb/;
	open my $ifh, $iff or die;
	open my $ofh, "> $off" or die;
	while (<$ifh>)  {
		my $line = remove_bom($_);
		print $ofh $line;
	}
	close $ofh;
	close $ifh;
}

sub main()
{
    my @ar = glob("pg*.txt");
    foreach my $ff (@ar) {
    	process_file($ff);
    }
}

main;
