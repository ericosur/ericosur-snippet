#!/usr/bin/perl
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 #   Author: Chris Harris
 #   Email for any feedback: clh8762@hotmail.com
 #   Title: TkTools
 #   Description: A collection network tools such as ping, finger, etc.
 #   Special thanks to Alan Ford, I used many of his excellent programs
 #   as starting points and in some cases I just plain copied his code.
 #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

require 5.002;
use Tk;
use Tk::NoteBook;
use Tk::Frame;
use Tk::Text;
use Tk::Label;
use Tk::Button;
use Tk::Entry;
use Tk::Scrollbar;
use Tk::Checkbutton;
use IO::Socket;
use Socket;
use English;
use Tk::DialogBox;
use Tk::Listbox;
sub finger ;
sub ping;
sub bind_message;
sub trace;
sub whoami;
sub whois;
sub netstat;
sub lookup ;
sub doubleclick ;
sub start;
sub ipcstart;
sub scan;
######################################################################

my $mw = MainWindow->new();
$mw->title("Network Tool Kit");
$mw->resizable(0,0);

my $nb = $mw->NoteBook(-ipadx => 6, -ipady => 6) ->pack(-side => 'top', -expand => '1',
     -fill => 'both');
######################################################################
my $page1 = $nb->add("page1", -label => "Ping");
my $lookup_frame = $page1->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');
$lookup_frame->Label(-text => "Address to Ping:")->pack(-side => 'left');
my $lookup_address = $lookup_frame->Entry(-width => '15', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_address, "Enter IP address for pinging a single host");

$lookup_frame->Label(-text => "To:")->pack(-side => 'left');
my $lookup_range = $lookup_frame->Entry(-width => '15', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_range, "Enter IP address for pinging a range of hosts");

my $exit = $lookup_frame->Button(-text => 'Exit', -width=> '15',
	-command => sub {
                                  exit;
                                });
$exit->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit, "Press to quit the application");

my $ping = $lookup_frame->Button(-text => 'Ping', - width=> '15',
	-command => sub {
									ping;
								});
$ping->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($ping, "Press to begin pinging specified host or range of hosts");


my $scroll = $page1->Scrollbar();
$scroll->pack(-side => 'right', -fill => 'y');
my $display = $page1->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll->configure(-command => ['yview', $display]);

$page1->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');

###################################################################

my $page2 = $nb->add("page2", -label => "Finger");
my $lookup_frame2 = $page2->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');

$lookup_frame2->Label(-text => "Address to Finger:")->pack(-side => 'left');
my $lookup_user2 = $lookup_frame2->Entry(-width => '15', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_user2, "Enter user name");

$lookup_frame2->Label(-text => "\@")->pack(-side => 'left');
my $lookup_host2 = $lookup_frame2->Entry(-width => '25', -relief => 'sunken')
->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_host2, "Enter host name");

my $long_value2 = '0';
my $long_output2 = $lookup_frame2->Checkbutton(-onvalue => '1', -offvalue => '0', -variable => \$long_value2, -text => 'Long Output')->pack(-side => 'left');

my $exit2 = $lookup_frame2->Button(-text => 'Exit',-width=>'15',
                                 -command => sub
                                 {
                                  exit;
                                 });
$exit2->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit2, "Press to quit the application");

my $finger = $lookup_frame2->Button(-text => 'Finger', -width=>'15',
                                   -command => sub
                                   {
                                    finger;
                                   });
$finger->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($finger, "Press to finger user");


my $scroll2 = $page2->Scrollbar();
$scroll2->pack(-side => 'right', -fill => 'y');
my $display2 = $page2->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll2])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll2->configure(-command => ['yview', $display2]);

$page2->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');

###################################################################

my $page3 = $nb->add("page3", -label => "Trace Route");
my $lookup_frame3 = $page3->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');
$lookup_frame3->Label(-text => "Address to Trace:")->pack(-side => 'left');
my $lookup_trace3 = $lookup_frame3->Entry(-width => '25', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_trace3, "Enter IP address or Host to trace");

