#!/usr/bin/env perl
#

# listarr.pl will ack setting.json as config,
# read "ifile" and output to "ofile"

use strict;
use Storable;
use utf8;
use JSON;

sub read_config($)
{
    my $jsonf = shift;
    my $json_text;

    open my $fh, $jsonf or die;
    while (<$fh>) {
        $json_text = $json_text . $_;
    }
    close($fh);
    #print $jsontext;

    my $hash = from_json($json_text);
    my $datafile = $hash->{'common'}->{'datafile'};
    my $ofile = $hash->{'listarr.pl'}->{'ofile'};
    my $repeat = $hash->{'listarr.pl'}->{'repeat'};

    printf("read_config:\ndatafile:%s\nofile:%s\nrepeat:%d\n", $datafile, $ofile, $repeat);

    return ($datafile, $ofile, $repeat);
}

sub process($$$)
{
    my $datafile = shift;
    my $ofile = shift;
    my $repeat = shift;

    my $ref = retrieve($datafile);

    binmode(STDOUT, ":encoding(utf8)");

    my @arr = @$ref;
    my $arrsize = scalar(@arr);

    printf("size of array: %d\n", $arrsize);

    printf("will output to %s\n", $ofile);
    open my $ofh, "> $ofile" or die;
    binmode($ofh, ":encoding(utf8)");

    print $ofh <<EOL;
{
    "array": [
EOL

    my @outarr = ();
    for (my $i=0; $i<$repeat; ++$i) {
        my $idx = int(rand($arrsize));
        #printf("%d: %s\n", $idx, $arr[$idx]);
        my $line = sprintf("\t\"%s\"", $arr[$idx]);
        print $ofh $line;
        if ($i != $repeat - 1) {
            print $ofh ",";
        }
        print $ofh "\n";
    }

    print $ofh <<EOL;
    ]
}
EOL

}

sub main()
{
    my ($datafile, $ofile, $repeat) = read_config('setting.json');
    process($datafile, $ofile, $repeat);
}

main;
