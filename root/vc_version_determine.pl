#!/usr/bin/perl -w

#
# copy from http://www.jeffhung.net/blog/articles/jeffhung/89/
# written by JeffHung
#

use File::Spec::Functions;
use Data::Dump qw(dump);

die "only for win32" if $^O ne "MSWin32";

sub file_version
{
    my $file = shift or die;
    use if $^O eq "MSWin32", "Win32::File::VersionInfo";
    my $vinfo = GetFileVersionInfo($file);
    if ($vinfo) {
        return $vinfo->{'FileVersion'};
    }
    return undef;
}

my $vc6_dir = catfile($ENV{'ProgramFiles'}, 'Microsoft Visual Studio', 'VC98');
my $vc6_versions = {
#    ....
    'vc6-sp5' => {
        catfile($vc6_dir, 'Bin', 'C1.DLL')     => '12.0.8867.0',
        catfile($vc6_dir, 'Bin', 'C1XX.DLL')   => '12.0.8961.0',
        catfile($vc6_dir, 'Bin', 'CL.EXE')     => '12.0.8804.0',
        catfile($vc6_dir, 'Bin', 'LINK.EXE')   =>  '6.0.8447.0',
        catfile($vc6_dir, 'Bin', 'CVTRES.EXE') =>  '5.0.1736.1',
    },
    'vc6-sp6' => {
        catfile($vc6_dir, 'Bin', 'C1.DLL')     => '12.0.9782.0',
        catfile($vc6_dir, 'Bin', 'C1XX.DLL')   => '12.0.9782.0',
        catfile($vc6_dir, 'Bin', 'CL.EXE')     => '12.0.8804.0',
        catfile($vc6_dir, 'Bin', 'LINK.EXE')   =>  '6.0.8447.0',
        catfile($vc6_dir, 'Bin', 'CVTRES.EXE') =>  '5.0.1736.1',
    },
};

foreach my $version (sort keys %$vc6_versions) {
    my $is_this_version = 1;
    foreach my $file (sort keys %{$vc6_versions->{$version}}) {
        my $fv = file_version($file);
        if (!defined($fv)) {
            $is_this_version = 0;
            last; # foreach ($file)
        }
        if ($fv ne $vc6_versions->{$version}->{$file}) {
            $is_this_version = 0;
            last; # foreach ($file)
        }
    }
    if ($is_this_version) {
        print "$version\n";
        exit;
    }
}
print "vc6\n";

