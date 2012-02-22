#!/usr/bin/perl
use strict;
use warnings;

use WWW::Mechanize;
use Win32::Clipboard;

my $clip = Win32::Clipboard();

sub foo(@)  {
	my $fn;
	($_, $fn) = @_;
	my $m = 'WWW::Mechanize'->new;
	my $t;

	print STDERR "get from: $_\n";
	$_ =~ s[http://|tw\.|www\.|youtube\.com/|watch\?|v=|][]g;
	$fn = $_ . '.flv' if !defined $fn;	# use default if not specified
	print STDERR "$_\n";

	($t = $m->get("http://www.youtube.com/v/$_")->request->uri) =~ s/.*&t=(.+)/$1/;
	$m->get("http://www.youtube.com/get_video?video_id=$_&t=$t", ':content_file', "$fn");
	$clip->Set($fn);	# put the result into clipboard
	print STDERR "output to $fn\n" if -e $fn;
}

if (not @ARGV)  {
	foo( $clip->Get() );
}
else  {
	foo(@ARGV);
}


__END__

=pod

=head1 NAME

get_youtube.pl

=head1 DESCRIPTION

Get flv file from given youtube url. The URL could retrieve from the
URL line of browser or the description.

=head1 SYSNOPSIS

get_youtube.pl "http://www.youtube.com/watch?v=aY2azHo0LAU"

=cut


# references
# the one-liner version:

#1
perl -MWWW::Mechanize -e '$_ = shift; s#http://|www\.|youtube\.com/|watch\?|v=|##g; $m = WWW::Mechanize->new; ($t = $m->get("http://www.youtube.com/v/$_")->request->uri) =~ s/.*&t=(.+)/$1/; $m->get("http://www.youtube.com/get_video?video_id=$_&t=$t", ":content_file" => "$_.flv")'

#2
perl -MWWW::Mechanize -e '$_ = shift; ($y, $i) = m#(http://www\.youtube\.com)/watch\?v=(.+)#; $m = WWW::Mechanize->new; ($t = $m->get("$y/v/$i")->request->uri) =~ s/.*&t=(.+)/$1/; $m->get("$y/get_video?video_id=$i&t=$t", ":content_file" => "$i.flv")'

#3
perl -MLWP -e '($y,$i)=shift=~/^(.+m)\/.+v=(.+)/;($m=LWP::UserAgent->new)->get("$y/get_video?video_id=$i&t=".($m->get("$y/v/$i")->request->uri=~/&t=(.+)/)[0],":content_file"=>"$i.flv")' 'http://www.youtube.com/watch?v=l69Vi5IDc0g'

#4
perl -MLWP -e'
( $y, $i ) = shift =~ /^(.+m)\/.+v=(.+)/;
( $m = LWP::UserAgent->new )->get(
    "$y/get_video?video_id=$i&t="
      . ( $m->get("$y/v/$i")->request->uri
             =~ /&t=(.+)/
        )[0],
    ":content_file" => "$i.flv"
  )'

#5
perl -MWWW::Mechanize -e'$y="http://youtube.com";($i)=pop=~/\w+$/g;$m=new WWW::Mechanize;$m->get("$y/v/$i")->request->uri=~/&t=.+/;$m->get("$y/get_video?video_id=$i$&",":content_file"=>"$i.flv")'

#4 (win)
perl -MO=Deparse -MLWP -e"$y='http://youtube.com';($i)=pop=~/\w+$/g;($m=new LWP::UserAgent)->get(qq{$y/v/$i})->request->uri=~/&t=.+/;$m->get(qq{$y/get_video?video_id=$i$&},':content_file',$i.'.flv')" "l69Vi5IDc0g"
