#!/usr/bin/env perl

use strict;

sub process_one_file($)
{
    my $fn = shift;
    if ( -e $fn ) {
        my $cmd = sprintf("mediainfo \"%s\"", $fn);
        my $ret = get_stdout($cmd);
        my @prop = grep_output($ret);
        printf("\"%s\",\"%s\",\"%s\"\n", $fn, $prop[0], $prop[1]);
    } else {
        printf("file not found: %s\n", $fn);
    }

}

sub grep_output($)
{
    my $inp = shift;
    my @ret = ();
    for my $ln (split(/\n/, $inp)) {
        if ( $ln =~ m/Bit depth\s+:\s+(\d+) bits/ ) {
            #printf("%s bits\n", $1);
            push @ret, $1;
        }
        if ( $ln =~ m/Sampling rate\s+:\s+(\d+\.?\d+?) kHz/ ) {
            #printf("%s kHz\n", $1);
            push @ret, $1;
        }
    }
    return @ret;
}

sub get_stdout($)
{
    my $exec_cmd = shift;
    open CMD,'-|', $exec_cmd or die $@;
    my $line;
    my $ret;
    while (defined($line=<CMD>)) {
        $ret = $ret . $line;
    }
    close CMD;
    return $ret;
}

sub process_list($)
{
    my $fn = shift;
    open my $fh, $fn or die;
    while (<$fh>) {
        s/[\r\n]//;
        my $ln = $_;
        process_one_file($ln);
    }
    close($fh);
}

sub main()
{
    process_list('list.txt');
}

main;
