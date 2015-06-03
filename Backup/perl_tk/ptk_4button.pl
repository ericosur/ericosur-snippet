#!/usr/bin/perl -w

#
# small perl/tk demo
# 2006/12/27 by ericosur
#

use strict;
use warnings;

use Tk;

my $mw = MainWindow->new;

my $btn1 = $mw->Button(-text => 'Done1', -command => sub { exit });
my $btn2 = $mw->Button(-text => 'Done2', -command => sub { exit });
my $btn3 = $mw->Button(-text => 'Done3', -command => sub { exit });

$btn1->pack(-side => 'left', -padx => '10m', -pady => '1c');
$btn2->pack(-side => 'left', -ipadx => 20, -padx => 10);
$btn3->pack(-side => 'left', -ipadx => 30);

# assign to an array
my @list1 = $btn1->packInfo();
for my $str (@list1)
{
	print $str . "\t";
}

print "\n" . "-" x 78 . "\n";

# assign to a hash
my %list2 = $btn2->packInfo();
my $key = '-ipadx';
printf "btn2: %s => %d\n", $key, $list2{$key};

MainLoop;
