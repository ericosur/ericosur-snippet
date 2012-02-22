#!/usr/bin/perl
#!/bin/perl

=pod

=head1 DESCRIPTION
 
md5.pl

 July 17 2002 by ericosur
 test on Digest::MD5

 fix the bug without using binary mode

=cut

use strict;
use warnings;

use Digest::MD5;
use Digest::MD4;
use Digest::SHA1;

my $md5;
my $md4;
my $sha1;

my $file = $ARGV[0] || $0;

die "cannot open $!\n" unless (-e $file);
print "check file <$file>\n";

# md5 hash

open FH, $file;
binmode(FH);
$md5 = Digest::MD5->new->addfile(*FH)->hexdigest;
close FH;

print "md5:\t$md5\n";


# md4 hash

#open FH, $file;
#binmode(FH);
#$md4 = Digest::MD4->new->addfile(*FH)->hexdigest;
#close FH;
#
#print "md4:\t$md4\n";


# sha-1 hash

open FH, $file;
binmode(FH);
$sha1 = Digest::SHA1->new->addfile(*FH)->hexdigest;
close FH;

print "sha1:\t$sha1\n";


__END__;
# just for usage reference
 use MD5;
 $context = new MD5;
 $context->reset();
 $context->add(LIST);
 $context->addfile(HANDLE);
 $digest = $context->digest();
 $string = $context->hexdigest();
 $digest = MD5->hash(SCALAR);
 $string = MD5->hexhash(SCALAR);

 # Functional style
 use Digest::MD5  qw(md5 md5_hex md5_base64);
 $digest = md5($data);
 $digest = md5_hex($data);
 $digest = md5_base64($data);
 # OO style
 use Digest::MD5;
 $ctx = Digest::MD5->new;
 $ctx->add($data);
 $ctx->addfile(*FILE);
 $digest = $ctx->digest;
 $digest = $ctx->hexdigest;
 $digest = $ctx->b64digest;

  $md5  = Digest->new("MD5");
  $sha1 = Digest->new("SHA-1");
  $sha256 = Digest->new("SHA-256");
  $sha384 = Digest->new("SHA-384");
  $sha512 = Digest->new("SHA-512");

  $hmac = Digest->HMAC_MD5($key);