my $exit3 = $lookup_frame3->Button(-text => 'Exit',-width=>'15',
                                 -command => sub
                                 {
                                  exit;
                                 });
$exit3->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit3, "Press to quit the application");

my $trace = $lookup_frame3->Button(-text => 'Trace',-width=>'15',
                                   -command => sub
                                   {
                                    trace;
                                    });
$trace->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($trace, "Press to begin tracing address or host");


my $scroll3 = $page3->Scrollbar();
$scroll3->pack(-side => 'right', -fill => 'y');
my $display3 = $page3->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll3])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll3->configure(-command => ['yview', $display3]);
tie(*STDOUT, 'Tk::Text', $display3);
$page3->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');
###################################################################
my $page4 = $nb->add("page4", -label => "WhoAmI");
my $lookup_frame4 = $page4->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');

my $exit4 = $lookup_frame4->Button(-text => 'Exit',-width=>'15',
                                 -command => sub
                                 {
                                  exit;
                                 });
$exit4->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit4, "Press to quit the application");

my $whoami = $lookup_frame4->Button(-text => 'Who Am I',-width=>'15',
                                   -command => sub
                                   {
                                    whoami;
                                    });
$whoami->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($whoami, "Press to find out who you are");

my $scroll4 = $page4->Scrollbar();
$scroll4->pack(-side => 'right', -fill => 'y');
my $display4 = $page4->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll4])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll4->configure(-command => ['yview', $display4]);
tie(*STDOUT, 'Tk::Text', $display4);

$page4->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');
##################################################################
my $page5 = $nb->add("page5", -label => "WhoIs");
my $default_server5 = "whois.networksolutions.com";

my $lookup_frame5 = $page5->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');
$lookup_frame5->Label(-text => "Whois Server:")->pack(-side => 'left');

my $lookup_server5 = $lookup_frame5->Entry(-width => '20', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_server5, "Enter the WhoIs server to use for lookup.");

$lookup_frame5->Label(-text => "Domain to Lookup:")->pack(-side => 'left');
my $lookup_host5 = $lookup_frame5->Entry(-width => '20', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_host5, "Enter the domain to lookup.");
$lookup_server5->insert('0', $default_server5);

my $exit5 = $lookup_frame5->Button(-text => 'Exit',-width=>'15',
                                 -command => sub
		                 {
		                  exit;
		                 });
$exit5->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit5, "Press to quit application");

my $whois = $lookup_frame5->Button(-text => 'Lookup Domain',-width=>'15',
                                  -command => sub
    		                  {
			           whois;
			          });
$whois->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($whois, "Press to begin lookup");

my $scroll5 = $page5->Scrollbar();
$scroll5->pack(-side => 'right', -fill => 'y');
my $display5 = $page5->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll5])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll5->configure(-command => ['yview', $display5]);
tie(*STDOUT, 'Tk::Text', $display5);

$page5->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');
##################################################################
my $page6 = $nb->add("page6", -label => "NetStat");
my $lookup_frame6 = $page6->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');

my $exit6 = $lookup_frame6->Button(-text => 'Exit',-width=>'15',
                                 -command => sub
                                 {
                                  exit;
                                 });
$exit6->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit6, "Press to quit the application");

my $netstat = $lookup_frame6->Button(-text => 'NetStat',-width=>'15',
                                   -command => sub
                                   {
                                    netstat;
                                    });
$netstat->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($netstat, "Press to view network statistics");


my $scroll6 = $page6->Scrollbar();
$scroll6->pack(-side => 'right', -fill => 'y');
my $display6 = $page6->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll6])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll6->configure(-command => ['yview', $display6]);
tie(*STDOUT, 'Tk::Text', $display6);

$page6->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');
##################################################################
my $page7 = $nb->add("page7", -label => "DNS Lookup");
my $lookup_frame7 = $page7->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');
$lookup_frame7->Label(-text => "Host to Lookup:")->pack(-side => 'left');
my $lookup_dns7 = $lookup_frame7->Entry(-width => '25', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_dns7, "Enter IP address or Host to lookup");

