is_alac
=======

A simple stupid utility function to test if specified file is a
ALAC (Apple Lossless Audio Codec) file. It does not use any code from
[Apple][2] or 3rd party. It uses stdio and string to identify header tag
within media file.

The original idea comes from: [stackoverflow][1]

---------------------------------------

## test

```
$ ./test_by_list.sh
````

## Generate test data

There are three test files at the source directory. I extracted header
512 bytes from media files.

```
$ head -c 512 song.m4a > song512header.m4a
```

They are not really media you could play, just for testing.

  * [aac.m4a](./aac.m4a) is a lossy AAC media.
  * [alac.m4a](./alac.m4a) is a ALAC media.
  * [flac.flac](./flac.m4a) is a FLAC media.


---------------------------------------
[1]: http://stackoverflow.com/questions/10934936/determine-whether-an-audio-file-is-encoded-in-apple-lossless-alac

[2]: https://macosforge.github.io/alac/

## dependency

Now isAlac depends on libpbox.so (https://github.com/ericosur/ccbox/pbox/)

## backup

old Makefile content moved to here, now use cmake to build

```
CFLAGS=-Wall -O3
PROGS=isAlac

all: $(PROGS)

isAlac: is_alac.cpp
    gcc $(CFLAGS) -o $@ $<

clean:
    rm -f $(PROGS) *.o
```
