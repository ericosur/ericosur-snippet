#!/usr/bin/env perl


use strict;
use v5.10;
use Storable;

my $cinfile = 'bpmf.cin';

sub parse_keyname()
{
	my %keyname = ();
	open my $ifh, $cinfile or die;

	my $flag = 0;
	while ( <$ifh> )  {
		s/[\r\n]//;
		if ($flag == 0)  {
			if ( $_ =~ "\%keyname  begin" )  {
				#say "==> keyname begin";
				$flag = 1;
			}
		}
		elsif ($flag == 1)  {
			if ($_ =~ "\%keyname  end")  {
				#say "==> keyname end";
				$flag = 0;
			}
			else {
				#say $_;
				$_ =~ m/^(\S)\s+(\S+)$/;
				my $code = key_to_num($1);
				$keyname{$code} = $2;
			}
		}
	}

	close $ifh;
	return %keyname;
}

sub parse_chardef()
{
	my %chardef = ();
	open my $ifh, $cinfile or die;
	my $cnt = 0;
	my $flag = 0;

	while ( <$ifh> )  {
		s/[\r\n]//;
		if ($flag == 0)  {
			if ( $_ =~ "\%chardef  begin" )  {
				#say "==> keyname begin";
				$flag = 1;
			}
		}
		elsif ($flag == 1)  {
			if ($_ =~ "\%chardef  end")  {
				#say "==> keyname end";
				$flag = 0;
			}
			else {
				#say $_;
				$_ =~ m/^(\S+)\s+(\S+)$/;
				my $keynum = key_to_num($1);
				$chardef{$keynum} = $2;
				$cnt ++;
			}
		}
	}

	close $ifh;
	say "cnt: ", $cnt;
	return %chardef;
}

sub key_to_num($)
{
	my $str = shift;
	my $num;
	foreach my $cc (split //, $str)  {
		$num = $num . sprintf("%02x", ord($cc));
	}
	#say $num;
	return $num;
}


sub dump_hash($)
{
	my $href = shift;
	my %hh = %$href;
	foreach my $kk (keys(%hh))  {
		say $kk . " => " . $hh{$kk};
	}
}


sub show_key($$)
{
	my $key = shift;
	my $rkeyname = shift;
	my %keyname = %$rkeyname;
	my $out;

	#say "show_key(): ", $key;

	for (my $i=0; $i<length($key)/2; $i++)  {
		my $cc = substr($key, $i*2, 2);
		#say $cc;
		$out = $out . $keyname{$cc};
	}

	return $out;
}

# hash of chardef
# hash of keyname
sub dump_key_hash($$)
{
	my $rcd = shift;
	my $rkn = shift;
	my %hh = %$rcd;
	foreach my $kk (sort keys(%hh))  {
		say show_key($kk, $rkn) . " => " . $hh{$kk};
	}
}

sub collect_first_key($)
{
	my %first = ();
	my $rh = shift;
	my %cd = %$rh;

	# $seq: "635963"
	foreach my $seq ( keys(%cd) )  {
#		if ( length($seq) == 2 )  {
#			say "one word ===> ", $seq;
#		}
#		else  {
			my $sb = substr($seq, 0, 2);	# first key only
			$first{$sb} ++;
#		}
	}
	return %first;
}

sub main()
{
	key_to_num("abc");

	my %kn = ();
	%kn = parse_keyname();
	#dump_hash(\%kn);
	say "size of key names: ", scalar(keys(%kn));

	say "-" x 80;

	my %cd = ();
	%cd = parse_chardef();
	#dump_key_hash(\%cd, \%kn);

	say "-" x 80;

	my %first_key = collect_first_key(\%cd);
	dump_key_hash(\%first_key, \%kn);
	say "size of \%first_key: ", scalar(keys(%first_key));

	say "-" x 80;

}


main;
