# readme

## howto build

Makefile is old for reference only.
Please use cmake to build.

* default gcc:

```
$ mkdir -p build && cd build
$ cmake ..
$ make
```

* using icc:

```
$ source /opt/intel/system_studio_2018/bin/compilervars.sh \
      -arch intel64 -platform linux
$ cmake -DINTEL=1 ..
$ make
```

* using clang:
  * add clang toolchain into path

```
$ clang -O3 -Wall -o bubble bubblesort.c loadutil.c
$ arm-none-linux-gnueabi-gcc -O3 -Wall -o bubble bubblesort.c loadutil.c
```


## benchmark

To test bubblesort, it will read data from __rand.dat__

How to generate with random numbers:
```
$ dd if=/dev/urandom of=rand.dat bs=2048 count=400
```

hardware of **kitty** is Intel Core i7-2600K
hardware of **oa18** is Intel Core i3-6100U
hardware of **rpi3** is arm7l

| hardware | sort algorithm | gcc | icc | clang | arm-none-linux-gnueabi-gcc |
|----------|----------------|-----|-----|-------|----------------------------|
| oa18     | bubblesort | 44.627s | 20.068s | 18.014s | n/a |
| kitty    | bubblesort | 10.890s | 10.107s | 8.883s | n/a |
| rpi3     | bubblesort | 36.699s | n/a | 1m3.079s | 35.911s |

