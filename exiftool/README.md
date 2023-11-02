# Readme

use perl module Image::ExifTool to show exif metadata from an image

* official site of Exiftool: https://www.sno.phy.queensu.ca/~phil/exiftool/

## requirements

```
apt-get install libimage-exiftool-perl
```

## usage

reference: https://stackoverflow.com/questions/841785/how-do-i-include-a-perl-module-thats-in-a-different-directory

If Image::Exiftool does not install into perl include path (@INC), use

```perl

BEGIN {push @INC, '/bs2/Image-ExifTool-12.69/lib'}

```

at the front of perl script, it could __use__ or "import" such module.
