#!/usr/bin/env perl

# module mp3::info demo

use strict;
use MP3::Info;
use Data::Dump qw(dump);

sub get_info($)
{
    my $file = shift;
    my $tag = get_mp3tag($file) or die "No TAG info";
    dump($tag);

    my $info = get_mp3info($file);
    printf "$file length is %d:%d\n", $info->{MM}, $info->{SS};
	dump($info);

}

sub main()
{
	my @fl = glob("*.mp3");
    LOOP:
	foreach my $ff (@fl) {
		get_info($ff);
		last LOOP;
	}
}

main;

