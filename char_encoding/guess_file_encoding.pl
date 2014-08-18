#!/usr/bin/perl
#
# copied from http://bbs.perlchina.org/ccb/topic_view.cgi?forum=4&article_id=0004070705234901&publishtime_id=0004070705234901&new_window=1&page=400
#

use Encode;
use Encode::Guess;

my %opt = (
	encode => 'UTF-16',
	buf_sz => 1024, # the buffer size when is used to guess file encoding
);

sub guess_file_encoding($);
sub convert($$;$);
sub open_file($$;$);

sub convert ($$;$) {
	my $src_file = shift or die "input the file to convert encoding\n";
	my $encoding = shift or die "input the target encoding\n";
	my $dest_file = shift or ( my $dest_file = $src_file ) =~ s{\.}{_$encoding\.}xms;

	# guess file encoding first
	my $decoding = guess_file_encoding( $src_file );

	my $FH_IN = open_file( $src_file, '<', $decoding );
	my $FH_OUT = open_file( $dest_file, '>', $encoding );

	while ( <$FH_IN> ) {
		print $FH_OUT $_;
	}

	close $FH_OUT;
	close $FH_IN;
}

sub guess_file_encoding($) {
	my $file = shift or die "input file first\n$!";

	open my $FH, '<', $file or die "$!";
	my @default_layers = PerlIO::get_layers($FH);
	binmode($FH, ':pop') if $default_layers[-1] eq 'crlf';
	binmode($FH, ':raw');
	my ( $buf, $buf_sz );
	$buf_sz = $opt{buf_sz} < -s $file ? $opt{buf_sz} : -s _;
	read( $FH, $buf, $buf_sz );
	my $decoder = Encode::Guess->guess( $buf );
	die $decoder unless ref($decoder);
	close $FH;

	return $decoder->name;
}

sub open_file ($$;$) {
	my ( $file, $mode, $encoding ) = @_;

	$encoding ||= $opt{encode}; # default
	unless ( Encode::perlio_ok($encoding) ) {
		die "the target encoding: $encoding is not support in PerlIO\n";
	}

	open my $FH, $mode, $file or die "$!";

	my @default_layers = PerlIO::get_layers($FH);
	binmode($FH, ':pop') if $default_layers[-1] eq 'crlf';

	my $add_bom_flag = 0;
	if ( $^O eq 'MSWin32'
	&& ( $mode eq '>' || $mode eq 'w' ) # we only play the trick for write only
	&& $encoding eq 'UTF-16' ) {
		# UTF-16 in win32 perl will mistakenly make BOM to be BE
		# which is not convenient, so we make a trick to solve it
		$encoding = 'UTF-16LE';
		$add_bom_flag = 1;
	}

	my $new_layers = ':perlio:raw' . ":encoding($encoding)" . 'crlf:utf8';

	binmode($FH, $new_layers);
	# print "$_\t" foreach PerlIO::get_layers($FH);

	print $FH "\x{feff}" if $add_bom_flag; # BOM

	return $FH;
}

my $file  = $ARGV[0] || "list.txt";
print "guess_file_encoding($file)\t";
print guess_file_encoding($file), "\n";
