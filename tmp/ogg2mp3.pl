#!/usr/bin/perl -w
# Filename:	ogg2mp3
# Author:	David Ljung Madison <DaveSource.com>
# See License:	http://MarginalHacks.com/License
# Description:	Converts ogg to mp3, with artist/title/info
# Ideas from:  Joseph E. O'Doherty <odoherty.net>

use strict;
use File::Spec;

##################################################
# Setup the variables
##################################################
my $PROGNAME = $0;
$PROGNAME =~ s|.*/||;

my $TMPFILE = File::Spec->catfile( File::Spec->tmpdir(), "$PROGNAME.$$.wav" );

#########################
# Ogg decoder
#########################
# Different versions of ogg123 handle files differently!  Argh!
#my $OGGDEC = "ogg123 -d wav -o file:$TMPFILE";
#my $OGGDEC = "ogg123 -d wav -f $TMPFILE";
# Just use oggdec instead.
# Add -Q for quiet..
my $OGGDEC = "oggdec -o $TMPFILE";

#########################
# MP3 encoder
# Choose your favorite..
#########################
#my $MP3ENC = "lame";
my $MP3ENC = "notlame";

my $OGGINFO = "ogginfo";
my $MP3INFO = "id3tool";

##################################################
# Usage
##################################################
sub usage {
  foreach my $msg (@_) { print STDERR "ERROR:  $msg\n"; }
print <<USAGE;

Usage:\t$PROGNAME [-d] [-o <dir>] <ogg> ..
  Converts ogg to mp3
  -d                  Set debug mode
  -o <dir>            Specify output directory
  -keepdir            Keep directory structure inside specified -o directory
  -f                  Force rewriting of mp3 if it already exists
  --enc_opts .. --    Options for encoding tool
  --dec_opts .. --    Options for decoding tool

  Example:  $PROGNAME --enc_opts -b 64 -- *.ogg

USAGE
  exit -1;
}

sub get_dashdash {
	my @dash;
	while ($#ARGV>=0) {
		my $arg=shift(@ARGV);
		last if $arg eq "--";
		push(@dash,$arg);
	}
	@dash;
}

sub parse_args {
	my $opt = {};
	my $outdir;
	my @oggs;
	while (my $arg=shift(@ARGV)) {
		if ($arg =~ /^-h$/) { usage(); }
		if ($arg =~ /^-d$/) { $MAIN::DEBUG=1; next; }
		if ($arg =~ /^-o$/) { $opt->{out}=shift @ARGV; next; }
		if ($arg =~ /^-keepdir$/) { $opt->{keepdir}=1; next; }
		if ($arg =~ /^-f$/) { $opt->{force}=1; next; }
		if ($arg =~ /^--enc_opts$/) { push(@{$opt->{enc_opts}}, get_dashdash()); next; }
		if ($arg =~ /^--dec_opts$/) { push(@{$opt->{dec_opts}}, get_dashdash()); next; }
		if ($arg =~ /^-/) { usage("Unknown option: $arg"); }
		push(@oggs, $arg);
	}
	usage("No oggs specified") unless @oggs;

	($opt,@oggs);
}

sub debug {
	return unless $MAIN::DEBUG;
	foreach my $msg (@_) { print STDERR "[$PROGNAME] $msg\n"; }
}

##################################################
# Genre code
##################################################
my @GENRES;
open(G,"$MP3INFO -l|") || die("[$PROGNAME] Can't get genre info: [$MP3INFO -l]\n");
while (<G>) {
	push(@GENRES,$1) if (/^(\S.*\S)\s+\|/);
}
close G;

sub get_genre {
	my ($genre) = @_;
	return undef unless $genre;
	my @g = grep(/^$genre$/i, @GENRES);
	return $g[0] if @g;
	@g = grep(/$genre/i, @GENRES);
	print STDERR "[$PROGNAME] Multiple genre matches [$genre -> @g]\n" if $#g>0;
	return $g[0] if @g;
	# No match
	print STDERR "[$PROGNAME] Unknown genre [$genre]\n";
	return undef;
}

##################################################
# Main code
##################################################
sub ogginfo {
	my ($ogg) = @_;

	# Get ogg tags
	open(TAGS,"$OGGINFO \Q$ogg\E |") || die("[$PROGNAME] Couldn't run ogginfo [$ogg]\n");
	my %i;
	while(<TAGS>) {
		chomp;
		next if /^\s*$/;

## The old way:
#		die("[$PROGNAME] Bad ogginfo: [$_]") unless /^\s*(\S+)=(.*)$/;
#		$i{$1} .= $2;

## Old ogginfo:
## "key=value"
##
## New ogginfo:
## "Some comment stuff..."
## "	key=value"
##
## I suppose I could parse the entire output to see if it's new or
## old, but it looks like the comments never have '=' in them, and who
## cares if it does anyways?  So, we'll just use a loose regexp:
		if (/^\s*(\S+)=(.*)$/) {
			my ($tag,$val) = (lc($1),$2);
			$i{$tag} .= $val
		}
	}
	close(TAGS);
	\%i;
}

