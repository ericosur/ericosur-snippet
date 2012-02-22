#!/usr/bin/perl

#
#  first script using Image::ExifTool package
#  using ppm to install
#
# 2007/10/29 by ericosur

use Image::ExifTool qw(:Public);

sub get_exif_info($);

sub main
{
	my $result;
	my $file = $ARGV[0] || 'list.txt';

	open my $fh, $file or die "cannot open file $file: $!\n";
	printf STDERR "==> file list from <%s>\n", $file;

	while (<$fh>)  {
		s/\n//;
		$result = get_exif_info($_);
		printf "%s: %s\n", $_, $result if ($result);
	}

	close $fh;
}


sub get_exif_info($)
{
	my $img_file = shift;
	if (not -f $img_file)  {
		print STDERR "<$img_file> not found\n";
		return "";
	}

	my $info = ImageInfo($img_file);
	my $str;
	my ($model, $lens, $apert, $expos, $focal, $iso) = (
		$$info{'Model'},
		$$info{'Lens'},
		$$info{'Aperture'},
		$$info{'ExposureTime'},
		$$info{'FocalLength'},
		$$info{'ISO'}
	);

	my $expcomp = $$info{'ExposureCompensation'};

	$model =~ s/ DIGITAL//g;
	$model =~ s/ *$//g;
	$lens =~ s/ //g;

	return undef if ($model eq undef);

	if ($lens eq undef)  {
		$str = sprintf "%s F%s %ss @%s",
			$model, $apert, $expos, $focal;
		if ($iso ne undef)  {
			$str = $str . ' ISO' . $iso;
		}
	}
	else  {	# for my DSLR
		if (substr($model, "G9"))  {
			$focal *= 4.6;
			$str = sprintf "%s F%s %ss @%smm ISO%s",
				$model, $apert, $expos, $focal, $iso;
			if ($expcomp ne '0')  {
				$str = $str . ' ' . $expcomp . 'ev';
			}
		}
		else  {
			$str = sprintf "%s %s F%s %ss @%s ISO%s",
				$model, $lens, $apert, $expos, $focal, $iso;
			if ($expcomp ne '0')  {
				$str = $str . ' ' . $expcomp . 'ev';
			}
		}
	}

	#print STDERR $str, "\n" if $debug;
	return $str;
}

#foreach (keys %$info) {
#    print "$_ => $$info{$_}\n";
#}

#my @wanted = qw(Model Lens ApertureValue ExposureTime FocalLength ISO );

#foreach (@wanted)
#{
#	printf STDERR "%s => %s\n", $_, $$info{$_};
#}

main();
