const member example
====================

* see [foo.h](./foo.h) for details
* [c11.cpp](./c11.cpp) use c++11 features
* [c14.cpp](./c14/c14.cpp) use c++14 features, need newer compiler to build
* [rl.c](./readln/rl.c) need library readline, maybe a missed library some cross-compiler environment

CMake Configurations
--------------------

There are several tool chain settings to use cmake
for cross compiling.

* [arm201405.txt](./arm201405.txt) for Sourcery CodeBench Lite 2014.05-29
* [armlinux.txt](./armlinux.txt) for package g++-5-arm-linux-gnueabi and gcc-5-arm-linux-gnueabi
* [poky.txt](./poky.txt) for using yocto codebase built toolchain

Note
----
Old style Makefile is removed.
