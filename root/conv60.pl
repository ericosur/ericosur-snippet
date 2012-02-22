use strict;
use 5.010;

#
# ddd.ddddd		25.06367
# ddd,mm.mmm	25,03.820
# ddd,mm,ss.s	25,03,49.2
#

sub dms_to_dd($$$)
{
	my ($dd,$mm,$ss) = @_;
	$mm = $mm + $ss / 60.0;
	$dd = $dd + $mm / 60.0;
	my $res = 0.0;
	$res = sprintf("%.5f",$dd);
	say "dms_to_dd: " . $res;
	return $res;
}

sub dms_to_ddmm($$$)
{
	my ($dd,$mm,$ss) = @_;
	$mm = $mm + $ss / 60.0;
	my $res = 0.0;
	$res = sprintf("%d,%.3f",$dd,$mm);
	say "dms_to_ddmm: " . $res;
	return $res;
}

sub ddmm_to_dms($$)
{
	my ($dd,$mm) = @_;
	my $ss = 0;

	if ( $mm =~ m/(\d+)(\.\d+)?/ )  {
		if ($2)  {
			$mm = $1;
			$ss = $2 * 60;
		}
	}

	my $res = sprintf("%d,%d,%.1f", $dd, $mm, $ss);
	say "ddmm_to_dms: " . $res;
	my $rdd = sprintf("%d",$dd);
	my $rmm = sprintf("%d",$mm);
	my $rss = sprintf("%.1f",$ss);
	return ($rdd,$rmm,$rss);
}

sub dd_to_dms($)
{
	my $deg = shift;
	my ($dd,$mm,$ss) = (0,0,0);

	#printf("deg:%s\n", $deg);

	if ( $deg =~ m/(\d+)(\.\d+)?/ )  {
		$dd = $1;
		if ($2)  {
			$mm = $2 * 60;
			#say __LINE__ . ":  $mm";
			if ($mm =~ m/(\d+)(\.\d+)?/)  {
				$mm = $1;
				$ss = $2 * 60 if $2;
			}
		}
	}

	my $res = sprintf("%d,%d,%.1f", $dd, $mm, $ss);
	say "dd_to_dms: " . $res;
	my $rdd = sprintf("%d",$dd);
	my $rmm = sprintf("%d",$mm);
	my $rss = sprintf("%.1f",$ss);
	return ($rdd,$rmm,$rss);
}

sub convert($)
{
	my $parm = shift;

	my @ele = split(/['",\s]/, $parm);	# '
	my $num = scalar @ele;
	my ($dd,$mm,$ss) = @ele;
	my ($rdd,$rmm,$rss) = (0,0,0);

	if ($num == 1)  {
		say "in: $dd";
		($rdd,$rmm,$rss) = dd_to_dms($dd);
		dms_to_ddmm($rdd,$rmm,$rss);
	} elsif ($num == 2)  {
		say "in: $dd,$mm";
		($rdd,$rmm,$rss) = ddmm_to_dms($dd,$mm);
		dms_to_dd($rdd,$rmm,$rss);
	} elsif ($num == 3)  {
		say "in: $dd,$mm,$ss";
		dms_to_dd($dd,$mm,$ss);
		dms_to_ddmm($dd,$mm,$ss);
	} else  {
		say "error!";
	}
}

sub main()
{
	if ( scalar @ARGV == 0 )  {
		push @ARGV, "25.06367";
	}

	foreach my $astr (@ARGV)  {
		#printf("%s\n", $astr);
		convert($astr);
	}

# ddd.ddddd		25.06367
# ddd,mm.mmm	25,03.820
# ddd,mm,ss.s	25,03,49.2

#	convert("25.06367");
#	say '-' x 20;
#	convert("25,03.820");
#	say '-' x 20;
#	convert("25,03,49.2");
}

main;
