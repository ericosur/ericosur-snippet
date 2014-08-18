#!/usr/bin/perl
#
# problematic while sending multipart mime to gmail
#


use strict;
use warnings;

use Net::SMTP::TLS;
use Config::Simple;
use MIME::Lite;

# global settings
my $config_file = "gmail.ini";
my ($smtp, $user, $password);
my $recp;
my @tmpix = ();
my $msg;

sub get_config($)
{
	my $ini = shift;
	die "cannot load $ini file\n" if (not -e $ini);

	my %conf = ();
	Config::Simple->import_from($ini, \%conf);

	$smtp = $conf{'gmail.smtp'} or warn "smtp not found";
	$user = $conf{'gmail.user'} or warn "user not found";
	$password = $conf{'gmail.password'} or warn "password not found";
	$recp = $user;
}

sub send_gmail
{
	my $subject = 'test subject';

    my $mailer = new Net::SMTP::TLS(
        $smtp,
        Hello   => $smtp,
#		Port    =>      465, # redundant
        User    => $user,
        Password=> $password,
    );

	compose_mime_body($user, $recp);

#	print $$msg->as_string;

	print "send mail to $recp\n";

	$mailer->mail($user);
	$mailer->to($recp);
	$mailer->data;
	$mailer->datasend($msg->as_string);
	$mailer->dataend;
	$mailer->quit;

    undef $mailer;
}


sub get_subject
{
	# compose date/time string for subject
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d%02d%02d%02d", $mon + 1, $mday, $hour, $min;
	return $date;
}

sub get_text
{
=pod
	my $str;
	my $cmd = q(cmd /c D:/Tool/SysinternalsSuite/pslist.exe 2> nul);

	$str = `$cmd`;
	return $str;
=cut
use Text::Lorem;

	my $text = Text::Lorem->new();
	# Generate paragraphs
	my $paragraph = $text->paragraphs(1);

	undef $text;
	return $paragraph;
}

#
# [in] from address
# [in] to address
#
sub compose_mime_body($$)
{
	my ($from, $to) = @_;
	my $debug = 0;

	# MIME::Lite object
	$msg = MIME::Lite->new(
		From	=> $from,
		To		=> $to,
#		Cc		=> q(),
#	 	Subject => get_subject_zh(),
	 	Subject => get_subject(),
#	 	Type	=> q(multipart/mixed),
#	 	Type	=> q(multipart/related),
	);

	# add a customized tag
#	$msg->add('X-Camel-Comment' => 'Powered by perl, MIME-Lite, Net-SMTP');

	# attach the text content
#	my $textpart = MIME::Lite->new(
=pod
	$msg->attach(
		Type => 'text/plain',
		Data => get_text(),
		Encoding => '7bit',
	);
	$msg->attr("content-type.charset" => "UTF-8");
#	$msg->attach($textpart);
=cut

	$msg->attach(
		Type => "image/jpeg",
		Path => 'img001.jpg',
		Id => 'img001.jpg',
#		Filename => $fn,
		Disposition => "attachment",
		Encoding => 'base64',
		ReadNow => 1
	);

=pod
	$msg->attach(
		Type => "image/jpeg",
		Path => 'img002.jpg',
		Id => 'img002.jpg',
#		Filename => $fn,
		Disposition => "attachment",
		Encoding => 'base64',
	);
=cut

#	$msg->as_string;
#	print $msg->as_string if 1;
#	return \$msg;		# return the reference of $msg
}

sub remove_tmp_pix
{
	foreach my $fn (@tmpix)  {
		unlink $fn;
	}
}

sub gen_images
{
 	# generate images
 	require "randpix.pm";
	for my $ii (1..2)  {
		my $fn = sprintf("img%03d.jpg", $ii);
		print $fn, "\n";
		pixutil::draw($fn);
		if (not -e $fn)  {
			print "$fn not found\n";
			next;
		}
		push @tmpix, $fn;
	}
}

sub main
{
	get_config($config_file);

#	my $msg = compose_mime_body($user, $recp);
#	print $$msg->as_string;

#	gen_images;

	send_gmail;

#	remove_tmp_pix;
}

main;
