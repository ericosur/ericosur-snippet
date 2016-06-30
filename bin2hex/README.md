bin2hex
=======

Usage
-----

```
perl bin2hex.pl <input_binary_file> <language_id>
```
result will be output to stdout

language_id could be:

* 0: Perl or similar language(default)
* 1: C / C++ / Java or similar language
* 2: Pascal / Delphi or similar language

Generate binary data to test
----------------------------

Generate a 128-byte binary file with random bytes

```
dd if=/dev/random of=example.bin bs=128 count
```

Demo
----

Remove all output files

```
make clean
```

Run the script
```
make
```
