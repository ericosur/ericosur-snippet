#!/usr/bin/env perl

# http://programmingpraxis.com/2014/12/19/diana-cryptosystem/
# http://home.earthlink.net/~specforces/spdiana.htm

use strict;
use Getopt::Std;
#use Data::Dump qw(dump);

my $a2z = q(ABCDEFGHIJKLMNOPQRSTUVWXYZ);
my $z2a = scalar reverse $a2z;
my $Z2A = $z2a;

# input 'A' output lookup string
sub jumplookup($$)
{
    my ($lhs, $rhs) = @_;

    my $i = rindex $a2z, $lhs;
    if ($i == -1) {
        return "<$lhs>";
    }

    my $j = rindex $a2z, $rhs;
    #print "i:$i\n";
    my $look =  substr($Z2A, $i, 26-$i) . substr($Z2A, 0, $i);

    #print $look,"\n";
    die if length($look)!=26;

    my $res = substr($look, $j, 1);
    #printf("%s / %s -> %s\n", $lhs, $rhs, $res);
    return $res;
}

sub show_otp($)
{
    my $res = shift;
    $res = uc($res);
    $res =~ s/ //g;
    print $res;
}


sub decrypt($$)
{
    my $otp = shift;
    my $cip = shift;
    my $debug = 0;

    $otp = uc($otp);
    $otp =~ s/[\r\n\s]//g;
    $cip = uc($cip);
    $cip =~ s/[\r\n\s]//g;

    print "<$cip>\n" if $debug;
    if (length($cip) > length($otp)) {
        die "cipher is too long";
    } else {
        print "len: ", length($cip), "\n" if $debug;
    }
    # skip first 10 char
    my $ans = " " x 10;
    $otp = substr($otp, 10, length($otp)-10);
    print "head:",substr($cip,0,10),"\n" if $debug;
    $cip = substr($cip, 10, length($cip)-10);
    print "cip:$cip,len:",length($cip),"\n" if $debug;
    for (my $i=0; $i<length($cip); $i++) {
        my $oo = substr($otp, $i, 1);
        my $pp = substr($cip, $i, 1);
         $ans = $ans . jumplookup($oo, $pp);
    }
    return $ans;
}

sub space_every5($)
{
    my $str = shift;
    my $i=0;
    my $j=0;
    for my $cc (split(//,$str)) {
        $i ++;
        print $cc;
        if ($i%5==0) {
            print " ";
            $j++;
        }
        if ($j!=0&&$j%5==0) {
            print "\n";
            $j=0;
        }
    }
    print "\n";
}

sub read_otp($)
{
    my $inf = shift;
    my $otp;

    open my $fh, $inf or die;
    while (<$fh>) {
        $otp = $otp . $_;
    }
    close $fh;

    #show_otp($otp);
    return $otp;
}

sub help()
{
    print<<HELP;
available arguments:
    -h      this help
    -i      cipher text to decrypt
    -f      file contain otp <OPTIONAL>
    -p      otp <MUST>
HELP
    exit;
}


sub main()
{
    my %opts;
    getopts('hi:p:f:',\%opts) || help();

    my $default=<<EOL;
BNUVO JOJMR TATAF WEIRO AIBBY
PPKJL ATXDY ETEGD NOZYH UNZMZ
NAYMB SARZF ATZLS
EOL
    my $msg = $opts{'i'} // $default;
    my $otp;
    my $inf = $opts{'f'};

    if (-e $inf) {
        $otp = read_otp($inf);
    } else {
        $otp = $opts{'p'};
    }
    unless ($otp) {
        print "must has OTP\n";
        help();
    }

    #show_otp($otp);
    print "-" x 40,"\n";
    print "OTP =>\n";
    print $otp;

    print "INPUT =>\n";
    my $inp = $msg;
    $inp = uc($inp);
    $inp =~ s/[\r\n\s]//g;
    space_every5($inp);

    print "-" x 40,"\n";
    print "CIPHER =>\n";
    #print jumplookup('S', 'A');
    my $cipher = decrypt($otp, $msg);
    #print $cipher,"\n";
    space_every5($cipher);

=pod
    # decrypt to verify
    print "-" x 40,"\n";
    print "DECRYPT =>\n";
    my $plain = decrypt($otp, $cipher);
    space_every5($plain);
    print "-" x 40,"\n";
=cut
}

main;
