#!/usr/bin/perl
use strict;
use warnings;


my $file = "ana_result.txt";
my @lines;

if (-f $file)
{
	open FH, $file or die;
	@lines = <FH>;
	close FH;
}
else
{
	@lines = <DATA>;
}

my $total = 0;
my $count = 0;
my %hash = ();


for (@lines)
{
	m/(.*): (\d+)/;
#	print $1,"\t",$2,"\n";

	my ($model, $cnt) = ($1, $2);
	$model =~ s/\s+$//;

	$hash{$model} = $cnt;
	$total += $cnt;
	++ $count;
}

die if ($total == 0);



#
# sort hash by "keys"
#
#foreach my $key (sort (keys(%hash)))
#{
#	printf "%25s: %f\n",
#		$key,							# model name
#		($hash{$key}/$total*100.0);		# ratio
#}


#
# sort hash by "values"
#
foreach my $key (sort hashValueDescendingNum (keys(%hash)))
{
	printf "%30s: %f\n",
		$key,							# model name
		($hash{$key}/$total*100.0);		# ratio
}



#----------------------------------------------------------------------#
#  FUNCTION:  hashValueDescendingNum                                   #
#                                                                      #
#  PURPOSE:   Help sort a hash by the hash 'value', not the 'key'.     #
#             Values are returned in descending numeric order          #
#             (highest to lowest).                                     #
#----------------------------------------------------------------------#
sub hashValueDescendingNum
{
   $hash{$b} <=> $hash{$a};
}


__DATA__
E995: 8
Canon PowerShot G5: 64
DSC-P100: 14
NIKON D100 : 12
FinePix F402  : 1
Canon DIGITAL IXUS v: 2
Canon PowerShot G3: 24
MX-700: 276
E5000: 4
Canon PowerShot A200: 320
E5700: 12
QV-3000EX: 20
EX-Z4  : 90
SP-2000: 14
QV-4000  : 4
FinePix S602 ZOOM: 2
Canon EOS 350D DIGITAL: 1150
E775: 1
DSC-P8: 10
Canon PowerShot G1: 54
DSC-V1: 1449
Canon PowerShot S10: 8
Canon EOS 300D DIGITAL: 14496
FinePix40i: 2
FinePix F601 ZOOM: 6
J1  : 113
E3100: 1190
DSC-MZ3 : 20
Canon PowerShot G2: 4142
HP PhotoSmart 315: 449
CLIE: 14
Canon EOS 10D: 2
EX-Z750: 40
FinePix S304  : 2
C730UZ: 4
Canon EOS DIGITAL REBEL: 90
Canon PowerShot S30: 22
Canon EOS Kiss Digital N: 927
C2100UZ: 2
DiMAGE F100: 38
E4500: 527
QSS-32_33: 251
Canon DIGITAL IXUS v3: 5
CYBERSHOT: 318
KODAK DX3500 DIGITAL CAMERA: 2
DMC-LC5: 4
DMC-F1: 3
NIKON D70: 776
E5900: 38
SIGMA SD9: 2
Canon PowerShot A80: 43
1.3M Digital CAM: 88
PENTAX Optio 330GS : 12
CP-80Z: 18
Canon EOS D30: 16
EX-Z57 : 95
Canon PowerShot S45: 4
FinePixS2Pro: 2
EX-Z55 : 1850
E885: 4
DMC-LC40: 8
Canon PowerShot A70: 7
1.0: 36
