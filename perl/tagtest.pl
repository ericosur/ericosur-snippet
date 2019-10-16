#!/usr/bin/perl

# example for Audio::TagLib

use strict;
use Audio::TagLib;
use Encode qw(from_to encode decode);

sub get_info($)
{
  my $fn = shift;
  my $f      = Audio::TagLib::FileRef->new($fn);
  my $title = $f->tag()->title()->toCString();
  my $artist = $f->tag()->artist()->toCString(1);
  my $album = $f->tag()->album()->toCString(1);
  my $track = $f->tag()->track();

  print $title,"\n";
  #printf("<%s>,<%s>,<%s>,<%s>\n", $title, $artist, $album, $track);
  #my $tit = from_to($title, "big5", "utf-8");
  #binmode(STDOUT, ':encoding(utf8)');

  #print $title,"\n";
}

sub main()
{
  my @fl = glob("*.mp3");
  #my $n=scalar(@fl);
  my $n = 1;
  while ($n>0) {
    my $fn = pop(@fl);

    # use raw/btyes to output filename
    binmode(STDOUT, ":bytes");
    printf("fn: %s\n", $fn);

    # use utf8 output
    binmode(STDOUT, ':encoding(utf8)');
    get_info($fn);

    $n --;
  }
}

main;

__END__
$f->tag()->setAlbum(Audio::TagLib::String->new("Fillmore East"));
$f->save();

my $g      = Audio::TagLib::FileRef->new("Free City Rhymes.ogg");
my $album  = $g->tag()->album();
print $album->toCString(), "\n";  # got "NYC Ghosts & Flowers"

$g->tag()->setTrack(1);
$g->save();
