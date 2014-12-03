#!/usr/bin/env perl

=pod

=head1 NOTE

�b linux/macos ���ɦW�� utf8 �s�X�A�p�G������r�����ܡA�b win32
�L�k���`�ѥX�A�� script �|�N tar �ɤ�������r�� utf8 �ର big5�A
�åt�s�s�ɡC

updated: if tar file size is giantic, I suggest another way.
1. use ubuntu to untar it
2. enter cygwin bash, and then untar it

idea from: http://blog.roodo.com/candyz/archives/283970.html
// it seems these articles are removed 2010/04/01
here is a similar one: http://blog.candyz.org/20050405/29
or: http://macblog2.blogspot.com/

=cut

use strict;
use Archive::Tar;
use Encode qw(from_to);

sub check_filename($)
{
	my $oldfn = shift;
	my $newfn = $oldfn;

	from_to($newfn, "UTF8", "BIG5");
	if ($newfn eq $oldfn)  {
		return "";
	}
	else  {
		return $newfn;
	}
}

sub main()
{
	unless (@ARGV)  {
		print "$0 [oldfile] [newfile]\n";
		return;
	}

	unless (-e $ARGV[0])  {
		die "no input file\n";
	}

	unless ($ARGV[1])  {
		die "no output filename\n";
	}

    my $tar = Archive::Tar->new;
    $tar->read($ARGV[0]);
	my @pp = ('name');
	my @ref = $tar->list_files(\@pp);

	for my $fn (@ref) {
		my $nfn = check_filename($fn);
		if ($nfn)  {
			$tar->rename($fn, $nfn);
			print "new: $nfn\n";
		}
	}

	$tar->write($ARGV[1], COMPRESS_GZIP);
}

main;

