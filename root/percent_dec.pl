#!/usr/bin/perl
=pod

=head1 NOTE

To decode percent encoding string from STDIN.
For example, %0A%0D => \r\n

=cut

use strict;

sub decode_percent($)
{
	my $str = shift;
	$str =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	return $str;
}

sub encode_percent($)
{
	#use Encode qw(from_to);
	my $str = shift;
	#from_to($string, "Shift_JIS", "GB2312");
	$str =~ s/(\W)/sprintf("%%%02X",unpack("C",$1))/eg;

	# it is UTF8
	return $str;
}

sub process_file($$)
{
	my $ifile = shift;
	my $ofile = shift;
	my $ifh;
	my $ofh;

	open $ifh, $ifile or die "$ifile: $!";
	if ($ofile eq 'stdout')  {
		$ofh = \*STDOUT;
	}
	else  {
		open $ofh, "> $ofile" or die;
	}

	while (<$ifh>)  {
		my $dec = decode_percent($_);
		print $ofh $dec;
	}
	close $ifh;
	close $ofh;
}

sub main
{
=pod
	# stdin version

	while (<>)  {
		print decode_percent($_);
	}
=cut
	# file i/o version
	my $ifile = $ARGV[0] // "-";
	my $ofile = $ARGV[1] // "stdout";


	process_file($ifile, $ofile);
}

main;
