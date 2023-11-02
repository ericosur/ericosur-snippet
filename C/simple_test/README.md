# readme

Standalone and simple test cpp could be stored in this folder.
Add a line of **add_executable()** in CMakeLists.txt to build a new sample.

```
$ mkdir -p build && cd build && cmake ..
```

if no error, may issue
```
$ make
```
to build them all

## hello_world

simple "hello world" to show:
  - a extenal instance will be run before main()
  - simple nlomann::json usage

## UTF-8-test.txt

[UTF-8-test.txt](./UTF-8-test.txt) downloads from:
https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
