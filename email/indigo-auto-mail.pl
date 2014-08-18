#!/usr/bin/perl
#
# simple demo for SMTP via perl script
#
# this script would automatically generate lorem text and
# two images attached in the mail
#

#
# YOU NEED TO CONFIGURE THIS SCRIPT WITH SERVER NAME/USER NAME/PASSWORD
# default using 'mail.conf' and 'recp.conf'
#
# note: RFC2822 (Internet Message Format) is not the same thing as
# RFC2821 (SMTP). The prior describes the format of email,
# the later describes how to transfer the email.
#

use strict;
use warnings;

use Net::SMTP;
#use MIME::Base64;
use MIME::Lite;		# to compose mail messaage body
use Text::Lorem;	# Lorem ipsum
#use Text::Greeking::zh_TW;
use Encode qw(encode);
use Digest::MD5 qw(md5 md5_hex md5_base64);
use Getopt::Std;
use MIME::Types;

sub get_subject();
#sub get_subject_zh();
sub get_text;
sub get_config;
sub get_date;
sub shink_subject($);
sub send_email();
sub load_attach($);
sub compose_mime_body($$);
sub calc_string_hash($);


my $user;	# smtp auth user name
my $pass;	# smtp auth user password
my $host;	# SMTP host
my $from;	# mail from email address
my $port;	# not used here, only for compatible to get_config()

my $debug;	# debug mode on/off
my $repeat;	# repeat mail for each recp
my $verbose;	# more debug info
my $attach;		# one specified attach file
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

sub get_recp
{
	print "get_recp: $recp_ini\n" if $debug;
	open my $fh, $recp_ini or die "no recp.conf found";
	while (<$fh>)  {
		next if /^$/;
		next if /^#/;
		s/\n//;
		print "get_recp: $_\n" if $debug;
		push @mailto, $_;
	}
	close $fh;
}

# compose date/time string for subject
sub get_date
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d%02d%02d%02d", $mon + 1, $mday, $hour, $min;
	#print "$date\n";
	return $date;
}

# generate subject
sub get_subject()
{
	my $text = Text::Lorem->new();
	my $result = $text->words(3);

	$result = get_date() . ' ' . $result;
	undef $text;
	return $result;
}

#sub get_subject_zh()
#{
#	my $g = Text::Greeking::zh_TW->new();
#	my $result = $g->sentences(1,1);
#	my $subj_max = 10;
#
#	$result = $g->generate();
#	$result = substr($result, 0, $subj_max) if (length($result) > $subj_max);
#	$result = $result . ' ==> ' . get_date();
#	$result = encode('MIME-Header', $result);	# or 'MIME-B', "MIME-Q"
#
#	return $result;
#}

sub get_lorem_text
{
	my $text = Text::Lorem->new();
	# Generate paragraphs
	my $paragraph = $text->paragraphs(3);

	undef $text;
	return $paragraph;
}

sub get_boundary
{
	my $b = sprintf("----=Part_Foo_%04d.%d",
		int(rand(9999)), int(rand(99999)));

	return $b;
}


sub send_email()
{
	my $to_list = join(', ', @mailto);
	my $mailbody;

	if ($attach)  {
		print "using email_body_attach()\n";
		$mailbody = email_body_attach($from, $to_list, $attach);
	}
	else  {
		print "using compose_mime_body()\n";
		$mailbody = compose_mime_body($from, $to_list);
	}

	my $smtp = Net::SMTP->new($host,
							Hello => 'localhost',
							Timeout => 30,
							Debug => $debug);
	#
	# note here the password is needed
	#
	$smtp->auth($user, $pass);

	foreach my $mt (@mailto)  {
		for (0..$repeat-1)  {
			print "mailto => $mt\n";

			# send the from and recipient one by one
			$smtp->mail($from);
			$smtp->to($mt);

			# start the mail
			$smtp->data();

			# send the header
			$smtp->datasend($mailbody);

			if ($debug eq 0)  {
				printf "send a mail to (%s)\n", $mt if $debug;
			}

			# send the termination string
			$smtp->dataend();
		}
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

#
# [in] from address
# [in] to address
#
sub compose_mime_body($$)
{
	my ($from, $to) = @_;
	my ($tmp, $subject) = ( calc_string_hash($to), get_subject() );

	print $tmp,"\n" if $debug;
	$tmp = substr($tmp, 24);
	$subject = $tmp . ' ' . $subject;
	print "subject => $subject\n" if 1;#$debug;

	# MIME::Lite object
	my $msg = MIME::Lite->new(
		From	=> $from,
		To		=> $to,
#		#Cc		=> q(),
	 	#Subject => get_subject_zh(),
	 	Subject => $subject,
	 	Type	=> q(multipart/mixed),
	);

	# add a customized tag
	$msg->add('X-Camel-Comment' => 'powered by perl');

	# attach the text content
	my $textpart = MIME::Lite->new(
		Type => 'text/plain',
		Data => get_lorem_text(),
		Encoding => 'base64',
	);

	$textpart->attr("content-type.charset" => "UTF-8");
	$msg->attach($textpart);

	my @fext = qw(png gif jpg);
	my %ftype = (
		png => 'image/png',
		gif => 'image/gif',
		jpg => 'image/jpeg'
	);
 	# attach images
 	require "randpix.pm";
 	my @tmppix = ();
	for my $ext (@fext)  {
		next if (rand(6) > 3);
		my $fn = sprintf "px%d.%s", rand(999), $ext;
		pixutil::draw($fn);
		next if not -e $fn;
		$msg->attach(
			Type => $ftype{$ext},
			Path => $fn,
			Filename => $fn,
			Disposition => "attachment",
		);
		push @tmppix, $fn;
	}

	my $str = $msg->as_string;
	print $str if $debug && $verbose;
	for my $tp (@tmppix)  {
		print "delete $tp...\n" if $debug;
		unlink $tp;
	}
	return $str;
}

sub calc_string_hash($)
{
	my $str = shift;
	my $md5 = md5_hex($str);

	return $md5;
}

sub help
{
	print<<EOL;
***** help message *****
<h>elp	this message
<n>umber	repeat times
<d>debug	debug info
<v>erbose	verbose, lots lots of info
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
	my ($tmp, $subject) = ( calc_string_hash($ifile), $ifile );

	print "ifile = $ifile\n";
	if (not -e $ifile)  {
		die "cannot found $ifile\n";
	}

	print $tmp,"\n" if $debug;
	$tmp = substr($tmp, 24);
	$subject = $tmp . ' ' . $subject;
	print "subject => $subject\n" if 1;#$debug;

	# MIME::Lite object
	my $msg = MIME::Lite->new(
		From	=> $from,
		To		=> $to,
#		#Cc		=> q(),
	 	Subject => $subject,
	 	Type	=> q(multipart/mixed),
	);

	# add a customized tag
	$msg->add('X-Camel-Comment' => 'powered by perl');

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

#
# main procedure start here
#
sub main
{
	# d: debug, h: help, n: repeat times
	my $optcmd = 'dhvn:f:';

	getopts($optcmd, \%opts);

	if ($opts{h})  {
		help();
		exit 1;
	}

	$debug = $opts{d} || 0;
	$repeat = $opts{n} || 1;	# at least one time
	$verbose = $opts{v} || 0;
	$attach = $opts{f} if $opts{f};

	print_option() if $debug;

	get_config();
	get_recp();

	send_email();
}

main;
