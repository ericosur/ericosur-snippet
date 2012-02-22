use strict;
use Storable;

sub show_scr($$)
{
	my ($ff, $hh) = @_;
	printf "file: %s:\n", $ff;
	foreach ( sort keys %$hh)  {
		printf "%s => %d\n", $_, ${$hh}{$_};
	}
}

my $ifile = 'list.txt';
#my @list = `cmd /c dir /s /b *.c`;
my $count = 0;
my %scr = ();

open LIST, $ifile or die;

#foreach (@list)  {
while (<LIST>)  {
	s/[\r\n]//g;
	++ $count;
	open my $ifh, $_ or die;
	my $ff = $_;
#	%scr = ();
	while (<$ifh>)  {
		if ( m/ShowCategory(\d+)Screen/ )  {
			$scr{$1} ++;
		}
	}
	close $ifh;
#	last;
}

close LIST;

printf "total %d files\n", $count;
show_scr("total", \%scr);

print "store hash 'scr' into 'result.dat\n";
store(\%scr, "result.dat");
