my $debug = 0;


sub get_config
{
    print "get_config: $ini\n" if $debug;
    open my $fh, $ini or die;
    while ( <$fh> )  {
            next if /^$/;
            next if /^#/;
            s/\n//;
            eval($_);
            print "get_config: $_\n" if $debug;
    }
    close $fh;
}