my $exit7 = $lookup_frame7->Button(-text => 'Exit',-width=>'15',-height=>'1',
                                 -command => sub
                                 {
                                  exit;
                                 });
$exit7->pack(-side => 'right', -expand => '0', -fill => 'x');
&bind_message($exit7, "Press to quit the application");

my $dns = $lookup_frame7->Button(-text => 'DNS Lookup',-width=>'15',-height=>'1',
                                   -command => sub
                                   {
                                    lookup;
                                    });
$dns->pack(-side => 'right', -expand => '0', -fill => 'x');
&bind_message($dns, "Press to begin resolving address or host");


my $scroll7 = $page7->Scrollbar();
$scroll7->pack(-side => 'right', -fill => 'y');

my $display7 = $page7->Listbox(
    -yscrollcommand => ['set', $scroll7],
    -relief => 'sunken',
	-background => 'white',
    -width => '85',
    -height => '20',
    -setgrid => 'yes',
);
$display7->pack(-side => 'top', -fill => 'both', -expand =>'0');
$scroll7->configure(-command => ['yview', $display7]);

$display7->bind('<Double-Button-1>' => sub {
   my($listbox7) = @ARG;
    foreach (split ' ', $listbox7->get('active')) {
        doubleclick $::ARG;
    }
});

$page7->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');
##################################################################

my $page8 = $nb->add("page8", -label => "NetBIOS");
my $lookup_frame8 = $page8->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');

$lookup_frame8->Label(-text => "Address:")->pack(-side => 'left');
my $lookup_address8= $lookup_frame8->Entry(-width => '15', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_address8, "Enter IP address for a single host");

$lookup_frame8->Label(-text => "To:")->pack(-side => 'left');
my $lookup_range8 = $lookup_frame8->Entry(-width => '15', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_range8, "Enter IP address for a range of hosts");

my $exit8 = $lookup_frame8->Button(-text => 'Exit',-width=> '15',
	 -command => sub
	 {
        exit;
	 });
$exit8->pack(-side => 'right', -expand => '', -fill => 'both');
&bind_message($exit8, "Press to quit the application");

my $start8 = $lookup_frame8->Button(-text => 'NetBIOS',-width=> '15',
	-command => sub
        {
        start;
        });
$start8->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($start8, "Press to begin targeting specified host or range of hosts");

my $scroll8 = $page8->Scrollbar();
$scroll8->pack(-side => 'right', -fill => 'y');
my $display8 = $page8->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll8])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll8->configure(-command => ['yview', $display8]);

$page8->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');

##################################################################
my $page9 = $nb->add("page9", -label => "IPConfig");
my $lookup_frame9 = $page9->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');

my $exit9 = $lookup_frame9->Button(-text => 'Exit',-width=> '15',
	 -command => sub
	 {
        exit;
	 });
$exit9->pack(-side => 'right', -expand => '', -fill => 'both');
&bind_message($exit9, "Press to quit the application");

my $start9 = $lookup_frame9->Button(-text => 'IpConfig',-width=> '15',
	-command => sub
        {
        ipcstart;
        });
$start9->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($start9, "Press to display IP information on local machine");

my $scroll9 = $page9->Scrollbar();
$scroll9->pack(-side => 'right', -fill => 'y');
my $display9 = $page9->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll9])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll9->configure(-command => ['yview', $display9]);

$page9->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');

##################################################################
my $page10 = $nb->add("page10", -label => "Port Scanner");
my $lookup_frame10 = $page10->Frame()->pack(-expand => '1', -fill => 'both', -side => 'top');
$lookup_frame10->Label(-text => "Address to Scan:")->pack(-side => 'left');
my $lookup_scan10 = $lookup_frame10->Entry(-width => '25', -relief => 'sunken')
    ->pack(-side => 'left', -expand => '0', -fill => 'x');
