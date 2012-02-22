#!/usr/bin/perl
#
# continuous watching a folder to execute some instructions
# i.e. get files or something...
#

use strict;
use warnings;
use 5.010;
use File::ChangeNotify;
use Data::Dump qw(dump);

sub process_events($);
sub parse_content($);

sub process_events($)
{
    my $rar = shift;
    my @arr = @$rar;
    foreach my $evt (@arr)  {
        # only take care create event type
        if ($evt->type() eq "create")  {
            say $evt->path(), "\t", $evt->type();
            parse_content( $evt->path() );
        }
    }
}

sub parse_content($)
{
    my $file = shift;
    say $file;
    if ( -e $file && (-s $file > 0) )  {
        say "let's process $file!";
    }
}


sub main()
{
    my $watcher =
        File::ChangeNotify->instantiate_watcher
            ( directories => [ '/src/watch' ],
              filter      => qr/\.(?:txt)$/,
              sleep_interval => 5
            );

    #if ( my @events = $watcher->new_events() ) {
    #    print_events(\@events);
    #}

    # blocking
    while ( my @events = $watcher->wait_for_events() )  {
        process_events(\@events);
    }
}

main;
