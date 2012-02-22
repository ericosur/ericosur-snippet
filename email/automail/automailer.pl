#!/usr/bin/perl
#
# simple demo for SMTP via perl script
#

#
# YOU NEED TO CONFIGURE THIS SCRIPT WITH SERVER NAME/USER NAME/PASSWORD
# default using 'mail.conf'
#
# note: RFC2822 (Internet Message Format) is not the same thing as
# RFC2821 (SMTP). The prior describes the format of email,
# the later describes how to transfer the email.
#

use strict;
use warnings;

use Net::SMTP;
use MIME::Lite;		# to compose mail messaage body
use MIME::Types;
use MIME::Base64;
use Encode qw(from_to encode decode);
use Getopt::Std;

my $user;	# smtp auth user name
my $pass;	# smtp auth user password
my $host;	# SMTP host
my $from;	# mail from email address
my $port;	# not used here, only for compatible to get_config()

my $debug;	# debug mode on/off
my $verbose;	# more debug info
my $attach;		# one specified attach file
my $bodyfile;	# file to store mail body content
my %opts = ();	# options from command line

my $ini = 'mail.conf';
my $recp_ini = 'recp.conf';

# recipient list
my @mailto = ();

# get config data from ''$ini''
sub get_config
{
	print "get_config: $ini\n" if $debug;
	open my $fh, $ini or die;
	while ( <$fh> )  {
		next if /^$/;
		next if /^#/;
		s/\n//;
		eval($_);
		print "get_config: $_\n" if $debug && $verbose;
	}
	close $fh;
}

# get config data from $recp_ini
sub get_recp
{
	print "get_recp: $recp_ini\n" if $debug;
	open my $fh, $recp_ini or die;
	while (<$fh>)  {
		next if /^$/;
		next if /^#/;
		s/\n//;
		print "get_recp: $_\n" if $debug;
		push @mailto, $_;
	}
	close $fh;
}



sub send_email()
{
	my $to_list = join(', ', @mailto);
	my $mailbody;

	if ($attach)  {
		print "using email_body_attach()\n" if $debug;
		$mailbody = email_body_attach($from, $to_list, $attach);
	}
	else  {
		print "using compose_mime_body()\n" if $debug;
		$mailbody = compose_mime_body($from, $to_list);
	}

	#return;	# hack

	my $smtp = Net::SMTP->new($host,
							Hello => 'localhost',
							Timeout => 30,
							Debug => $debug);
	#
	# note here the password is needed
	#
	#$smtp->auth($user, $pass);

	foreach my $mt (@mailto)  {
		print "mailto => $mt\n" if $debug;

		# send the from and recipient one by one
		$smtp->mail($from);
		#$smtp->to($mt);
		$smtp->bcc($mt);

		# start the mail
		$smtp->data();

		# send the header
		$smtp->datasend($mailbody);

		printf "send a mail to (%s)\n", $mt if $debug;

		# send the termination string
		$smtp->dataend();
	}

	$smtp->quit;
}



sub shink_subject($)
{
	my $subj = shift;
	my $max = 60;

	if (length($subj) > $max)  {
		substr($subj, $max, length($subj)-1) = "...";
	}

	return $subj;
}


sub load_attach($)
{
	my $rcontent = shift;

	open FH, "attach.txt" or return;
	undef $/;
	$$rcontent = <FH>;
	close FH;

#	return $$content;
}


sub get_body_content()
{
	if (not -e $bodyfile)  {
		die "cannot load mail body file\n";
	}

	my $msg;
	open my $fh, $bodyfile or die;
	local $/ = undef;
   	$msg = <$fh>;

	# trnascode from big5 to utf8
	from_to($msg, "BIG5", "UTF8");

	return $msg;
}

sub test_encoding($)
{
	my $str = shift;
	my $b64;

	$b64 = encode_base64($str);
	$b64 =~ s/[\r\n]//;

	my $ostr = sprintf "=?UTF8?B?%s?=", $b64;

	return $ostr;

}