&bind_message($lookup_scan10, "Enter IP address or Host to scan");

$lookup_frame10->Label(-text => "Port:")->pack(-side => 'left');
my $lookup_port10 = $lookup_frame10->Entry(-width => '11', -relief => 'sunken')
  ->pack(-side => 'left', -expand => '0', -fill => 'x');
  &bind_message($lookup_port10, "Enter port to scan");

$lookup_frame10->Label(-text => "To:")->pack(-side => 'left');
my $lookup_portrange10 = $lookup_frame10->Entry(-width => '11', -relief => 'sunken')
  ->pack(-side => 'left', -expand => '0', -fill => 'x');
  &bind_message($lookup_portrange10, "Enter port range to scan");

my $exit10 = $lookup_frame10->Button(-text => 'Exit',-width=>'15',
                                 -command => sub
                                 {
                                  exit;
                                 });
$exit10->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($exit10, "Press to quit the application");

my $scan = $lookup_frame10->Button(-text => 'Scan',-width=>'15',
                                   -command => sub
                                   {
                                    scan;
                                    });
$scan->pack(-side => 'right', -expand => '0', -fill => 'both');
&bind_message($scan, "Press to begin scanning for open ports.");


my $scroll10 = $page10->Scrollbar();
$scroll10->pack(-side => 'right', -fill => 'y');
my $display10 = $page10->Text(-height => '25', -width => '85', -yscrollcommand => ['set', $scroll10])
    ->pack(-side => 'top', -expand => '1', -fill => 'both');
$scroll10->configure(-command => ['yview', $display10]);
tie(*STDOUT, 'Tk::Text', $display10);
$page10->Label(-textvariable => \$message)
   ->pack(-side => 'bottom',-expand => '1', -fill => 'x');
