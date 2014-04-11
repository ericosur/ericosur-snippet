#!/usr/bin/perl

use strict;
use v5.010;

# parse android kcm file and output into CSV

# change $proj to project directory
my $proj = "/src/oasis";
my $base = "frameworks/base/packages/InputDevices/res/raw";
my %keyloc = ();

sub translate($)
{
    my $file = shift;
    my $in_range = 0;

    open my $fh, $file or die;
    my %keymap;
    my $currkey;

    while (<$fh>) {
        next if /^#/;
        next if /^\s*$/;
        if ( m/key (\S+) {/ ) {
            $currkey = $1;
            %keymap = ();
            #$keyloc{$currkey} = \%keymap;
            #say "key ====> $1";
            $in_range = 1;
            next;
        }
        if ($in_range) {
            s/[\r\n]//g;
            if ( m/^\s+([a-z,+ ]+):\s+(.*)$/ ) {
                $keyloc{$currkey}->{$1} = $2;
            }
        }
    }
    close $fh;

}

sub display_keyloc($)
{
    my $ofile = shift;
    open my $ofh, "> $ofile" or die;

    print $ofh "KEY\tLABEL\tSHIFT\tSHIFT_CAPLOCK\tBASE\tRALT\tRALT+SHIFT\n";

    foreach my $kk (keys %keyloc) {
        print $ofh $kk,"\t";
        my $rh = $keyloc{$kk};
        #say $rh;
        my ($labl, $shft, $bse, $ralt) = ('NA','NA','NA','NA');
        my ($shcp, $alsh) = ('NA', 'NA');

        $labl = $rh->{'label'} if $rh->{'label'};
        $shft = $rh->{'shift'} if $rh->{'shift'};
        $shcp = $rh->{'shift, capslock'} if $rh->{'shift, capslock'};
        $bse = $rh->{'base'} if $rh->{'base'};
        $ralt = $rh->{'ralt'} if $rh->{'ralt'};
        $alsh = $rh->{'ralt+shift'} if $rh->{'ralt+shift'};

        printf $ofh "%s\t%s\t%s\t", $labl, $shft, $shcp;
        printf $ofh "%s\t%s\t%s", $bse, $ralt, $alsh;
        #foreach my $mm (keys %$rh) {
        #    say "$mm => $rh->{$mm}";
        #}
        print $ofh "\n";
    }
}

sub main()
{
    my @files = glob($proj . '/' . $base . '/' . '*.kcm');
    foreach (@files) {
        my $ifile = $_;
        my $ofile;

        $ifile =~ m/\/(\w+\.kcm)$/;
        $ofile = $1;
        $ofile =~ s/\.kcm/\.csv/;
        $ofile =~ s/keyboard_layout_//;

		print STDERR "$ofile\n";

        translate($ifile);
        display_keyloc($ofile);
    }
}

main;

__END__
key GRAVE {
    label:                              '`'
    base:                               '`'
    shift:                              '~'
}
