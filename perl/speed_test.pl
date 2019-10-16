#!/usr/bin/perl
#
# benchmark on some digest/hash functions
#


use strict;
use warnings;

use Digest::MD5;
use Digest::MD4;
use Digest::SHA;	# include sha1, sha224, sha256, sha384, sha512
use Digest::SHA1;	# only sha1
use String::CRC32;

use Data::Dump qw(dump);
use Benchmark ':hireswallclock';

my $fh;
#my $file;

# specify a file name while large enough
if (!@ARGV)  {
	print "need specify a file\n";
	exit;
}

my @all = ( @ARGV
			#, q(D:\ericosur-google\tmp\oxford.iso)
			);

sub run_test($$)
{
	my ($test_func, $msg) = @_;
	my $file_size = 0;

	#print dump(@_);

	my $t0 = new Benchmark;
	START:
	for (@all)  {
		s/\n//;
		if (-f $_)  {
			print STDERR "test using $_ >>>>>\n";
		}
		else  {
			print STDERR "$_ not exist, skips\n";
			next START;
		}
		$file_size = -s $_;
		open $fh, $_ or die;
		binmode $fh;
		&$test_func;
		close $fh;
	}
	my $t1 = new Benchmark;
    my $td = timediff($t1, $t0);

	#printf STDERR "\ncalc_%s() took: %s\n", $msg, timestr($td);
	#print STDERR dump($td);
	#print STDERR "size = $file_size\n";
	if ($td->[0] != 0)  {
		my $result = show_size($file_size / $td->[0]);
		print "$msg: $result/s\n";
	}

	undef $t0;
	undef $t1;
	undef $td;
}

sub show_size()
{
	my @unit = qw(B KB MB GB);
	my $cnt = 0;
	my $fsize = shift;

	while ($fsize > 1024)  {
		++ $cnt;
		$fsize /= 1024;
	}

	return $fsize . ' ' . $unit[$cnt];
}

# crc32 digest
sub calc_crc32
{
	my $crc;
	$crc = crc32(*$fh);
}

# md5 hash
sub calc_md5
{
	my $md5;

	$md5 = Digest::MD5->new->addfile(*$fh)->hexdigest;
#	print "md5:\t$md5\n";
}

# md4 hash
sub calc_md4
{
	my $md4;

	$md4 = Digest::MD4->new->addfile(*$fh)->hexdigest;
#	print "md4:\t$md4\n";
}

# sha1 from Digest::SHA1
sub calc_sha1
{
	my $sha1 = Digest::SHA1->new;

	my $result = $sha1->addfile(*$fh)->hexdigest;
#	print "sha1:\t$result\n";
}


# sha1 from Digest::SHA(sha1)
sub calc_sha1_v2
{
	my $sha1 = Digest::SHA->new('sha1');
	my $result = $sha1->addfile(*$fh)->hexdigest;
	print "$result\t";
}

sub calc_sha224
{
	my $sha1 = Digest::SHA->new('sha224');
	my $result = $sha1->addfile(*$fh)->hexdigest;
	print "$result\t";
}

sub calc_sha256
{
	my $sha1 = Digest::SHA->new('sha256');
	my $result = $sha1->addfile(*$fh)->hexdigest;
	print "$result\t";
}

sub calc_sha384
{
	my $sha1 = Digest::SHA->new('sha384');
	my $result = $sha1->addfile(*$fh)->hexdigest;
	print "$result\t";
}

# input calc_sha_all(sha224, sha256, sha384, sha512
sub calc_sha_all
{
	#print dump(@_);
	my $alg = shift;
	my $sha = Digest::SHA->new($alg);
	my $result = $sha->addfile(*$fh)->hexdigest;
#	print "$alg:\t$result\n";
}


#
#
#			START HERE
#
#

#	open my $flist, "list.txt" or die;
#	@all = <$flist>;
#	close $flist;

	run_test(\&calc_crc32, 'crc32');
	run_test(\&calc_md5, 'md5');
#	run_test(\&calc_md4, 'md4');
	run_test(\&calc_sha1, 'sha1');
#	run_test(\&calc_sha1_v2, 'sha1v2');

# input calc_sha_all(sha224, sha256, sha384, sha512
#	run_test(\&calc_sha224, 'sha224');
#	run_test(\&calc_sha256, 'sha256');

# eof
__END__