###################################################################
sub ping {
  $display->delete('1.0', 'end');
  $display->idletasks;

  my $address = $lookup_address -> get;
  my $range = $lookup_range -> get;

  if ($range == ' ' ) {
      $message = "Pinging $address";
      open(NET, "ping $address |")    || die "cannot fork: $!";
      $| = 1;
      while ($_ = <NET>) {
	      $display-> yview('end');
	      $display->idletasks;
		  $mw->update;
          $_ =~ s/\r$//;
		  $display -> insert('end',$_);
		   }
      close(NET)                      || die "can't close ping: $!";
   }

  else {
      ($add_1, $add_2, $add_3, $add_4) = split(/\./, $address, 4);
      ($range_1, $range_2, $range_3, $range_4) = split(/\./, $range, 4);
      while ($add_4 <= $range_4) {
           my $host = "$add_1"."."."$add_2"."."."$add_3"."."."$add_4";
           $message = "Pinging $host";
           open(NET, "ping $host |")    || die "cannot fork: $!";
           $| = 1;
               while ($_ = <NET>) {
			       $display-> yview('end');
	               $display->idletasks;
				   $mw->update;
                   $_ =~ s/\r$//;
		           $display -> insert('end',$_);
		           }
	        close(NET)                      || die "can't close ping: $!";
            $add_4++;
	   }
   }
}
##################################################################
sub bind_message {
  my ($widget, $msg) = @_;
  $widget->bind('<Enter>', [ sub { $message = $_[1]; }, $msg ]);
  $widget->bind('<Leave>', sub { $message = "Network Tool Kit Copyright(c) Chris Harris 2001"; });
}
###################################################################
sub finger {
$display2->delete('1.0', 'end');
$display2->idletasks;
$display2-> yview('end');

my $host2 = $lookup_host2->get;
if ($host2 eq "") {
    $host2 = "localhost";
    $lookup_host2->insert('0', "localhost");
}
my $user2 = $lookup_user2->get;
my $msg;

my $remote2 = IO::Socket::INET->new(
               Proto    => "tcp",
               PeerAddr => $host2,
               PeerPort => "finger(79)",
              );

unless ($remote2) {
    $msg = "Cannot connect to $host2\n";
    $display2->insert('end', $msg);
    next;
}

$remote2->autoflush(1);

# use CRLF network line terminators
if ($long_value2 == 1) {
    $display2->idletasks;
	$mw->update;
    print $remote2 "/W $user2\015\012";
} else {
    print $remote2 "$user2\015\012";
}
while ($_ = <$remote2>) {
    $display2->idletasks;
	$mw->update;
    $_ =~ s/\r$//;  # trim annoying \r line-endings on some finger output
    $display2->insert('end', $_);

}
close($remote2)  or sub {
    $display2->idletasks;
	$mw->update;
    $msg = "Can't close socket: $!\n";
    $display2->insert('end', $msg);
    };
}
##################################################################
sub trace {
  my $trace_address = $lookup_trace3 -> get;
  $message = "Tracing  $trace_address";
  $display3->delete('1.0', 'end');
   open(NET, "tracert $trace_address |")    || die "cannot fork: $!";
      $| = 1;
      while ($_ = <NET>) {
	      $display3->idletasks;
		  $mw->update;
          $_ =~ s/\r$//;
		  $display3 -> insert('end',$_);
		  $display3-> yview('end');
		   }
      close(NET)                      || die "can't close tracert: $!";
}
##################################################################
sub whois {
$display5->delete('1.0', 'end');
$mw -> idletasks;
my $host5 = $lookup_host5->get;
my $server5 = $lookup_server5->get;
if ($server5 eq "") {
    $server5 = $default_server5;
    $lookup_server5->insert('0', $default_server5);
}
my $msg;

my $remote5 = IO::Socket::INET->new(
    	       Proto    => "tcp",
    	       PeerAddr => $server5,
    	       PeerPort => "whois(43)",
      	      );

unless ($remote5) {
    $msg = "Cannot connect to $server5\n";
    $display5->insert('end', $msg);
    next;
}

$remote5->autoflush(1);

# use CRLF network line terminators
print $remote5 "$host5\015\012";

while ($_ = <$remote5>) {
    $mw->update;
    #print;
    $_ =~ s/\r$//;  # trim annoying \r line-endings on some output
    $display5->insert('end', $_);
	$display5-> yview('end');
}
close($remote5)	or sub {
    $msg = "Can't close socket: $!\n";
    $display5->insert('end', $msg);
    };
}

