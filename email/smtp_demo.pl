#!/usr/bin/perl
#
# simple demo for SMTP via perl script
#

#
# YOU NEED TO CONFIGURE THIS SCRIPT WITH SERVER NAME/USER NAME/PASSWORD
#

use strict;
use warnings;

use Net::SMTP;

# SMTP host
my $mailhost = "mail.mailer.com";

# mail from email address
my $mailfrom = q(fromthisuser@gmail.com);

# recipient list
my @mailto = (q(nosuchuser@gmail.com));

my $subject = "Greetings from perl script from rasmus";

my $text=<<EOL;
This is a test perl script to send email via
Net::SMTP
EOL

my $smtp = Net::SMTP->new($mailhost,
						Hello => 'localhost',
						Timeout => 30,
						Debug => 1);

#
# note here the password is needed
#
$smtp->auth('rasmus lai', 'password here');

foreach my $mt (@mailto)
{
	# send the from and recipient one by one
	$smtp->mail($mailfrom);
	$smtp->to($mt);

	# start the mail
	$smtp->data();

	# send the header
	$smtp->datasend("To: $mt\n");
	$smtp->datasend("From: $mailfrom\n");
	$smtp->datasend("Subject: $subject\n");
	$smtp->datasend("\n");

	# send the message
	$smtp->datasend("$text\n\n");

	# send the termination string
	$smtp->dataend();
}

$smtp->quit;