sub set_mp3info {
	my ($mp3,$info) = @_;
	my $set;
	# Newer id3tool supports setting track
	#$set .= " -n \QTrack $info->{tracknumber}\E" if $info->{tracknumber} && !$info->{comment};
	$set .= " -c \Q$info->{tracknumber}\E" if $info->{tracknumber};
	$set .= " -t \Q$info->{title}\E" if $info->{title};
	$set .= " -a \Q$info->{album}\E" if $info->{album};
	$set .= " -r \Q$info->{artist}\E" if $info->{artist};
	$set .= " -n \Q$info->{comment}\E" if $info->{comment};
	my $genre = get_genre($info->{genre});
	$set .= " -G \Q$genre\E" if $genre;
	$set .= " -y \Q$info->{date}\E" if $info->{date} && $info->{date} =~ /^\d+$/;
	return print STDERR "[$PROGNAME] No tag info for [$mp3]\n" unless $set;
	system("$MP3INFO $set \Q$mp3\E");
	print STDERR "[$PROGNAME] Errors from:\n  $MP3INFO $set $mp3\n  $!\n" if $?;
}

sub ogg2mp3 {
	my ($opt,$ogg) = @_;
	my $mp3 = $ogg;
	$mp3 =~ s/(\.ogg)?$/.mp3/i;

	# Handle outdir if specified
	if ($opt->{out}) {
		$mp3 =~ s|.*/||g unless $opt->{keepdir};
		$mp3 = "$opt->{out}/$mp3";
	}

	return print STDERR "[$PROGNAME] Skipping mp3 (already exists) [$mp3]\n"
		if !$opt->{force} && -f $mp3;

	my $dec_opts = $opt->{dec_opts} ? join(' ',@{$opt->{dec_opts}}) : "";
	my $enc_opts = $opt->{enc_opts} ? join(' ',@{$opt->{enc_opts}}) : "";

	print "$ogg -> $mp3\n";

	# Decode
#	system("$OGGDEC \Q$ogg\E | $MP3ENC - \Q$mp3\E");
#	print STDERR "[$PROGNAME] Errors from:\n  $OGGDEC \Q$ogg\E | $MP3ENC - \Q$mp3\E\n  $!\n"
#		if $?;
	system("$OGGDEC $dec_opts \Q$ogg\E");
	print STDERR "[$PROGNAME] Errors from:\n  $OGGDEC \Q$ogg\E\n  $!\n" if $?;

	# Encode
	system("$MP3ENC $enc_opts $TMPFILE \Q$mp3\E");
	print STDERR "[$PROGNAME] Errors from:\n  $MP3ENC $TMPFILE \Q$mp3\E\n  $!\n" if $?;
	unlink $TMPFILE;


	my $info = ogginfo($ogg);
	set_mp3info($mp3,$info);
}

sub main {
	my ($opt,@oggs) = parse_args();

	map(ogg2mp3($opt,$_), @oggs);
}
main();

__END__
這個script的特色是：
它不只轉換ogg to mp3 它還會把ogg的歌手，專輯標籤,一個個的補到mp3標籤中。
而小弟自己的使用心得是：只要打入指令，和所有要轉換的ogg檔（中間隔空白）
                        這個腳本就一個個的幫你轉好（超方便）。

一，在下載之前，請先安裝以下各個必要套件：
        1perl                本程式的主要執行
        2id3tool             mp3的標籤編輯程式
        3vorbis tools        OGG的編碼與解碼的套件。
        4lame                WAV轉mp3的轉碼程式。

二，套件滿足後，請到 http://marginalhacks.com/bin/ogg2mp3  下載script。
        下載後的腳本並不是馬上可以用，請修改33行與34行，修改重點如下：
        行號｜程式
        29   | #########################
        30   | # MP3 encoder
        31   | # Choose your favorite..
        32   | #########################
        33   | my $MP3ENC = &quotlame"       <----
        34   | #my $MP3ENC = &quotnotlame"<----這是我修改後的狀況
        35
        36   | my $OGGINFO = &quotogginfo"
        37   | my $MP3INFO = &quotid3tool"
        如果你有其他熟悉的mp3編碼程式，請把notlame改成你的mp3編碼程式。
        33   | #my $MP3ENC = &quotlame"
        34   | my $MP3ENC = &quotnotlame"
註：小弟的mp3編碼程式是lame，使用無誤，而別的並沒有實用過，
    如果不是lame而有問題，請自己問原作者。
三，將本腳本複製到你的path下面（不知道在哪？請執行:echo $PATH）
    改變執行權限。chmod 744 ogg2mp3
四，大功告成！

後記，本文是因為小弟需要轉mp3給自己爸爸聽的，
        但是怎麼找只有向這樣的傳換程式：
        if [ $# != 2 ]; then
        echo &quotUsage: ogg2mp3 "
        fi
        #converting!
        oggdec $1 -o - | lame - $2.mp3
        exit 0
        這充其量也只有轉mp3的音效罷了。經過谷歌大神的幫助下，發現的這隻perl
        而且還可以大量的轉！不管幾首ogg只要輸入

        ogg2mp3 歌曲一.ogg 歌曲2.ogg 歌曲三.ogg

        這隻腳本就一個個的幫你轉好好喔，還把標籤一個個補完。一整個方便！
        遺憾的是小弟不能把整個程式碼貼上，因為作者有交代，只可以連結和介紹。
        最後希望各位使用愉快！

免則與免費聲明中的重點：
1該網站下面的各項程式,並不是很方便安裝的。而且沒有任何擔保！
2如果可以自行安裝,且使用方便,作者們也會相當開心。
3作者很願意收到使用後的感謝回應與相關修正。
4如果有paypal的帳號，而且還願意付點錢支持他們，在免費條款下就可以提供支持。