##################################################################
sub whoami {
$display4->delete('1.0', 'end');
$msg = "\n\nCurrently logged on as:\n";
$display4 ->insert('end', $msg);
$msg =  "----------------------\n";
$display4 ->insert('end', $msg);
$msg =  "Domain:  ";
$display4 ->insert('end', $msg);
$msg =  Win32::DomainName()."\n";
$display4 ->insert('end', $msg);
$msg =  "Computer: ";
$display4 ->insert('end', $msg);
$msg =  Win32::NodeName()."\n";
$display4 ->insert('end', $msg);
$msg =  "Userid:  ";
$display4 ->insert('end', $msg);
$msg =  Win32::LoginName()."\n\n";
$display4 ->insert('end', $msg);
}
##################################################################
sub netstat {
  $message = "Gathering data.....";
  $display6->delete('1.0', 'end');
  $mw->idletasks;
  open(NET, "netstat -n -a -se -r |")    || die "cannot fork: $!";
      $| = 1;
      while ($_ = <NET>) {
	      $display6->idletasks;
		  $mw->update;
          $_ =~ s/\r$//;
		  $display6-> insert('end',$_);
		  $display6-> yview('end');
		  }
   close(NET)                      || die "can't close netstat: $!";
}
##################################################################
sub lookup {
    # Do the Lookup
    my $host7 = $lookup_dns7->get;
	$message = "Resolving $host7.";
    if ($host7 =~ /^[01-9.]+$/) {
        my $addresses7 = gethostbyaddr(inet_aton($host7), AF_INET) or
		    $addresses7 = "Can't resolve $host7: $!";
			$mw->idletasks;
			$mw->update;
            $display10-> yview('end');
	        $display7->delete('0', 'end');
	        $display7->insert('end', $addresses7);
    }
    else {
        my @addresses7 = gethostbyname($host7) or @addresses7 = ("Can't resolve $host7: $!");
	        @addresses7 = map { inet_ntoa($_) } @addresses7[4 .. $#addresses7];
	        $mw->idletasks;
			$mw->update;
	        $display7->delete('0', 'end');
	        $display7->insert('end', @addresses7);
		    $display7-> yview('end');
    }
}
#########################################################################
sub doubleclick {
   # Get and display gethostbyaddr if an IP address

   my($host7) = @ARG;
   if ($host7 =~ /^[01-9.]+$/) {
       my $addresses7 = gethostbyaddr(inet_aton($host7), AF_INET) or $addresses7 = "Can't resolve $host7: $!";
       my $dialogbox7 = $page7->DialogBox( -title   => "DNS Lookup",
                                     -buttons => [ "OK" ]);
       $dialogbox7->add("Label", -text => "$host7 is $addresses7")->pack;
       $dialogbox7->Show;
   }
}
###################################################################
sub start {
  $display8->delete('1.0', 'end');
  $display8->idletasks;

  my $address8= $lookup_address8 -> get;
  my $range8 = $lookup_range8 -> get;

  if ($range8 == ' ' ) {
      $message = "Targeting $address8";
      my @results8 = `nbtstat -A $address8`;
	  $display8->insert('end', "Results from $address8:");
      foreach $result8(@results8) {
		  $display8->idletasks;
		  $result8 =~ s/\r$//;
		  $display8 -> insert('end', $result8);
		  $display9-> yview('end');
	  }
   }

  else {
      ($add_1, $add_2, $add_3, $add_4) = split(/\./, $address8, 4);
      ($range_1, $range_2, $range_3, $range_4) = split(/\./, $range8, 4);
      while ($add_4 <= $range_4) {
          my $host8 = "$add_1"."."."$add_2"."."."$add_3"."."."$add_4";
           $message = "Targeting $host8";
          my @results8 = `nbtstat -A $host8`;
		  $display8->insert('end', "Results from $host8:");
          foreach $result8 (@results8) {
		  $display8->idletasks;
		  $mw->update;
		  $result8 =~ s/\r$//;
		  $display8 -> insert('end', $result8);
		  }
          $add_4++;
		  $display8 -> insert('end', "\n"."\n");
		  $display8-> yview('end');
      }
  }
}
###################################################################
sub ipcstart {
  $message = "Gathering data.....";
  $display9->delete('1.0', 'end');
  $mw->idletasks;
my @ipconfig_back = `ipconfig /all`;
     foreach $ipconfig_back(@ipconfig_back) {
	      $display9-> yview('end');
          $display9 -> idletasks;
          $ipconfig_back =~ s/\r$//;
          $display9->insert('end', $ipconfig_back);
      }
}
##################################################################
sub scan {
$display10->delete('1.0', 'end');
my $port10 = $lookup_port10->get;
my $portrange10 = $lookup_portrange10 -> get;
my $host10 = $lookup_scan10->get;
while ($port10 <= $portrange10) {
    $message = "Scanning port:$port10";
	$display10 ->idletasks;
	$mw->update;
	$display10-> yview('end');
	my $serv10;
    $serv10 = getservbyport $port10, "tcp";
	my $service;
	if($serv10 eq "") {
	    $service = "";
	}
	else{
	    $service = "($serv10)";
	}
    my $remote10 = IO::Socket::INET->new(
    	       Proto    => "tcp",
    	       PeerAddr => $host10,
    	       PeerPort => $port10,
			   );
    unless ($remote10) {
        #~ $msg = "Port:$port10$service is closed.\n";
        #~ $display10->insert('end', $msg);
    }
	else {
	    $msg = "Port:$port10$service is open.\n";
        $display10->insert('end', $msg);
	}
    close $remote10;
	$port10 ++;

  }
}
###################################################################
MainLoop;
