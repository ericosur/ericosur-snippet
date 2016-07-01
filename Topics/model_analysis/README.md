Model Analysis
==============

To know how many picture taken by which camera/manufacturer.

Pre-requirement
---------------

need external perl module

  ```perl
  use Image::ExifTool
  ```

How to use
----------

1. use the following command to generate list file

  ```
  dir /s /b /a-d *.jpg > list.txt
  ```

2. input: list.txt, output: model.txt
  ```
  perl get_exif_model.pl
  ```

3. intput model.txt
  ```
  perl ana_model.pl
  ```