#
# [in] from address
# [in] to address
#
sub compose_mime_body($$)
{
	my ($from, $to) = @_;

	# to fetch infomation first, for subject and mail body
	#my $mail_body = twoday();
	my $mail_body = get_body_content();
	my $subject;

	if ( $mail_body =~ m/^subject: (.*)/i )  {
		$subject = $1;
	}

	$mail_body =~ s/^subject:.*//i;

	print "subject => $subject\n" if $debug;

	my $test_hdr;
	$test_hdr = test_encoding($subject);
	print "test_hdr => $test_hdr\n" if $debug;

	# MIME::Lite object
	my $msg = MIME::Lite->new(
		From	=> $from,
		#To		=> $to,
		#Cc		=> q(),
		Bcc => $to,
	 	Subject => $subject,
	 	#Subject => $test_hdr,
	 	Type	=> q(multipart/mixed),
	);


	# add a customized tag
	$msg->add('X-Camel-Comment' => 'powered by perl');
	$msg->add('X-Author-Comment' => 'script by ericosur');

	# attach the text content
	my $textpart = MIME::Lite->new(
		Type => 'text/plain',
		#Data => get_lorem_text(),
		Data => $mail_body,
		Encoding => 'base64',
	);

	$textpart->attr("content-type.charset" => "UTF-8");
	#$textpart->attr("content-type.charset" => "BIG5");
	$msg->attach($textpart);

=pod
	my @fext = qw(png gif jpg);
	my %ftype = (
		png => 'image/png',
		gif => 'image/gif',
		jpg => 'image/jpeg'
	);
=cut

	my $str = $msg->as_string;
	print $str if $debug && $verbose;
	return $str;
}



sub help
{
	print<<EOL;
***** help message *****
<h>elp	this message
<n>umber	repeat times
<d>debug	debug info
<v>erbose	verbose, lots lots of info
<a>ttach	specify attach filename
<f>ile	mail body content
EOL
}



sub print_option
{
	for my $kk (keys %opts)  {
		print "opts{$kk} -> $opts{$kk}\n";
	}
}


#
# [in] from address
# [in] to address
#
sub email_body_attach($$$)
{
	my ($from, $to, $ifile) = @_;
	my ($tmp, $subject) = ( $ifile, $ifile );

	print "ifile = $ifile\n";
	if (not -e $ifile)  {
		die "cannot found $ifile\n";
	}

	print "subject => $subject\n" if 1;#$debug;

	# MIME::Lite object
	my $msg = MIME::Lite->new(
		From	=> $from,
		#To		=> $to,
		#Cc		=> q(),
		Bcc		=> $to,
	 	Subject => $subject,
	 	Type	=> q(multipart/mixed),
	);

	# add a customized tag
	#$msg->add('X-Camel-Comment' => 'powered by perl');

	# attach the text content
	my $textpart = MIME::Lite->new(
		Type => 'text/plain',
		Data => $ifile,
		Encoding => 'base64',
	);

	$textpart->attr("content-type.charset" => "UTF-8");
	$msg->attach($textpart);

	my $mimetypes = MIME::Types->new;
	my $mtype = $mimetypes->mimeTypeOf($ifile);
	$mtype = 'application/octet-stream' if (not $mtype);
	print "mime type is: ", $mtype, "\n";

	### attach one specified file
	$msg->attach (
	   Type => $mtype,
	   Path => $ifile,
	   Filename => $tmp,
	   Disposition => 'attachment',
	   Encoding => 'base64'
	) or die "Error while attaching: $!\n";

	return $msg->as_string;
}


# compose date/time string for subject
sub get_date()
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d/%02d %02d:%02d", $mon + 1, $mday, $hour, $min;
	#print "$date\n";
	return $date;
}


sub write_log
{
	my $file = "automail.log";
	my $date = get_date();

	open my $fh, ">>", $file or die;
	print $fh $date, " send mail\n";
	close $fh;
}


#
# main procedure start here
#
sub main
{
	# d: debug, h: help, n: repeat times
	my $optcmd = 'dhva:f:';

	getopts($optcmd, \%opts);

	if ($opts{h})  {
		help();
		exit 1;
	}

	$debug = $opts{d} || 0;
	$verbose = $opts{v} || 0;
	$attach = $opts{a} if $opts{a};
	$bodyfile = $opts{f} if $opts{f};

	print_option() if $debug;

	get_config();
	get_recp();

	send_email();
	write_log();
}


main;

