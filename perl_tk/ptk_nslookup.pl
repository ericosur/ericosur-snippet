#!/usr/bin/perl -w
# ptknslookup version 0.1     for Perl/Tk
# By Alan Ford <alan@whirlnet.demon.co.uk>  07/04/1999
#
# Description:
# Perl/Tk App to provide DNS Lookups
#
# Distributed with no warranty under the GNU Public License

require 5.003;
use English;
use Tk;
use Tk::DialogBox;
use Socket;
#use Net::DNS;
#use Net::Ping;
my $ping_available = 0;
## try loading the module, but don't blow up if missing
#eval {
#    require Net::Ping;
#    $ping_available = 1;
#};
my $fetch_mx = 0;
# try loading the module, but don't blow up if missing
eval {
    require Net::DNS;
    Net::DNS->import('mx');
    $fetch_mx = 1;
};
            
sub lookup ;
sub doubleclick ;
sub lookupmx ;
sub pinghost ;

my $MW = MainWindow->new;

# NOT IMPLEMENTED DUE TO A BUG CREATED WHEN ENTRY BOX IS CLICKED ON
## set up a warning handler that displays the warning in a Tk dialog box
#BEGIN {
#    $SIG{__WARN__} = sub {
#        if (defined $MW) {
#           my $warnbox = $MW->DialogBox( -title   => "Warning",
#                                         -buttons => [ "Acknowledge" ]);
#           $warnbox->add("Label", -text => $_[0])->pack;
#           $warnbox->Show;
#       } else {
#           print STDOUT join("\n", @_), "n";
#       }
#   };
#}

$MW->title("Perl/Tk DNS Lookup");
$MW->Label(-text => "Version 0.1 - Written by Alan Ford\n<alan\@whirlnet.demon.co.uk>")->pack(-side => 'bottom');

my $exit = $MW->Button(-text => 'Exit',
                       -command => sub
                       {
                        exit;
                       });
$exit->pack(-side => 'bottom', -expand => '1', -fill => 'both');

my $mxlookup = $MW->Button(-text => 'Lookup MX',
                           -command => sub
                           {
                            lookupmx;
                           });
$mxlookup->pack(-side => 'bottom', -expand => '1', -fill => 'both');

my $lookup = $MW->Button(-text => 'Lookup',
                          -command => sub
                          {
                           lookup;
                          });
$lookup->pack(-side => 'bottom', -expand => '1', -fill => 'both');

my $lookup_frame = $MW->Frame()->pack(-expand => '1', -fill => 'both', -side
=> 'top');

$lookup_frame->Label(-text => "Thing to Lookup:")->pack(-side => 'left');
my $lookup_value = $lookup_frame->Entry(-width => '15', -relief => 'sunken')->pack(-side => 'right');

my $scroll = $MW->Scrollbar();
$scroll->pack(-side => 'right', -fill => 'y');
my $list = $MW->Listbox(
    -yscrollcommand => ['set', $scroll],
    -relief => 'sunken',
    -width => 20,
    -height => 4,
    -setgrid => 'yes',
);
$list->pack(-side => 'left', -fill => 'both', -expand => 'yes');
$scroll->configure(-command => ['yview', $list]);
$MW->minsize(1, 1);

$list->bind('all', '<Control-c>' => \&exit);
$list->bind('<Double-Button-1>' => sub {
    my($listbox) = @ARG;
    foreach (split ' ', $listbox->get('active')) {
        doubleclick $::ARG;
    }
});
                    

MainLoop;

sub lookup {
    # Do the Lookup
    my $host = $lookup_value->get;
    if ($host =~ /^[01-9.]+$/) {
        my $addresses = gethostbyaddr(inet_aton($host), AF_INET) or $addresses = "Can't resolve $host: $!";
        $list->delete('0', 'end');
        $list->insert('end', $addresses);
    }
    else {
        my @addresses = gethostbyname($host) or @addresses = ("Can't resolve $host: $!");
        @addresses = map { inet_ntoa($_) } @addresses[4 .. $#addresses];
        $list->delete('0', 'end');
        $list->insert('end', @addresses);
    }
}

sub doubleclick {
   # Get and display gethostbyaddr if an IP address

   my($host) = @ARG;
   if ($host =~ /^[01-9.]+$/) {
       my $addresses = gethostbyaddr(inet_aton($host), AF_INET) or $addresses = "Can't resolve $host: $!";
       my $dialogbox = $MW->DialogBox( -title   => "DNS Lookup",
                                     -buttons => [ "OK" ]);
       $dialogbox->add("Label", -text => "$host is $addresses")->pack;
       $dialogbox->Show;
   }
}

sub lookupmx {
    # Lookup MX records for host and display in listbox
    
    if ($fetch_mx == 1) {
        my $host = $lookup_value->get;
        my $res = Net::DNS::Resolver->new();
        my @mx = mx($res, $host)
           or die @mx = ("Can't find MX records for $host (".$res->errorstring,")");
        $list->delete('0', 'end');
        foreach $record (@mx) {
            my $preference = $record->preference;
            my $exchange = $record->exchange;
            $list->insert('end', "$preference $exchange");
        }
    }
    else {
        my $dialogbox = $MW->DialogBox( -title   => "MX Lookup",
                                      -buttons => [ "OK" ]);
        $dialogbox->add("Label", -text => "The Net::DNS Module (available from CPAN) is not present, so this feature is unavailable.")->pack;
        $dialogbox->Show;
    }
}

sub pinghost {
    # THIS FEATURE REMOVED AS IT SERVES LITTLE PURPOSE - ALMOST NO HOSTS LIKE
    # TCP ECHO PACKETS. CODE LEFT FOR HISTORICAL PURPOSES. MODULE LINES #'ed
    
    # Ping Host using Net::Ping module to check if it is alive.
    if ($fetch_mx == 1) {
        my $host = $lookup_value->get;
        my $proto = ( $> ? "tcp" : "icmp" );
        my $pong = Net::Ping->new($proto);
        (defined $pong) or $msg = "Couldn't create Net::Ping object: $!";
        if ($pong->ping($host)) {
            $msg = "$host responded to $proto echo ping packets";
        } else {
            $msg = "$host did not respond to $proto echo ping packets";
        }
        my $dialogbox = $MW->DialogBox( -title   => "Ping Host",
                                        -buttons => [ "OK" ]);
        $dialogbox->add("Label", -text => $msg)->pack;
        $dialogbox->Show;
    } else {
        my $dialogbox = $MW->DialogBox( -title   => "Ping Host",
                                        -buttons => [ "OK" ]);
        $dialogbox->add("Label", -text => "The Net::Ping Module (available from CPAN) is not present, so this feature is unavailable.")->pack;
        $dialogbox->Show;
    }
}
