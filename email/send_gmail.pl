#!/usr/bin/perl

# http://www.nixtutor.com/linux/sending-mail-through-gmail-with-perl/

# tested on 2010/11/09 ok

use strict;
use warnings;

use Net::SMTP::TLS;
my $mailer = new Net::SMTP::TLS(
    'smtp.gmail.com',
    Hello   =>      'smtp.gmail.com',
    Port    =>      587,
    User    =>      'rasmus.lai@gmail.com',
    Password=>      'jjezGoo1108');
$mailer->mail('rasmus.lai@gmail.com');
$mailer->to('ericosur@gmail.com');
$mailer->data;
$mailer->datasend("Sent from perl!");
$mailer->dataend;
$mailer->quit;
