#!/usr/bin/perl
# apt-get install libjson-perl
# http://search.cpan.org/dist/JSON/

use strict;

# use JSON qw/to_json from_json/;
use JSON;
use Data::Dumper;

sub main()
{
    my $json_text = '{"text":"hello,world"}';
    print Dumper from_json($json_text);

    my $hash = from_json($json_text);
    print $hash->{'text'} . "\n";
}


main();
