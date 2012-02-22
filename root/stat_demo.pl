#!/usr/bin/perl
#
# simple demo for stat()
#

$filename = $ARGV[0] || $0;

    ($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,
       $atime,$mtime,$ctime,$blksize,$blocks)
           = stat($filename);

print "$filename ===>\n",
	"dev($dev), inode($ino), mode($mode), nlink($nlink), \n",
	"uid($uid), gid($gid), rdev($rdev), size($size), \n",
	"atime($atime), mtime($mtime), ctime($ctime), \n",
	"blocksize($blksize), blocks($blocks)\n";
