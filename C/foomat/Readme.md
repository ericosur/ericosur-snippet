# readme for foomat

a simple stupid matrix cross calculation

## benchmark on kitty.local


| hardware | compiler | time usage |
|----------|----------|------------|
| kitty    | gcc      | 10.275s    |
| kitty    | icc      | 17.499s    |
| kitty    | clang    | 17.090s    |
| oa18     | gcc      | 125.573s   |
| oa18     | icc      | 20.366s    |
| rpi3     |


## how to use ICC

```
source /opt/intel/system_studio_2018/bin/compilervars.sh \
      -arch intel64 -platform linux
```

```
cmake -DINTEL=1 ..
```

## using clang

```
clang++ -o foo -O3 main.cpp mymat.cpp
```
