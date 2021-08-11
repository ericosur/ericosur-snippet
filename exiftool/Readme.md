# Readme

use perl module Image::ExifTool to show exif metadata from an image

* official site of Exiftool: https://www.sno.phy.queensu.ca/~phil/exiftool/

## usage

If Image::Exiftool does not install into perl include path (@INC), use

```perl

BEGIN {push @INC, '/bs2/Image-ExifTool-12.29/lib'}

```

at the front of perl script, it could __use__ or "import" such module.
