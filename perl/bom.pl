#!/usr/bin/perl
=pod

=head NOTE

add, remove BOM

=cut

use strict;

my $bom = pack("CCC",0xef,0xbb,0xbf);

sub remove_bom($)
{
	my $str = shift;
   if (substr($str, 0, 3) == $bom) {
       $str = substr($str, 3);
   }
   return $str;
}

sub has_bom($)
{
	my $str = shift;

	if ($str =~ m/\xef\xbb\xbf/)  {
	#if (substr($str, 0, 3) == pack("CCC",0xef,0xbb,0xbf)) {
		return 1;
	}
	return 0;
}

sub main
{
	my @files = ();
	my $buffer;

	if (@ARGV)  {
		@files = (@ARGV);
	}
	else  {
		@files = glob('*.pl');
	}
	foreach my $ff (@files)  {
		open my $ifh, $ff or die;
		$buffer = <$ifh>;
		#binmode $ifh;
		#my $rv = read($ifh, $buffer, 16);
		close $ifh;
		if (has_bom($buffer))  {
			print "$ff: has BOM\n";
		}
	}
}

main;

__END__

<?php
function writeUTF8File($filename,$content)
{
    $f = fopen($filename, 'w');
    fwrite($f, pack("CCC", 0xef,0xbb,0xbf));
    fwrite($f,$content);
    fclose($f);
}
?>

<?php
function removeBOM($str = '')
{
   if (substr($str, 0,3) == pack("CCC",0xef,0xbb,0xbf)) {
       $str = substr($str, 3);
   }
   return $str;
}
?>

由此上述 BOM = pack("CCC",0xef,0xbb,0xbf), 所以移除 BOM 的寫法可用上面的 removeBOM function 或 下述其一:

    * str_replace("\xef\xbb\xbf", '', $bom_content);
    * preg_replace("/^\xef\xbb\xbf/", '', $bom_content);

另外看到 判斷此字串是不是 UTF-8 的 function:

    function isUTF8($string)
    {
        return (utf8_encode(utf8_decode($string)) == $string);
    }
