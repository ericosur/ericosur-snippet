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
use Digest::MD5 qw(md5 md5_hex md5_base64);
use MIME::Types;
use WWW::Mechanize;
use Encode qw(from_to encode decode);
use Getopt::Std;

sub get_subject();
sub get_text;
sub get_config;
sub get_date;
sub shink_subject($);
sub send_email();
sub show_weather($);
sub get_lunar();
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

my $lazy_subject;

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

# compose date/time string for subject
sub get_date
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d/%02d %02d:%02d", $mon + 1, $mday, $hour, $min;
	#print "$date\n";
	return $date;
}

# generate subject
sub get_subject()
{
	my $result;
	my $lunar = get_lunar();
	my $date = get_date();

	if ($lazy_subject eq "")  {
		$result = "[天氣預報]" . $lunar . $date;
	}
	else {
		$result = $lazy_subject . $lunar;
		$result =~ s/\s+//g;
	}

	return $result;
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
	$smtp->auth($user, $pass);

	foreach my $mt (@mailto)  {
		for (0..$repeat-1)  {
			print "mailto => $mt\n" if $debug;

			# send the from and recipient one by one
			$smtp->mail($from);
			#$smtp->to($mt);
			$smtp->bcc($mt);

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

sub get_lunar()
{
	my $url = 'http://tw.news.yahoo.com/';
	my $mech = WWW::Mechanize->new();
	$mech->get($url);
	my $html = $mech->content();
	my $msg = "null";

	# get rip off messy stuff
	$html =~ s/[\r\n]//g;	# 變成一長行
	$html =~ s/\<[^\<]+\>//g;	# 可以把大部份的 tag 都去掉

	# 農曆 (己丑) 三月十三日 09:30 更新
	if ( $html =~ m/(農曆.+日) \d+:/ )  {
		$msg = $1;
	}

	return $msg;
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

	# to fetch infomation first, for subject and mail body
	my $mail_body = twoday();
	my $subject = get_subject();
	print "subject => $subject\n" if $debug;

	# MIME::Lite object
	my $msg = MIME::Lite->new(
		From	=> $from,
		#To		=> $to,
		#Cc		=> q(),
		Bcc => $to,
	 	#Subject => get_subject_zh(),
	 	Subject => $subject,
	 	Type	=> q(multipart/mixed),
	);


	# add a customized tag
	$msg->add('X-Camel-Comment' => 'powered by perl');
	$msg->add('X-Author-Comment' => 'script by ericosur');

	# attach the text content
	my $textpart = MIME::Lite->new(
		Type => 'text/plain',
		#Data => get_lorem_text(),
		Data => twoday(),
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

	my $str = $msg->as_string;
	print $str if $debug && $verbose;
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
		#To		=> $to,
		#Cc		=> q(),
		Bcc		=> $to,
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
	write_log();
}


# make string more beautiful
sub format_str($)
{
	my $str = shift;
	$str =~ s/&deg;/度/;	# change &deg; to ''度''
	$str =~ s/(\s+)/\t/g;
	$str =~ s/(\d+%)/降雨機率$1/;	# add description for percent
	return $str;
}

sub show_weather($)
{
	my $url = shift;
	my $mech = WWW::Mechanize->new();
	$mech->get($url);
	my $html = $mech->content();

#
# get rip off messy stuff
#
	$html =~ s/\r//g;
	$html =~ s/\n//g;	# 變成一長行
	$html =~ s/\<[^\<]+\>//g;	# 可以把大部份的 tag 都去掉

	#print STDERR $html;	# for debugging

	my ($ptime, $vtime, $t1, $t2);
	my $msg;

	$ptime = $1 if ($html =~ m/(發.*)有/);
	$vtime = $1 if ($html =~ m/(有[^\s]+)/);
	#print "$ptime\n$vtime\n";
	$msg = "$ptime\n$vtime\n";

	$t1 = $1 if ($html =~ m/(台北市.*)基/);
	$t2 = $1 if ($html =~ m/(台北地區.*)桃/);
	$t1 = format_str($t1);
	$t2 = format_str($t2);
	$msg = $msg . "$t1\n$t2\n";

	$lazy_subject = $t1 if $lazy_subject eq "";

	return $msg;
}

sub twoday()
{
	my @url = (
			'http://tw.weather.yahoo.com/today.html',
			'http://tw.weather.yahoo.com/tomorrow.html',
	);
	my $msg;

	foreach (@url)  {
		$msg = $msg . show_weather($_);
	}

	return $msg;
}

main;
