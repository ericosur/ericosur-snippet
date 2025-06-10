# note

* reference from: https://stackoverflow.com/questions/29979539/how-can-i-make-numpy-use-openblas-in-ubuntu

```
$ update-alternatives --config libblas.so.3
```

* https://github.com/xianyi/OpenBLAS/wiki/faq#debianlts

* [http://bit.ly/2GMbQIq](https://www.r-bloggers.com/for-faster-r-use-openblas-instead-better-than-atlas-trivial-to-switch-to-on-ubuntu/)


## benchmark

use /usr/bin/python to execute test.py
```
rasmus@oa18:~/src/snippet/python/blas$ time /usr/bin/python test.py
real    0m40.263s
user    2m9.850s
sys 0m8.798s
```

```
intel python
real    0m38.567s
user    1m8.258s
sys 0m4.748s
```