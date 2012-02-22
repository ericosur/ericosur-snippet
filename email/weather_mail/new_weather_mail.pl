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
use LWP::Simple;
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

my $lazy_subject = "";

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
		$result = "[天氣預報]";
		$result = $result . $lunar if $lunar;
		$result = $result . $date  if $date;
	}
	else {
		$result = $lazy_subject if $lazy_subject;
		$result = $result . $lunar if $lunar;
		$result =~ s/\s+//g;
		printf "%d: %s\n", __LINE__, $result;
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

	#return;	# hack - omit sending email for debug

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
	my $html = get($url);
	my $msg = "null";

	# get rip off messy stuff
	$html = untag($html);
	$html =~ s/\s+\n//gm;
	$html =~ s/\n+/\n/gm;

	print STDERR $html if $debug;

	# 農曆 (己丑) 三月十三日 09:30 更新
	if ( $html =~ m/(農曆.+日)/ )  {
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
	print "body => $mail_body\n" if $debug;

	# MIME::Lite object
	my $msg = MIME::Lite->new(
		From	=> $from,
		Bcc => $to,
	 	Subject => $subject,
	 	Type	=> q(multipart/mixed)
		#To		=> $to,
		#Cc		=> q(),
	 	#Subject => get_subject_zh(),
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
	 	Subject => encode('MIME-Header', $subject),
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


# make string more beautiful
sub format_str($)
{
	my $str = shift;
	return "" unless $str;

	$str =~ s/&deg;/度/;	# change &deg; to ''度''
	$str =~ s/(\s+)/\t/g;
	$str =~ s/(\d+%)/降雨機率$1/;	# add description for percent
	return $str;
}

# this function is copied from http://www.perlmonks.org/?node_id=161281
sub untag {
  local $_ = $_[0] || $_;
# ALGORITHM:
#   find < ,
#       comment <!-- ... -->,
#       or comment <? ... ?> ,
#       or one of the start tags which require correspond
#           end tag plus all to end tag
#       or if \s or ="
#           then skip to next "
#           else [^>]
#   >
  s{
    <               # open tag
    (?:             # open group (A)
      (!--) |       #   comment (1) or
      (\?) |        #   another comment (2) or
      (?i:          #   open group (B) for /i
        ( TITLE  |  #     one of start tags
          SCRIPT |  #     for which
          APPLET |  #     must be skipped
          OBJECT |  #     all content
          STYLE     #     to correspond
        )           #     end tag (3)
      ) |           #   close group (B), or
      ([!/A-Za-z])  #   one of these chars, remember in (4)
    )               # close group (A)
    (?(4)           # if previous case is (4)
      (?:           #   open group (C)
        (?!         #     and next is not : (D)
          [\s=]     #       \s or "="
          ["`']     #       with open quotes
        )           #     close (D)
        [^>] |      #     and not close tag or
        [\s=]       #     \s or "=" with
        `[^`]*` |   #     something in quotes ` or
        [\s=]       #     \s or "=" with
        '[^']*' |   #     something in quotes ' or
        [\s=]       #     \s or "=" with
        "[^"]*"     #     something in quotes "
      )*            #   repeat (C) 0 or more times
    |               # else (if previous case is not (4))
      .*?           #   minimum of any chars
    )               # end if previous char is (4)
    (?(1)           # if comment (1)
      (?<=--)       #   wait for "--"
    )               # end if comment (1)
    (?(2)           # if another comment (2)
      (?<=\?)       #   wait for "?"
    )               # end if another comment (2)
    (?(3)           # if one of tags-containers (3)
      </            #   wait for end
      (?i:\3)       #   of this tag
      (?:\s[^>]*)?  #   skip junk to ">"
    )               # end if (3)
    >               # tag closed
   }{}gsx;          # STRIP THIS TAG
  return $_ ? $_ : "";
}



sub show_weather($)
{
	my $url = shift;
	my $html = get($url);
	my $dbg = 1;

	$html = untag($html);

#
# get rip off messy stuff
#
	$html =~ s/\s+\n//g;
	$html =~ s/\n+/\n/gm;

	my ($ptime, $vtime, $t1, $t2);
	my $msg = "";

	die unless $html;
	if ($debug)  {
		print STDERR "天氣預測：\n", $html;
	}

	if ($html =~ m/(發.*分)/)  {
		$ptime = $1;
		print $ptime,"\n" if $debug;
		$msg = $msg . $ptime . "\n";
	}
	else {
		print "cannot match\n" if $debug;
	}
	if ($html =~ m/(有[^\s]+)/m) {
		$vtime = $1;
		print $vtime,"\n" if $debug;
		$msg = $msg . $vtime . "\n";
	}
	else {
		print "cannot match\n" if $debug;
	}

	my ($ua1, $ua2);
	$t1 = $1 if ($html =~ m/(台北市.*)/);
	if ($html =~ m/(\d+%) 基隆/) {
		$ua1 = $1;
		$t1 = $t1 . $ua1 if $ua1;
	}
	$t2 = $1 if ($html =~ m/(台北地區.*)/);
	if ($html =~ m/(\d+%) 桃園/) {
		$ua2 = $1;
		$t2 = $t2 . $ua2 if $ua2;
	}
	$t1 = format_str($t1);
	$t2 = format_str($t2);
	$msg = $msg . "$t1\n$t2\n";

	if ($t1)  {
		$lazy_subject = $t1 if $lazy_subject eq "";
		print "lazy_subject = $lazy_subject\n" if $debug;
	}

	return $msg;
}

sub twoday()
{
	my @url = (
			'http://tw.weather.yahoo.com/today.html',
			'http://tw.weather.yahoo.com/tomorrow.html',
	);
	my @append_msg = ("今日天氣預報\n", "明日天氣預報\n");
	my $msg = "";

	foreach my $ii (0..1)  {
		$msg = $msg . $append_msg[$ii] . show_weather($url[$ii]);
		$msg = $msg . "\n";
	}

	my $m2 = get_current_weather();
	if ($m2)  {
		$msg = $msg . "\n" . "目前天氣概況：\n" . $m2;
	}

	return $msg;
}

sub fetch_pdf()
{
	my $mech = WWW::Mechanize->new( autocheck => 1 );
	# 偽裝為 IE6
	$mech->agent_alias( 'Windows IE 6' );

	my $url = q(http://www.cwb.gov.tw/V5/forecast/taiwan/Data/W31.pdf);

	my $file = 'tmp.pdf';	# default name
	if ( $url =~ m!\/([^/]+)$! )  {
		$file = $1 if $1;
		$file = lc($file);
	}
	#print "file: ", $file,"\n";
	$mech->get($url, ":content_file" => $file);

	return $file;
}

# call ''pdftotext'' come with CAM::PDF
# also need poddler-data package for CJK pdf
sub pdf_to_text($)
{
	my $ifile = shift;
	my $ofile = $ifile;

	$ofile =~ s!\.pdf!\.txt!i;
	my $cmd = 'pdftotext -layout ' . $ifile . ' ' . $ofile;
	system $cmd;
	return $ofile;
}


sub get_wanted_line($)
{
	my $file = shift;
	my $line;
	my $otime;

	open my $fh, $file or die;
	while ( <$fh> ) {
		s/[\r\n]//;
		if ( m/觀測時間/ )  {
			s/\\//;
			$otime = $_;
			next;
		}
		if ( m/台\s+北/ )  {
			s/台\s+北/台北\t/;
			$line = $_;
			$line =~ s!				# to parse ''20.1(+3.5)''
				(
					-?\d*\.\d+			# 20.1
				)
				\(
					\s*
						([+-]\d+\.\d+)	# +3.5
					\s*
				\)
				!
					\t$1\($2\)
				!x;
			#printf("<%s>\t<%s>\n", $1, $2);
			$line =~ s/\s{2,}/\t/g;
			last;
		}
	}
	close $fh;

	return "" unless $line;

	my @a = split /\t/, $line;
	my $msg;

	print $otime, "\n" if $debug;
	$msg = sprintf("站名: %s\n風向: %s\n風力: %s\n陣風: %s\n能見度: %s\n氣溫: %s\n濕度: %s
氣壓: %s\n天氣: %s\n累積雨量: %s\n", $a[0], $a[1], $a[2], $a[3], $a[4], $a[5], $a[6],
		$a[7], $a[8], $a[9]);
}

sub get_current_weather
{
	my $ofile = fetch_pdf();
	my $textfile = pdf_to_text($ofile);
	my $msg = get_wanted_line($textfile);
	return $msg;
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


main;
