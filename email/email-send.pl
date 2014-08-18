#!/usr/bin/perl
#
# problems
#

use strict;
use warnings;

use Email::Send;
use Email::Simple::Creator; # or other Email::
use Email::MIME::Creator;
use IO::All;
use Config::Simple;

my $debug = 0;
my $verbose = 0;
my @mailto = ();
my %conf = ();

sub send_mail($)
{
	my $body = shift;

	my $mailer = Email::Send->new( {
	    mailer => 'SMTP::TLS',
	    mailer_args => [
	        Host => $conf{'gmail.smtp'},
	        Port => 587,
	        User => $conf{'gmail.user'},
	        Password => $conf{'gmail.password'},
	        Hello => 'localhost',
	    ]
	} );

	my $email = Email::Simple->create(
	    header => [
	        From    => $conf{'gmail.user'},
	        To      => $conf{'gmail.user'},
	        Subject => &get_date,
	    ],
	    body => get_data(),
	);

	eval { $mailer->send($email) };
	die "Error sending email: $@" if $@;
}

sub get_data()
{
	return `cmd /c dir /s /b`;
}

sub generate_email_body()
{
	*rcpts = *cc_rcpts = *bcc_rcpts = sub { 'ericosur@gmail.com' };

	# multipart message
	my @parts = (
	  Email::MIME->create(
	      attributes => {
	          filename     => "img001.jpg",
	          content_type => "image/jpeg",
	          encoding     => "base64",
	          name         => "img001.jpg",
	      },
	      body => io( "img001.jpg" )->all,
	  ),
	  Email::MIME->create(
	      attributes => {
	          content_type => "text/plain",
	          disposition  => "attachment",
	          charset      => "UTF-8",
	      },
	      body => "Hello there!",
	  ),
	);

	my $email = Email::MIME->create(
	  header => [ From => $conf{'gmail.user'} ],
	  parts  => [ @parts ],
	);

	# standard modifications
	$email->header_set( 'X-PoweredBy' => 'perl Email-Send'      );
	$email->header_set( To            => rcpts()        );
	$email->header_set( Cc            => cc_rcpts()    );
	$email->header_set( Bcc           => bcc_rcpts() );

	# more advanced
	$_->encoding_set( 'base64' ) for $email->parts;

	return $email->as_string;
}

=pod
sub get_recp($)
{
	my $recp_ini = shift;

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
=cut

# compose date/time string for subject
sub get_date
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d%02d%02d%02d", $mon + 1, $mday, $hour, $min;
	#print "$date\n";
	return $date;
}

sub see
{
	printf("user: %s\nhost: %s\n",
		$conf{'gmail.user'}, $conf{'gmail.smtp'}, $conf{'gmail.password'});
}

sub get_ini($$)
{
	my $config_file = shift;
	my $confref = shift;

	Config::Simple->import_from($config_file, $confref);
}

sub main
{
	my $emailbody;

	get_ini('gmail.ini', \%conf);
	see;
	$emailbody = generate_email_body();

#	print $emailbody;
	send_mail($emailbody);
}

main;
