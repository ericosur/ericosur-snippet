#!/usr/bin/perl

use Digest::SHA3 qw(sha3_224_hex sha3_256_hex sha3_384_base64 sha3_512_hex);


sub show($)
{
    my $d = shift;
    print $d,"\n";
}

sub main()
{
    $date = "1234";

    $digest = sha3_224_hex($data);
    show($digest);
    $digest = sha3_256_hex($data);
    show($digest);
    $digest = sha3_384_base64($data);
    show($digest);
    $digest = sha3_512_hex($data);
    show($digest);
    # $digest = sha3_0_hex($data);
    # show($digest);
}

main();
