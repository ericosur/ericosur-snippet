# use cross compiler to build busybox

add path:
```
export PATH=$HOME/arm2014.05/bin:$PATH
make menuconfig
```

* busybox settings:
    * Settings -> Build Options
        - Build static binary (no shared libs)
        - Cross compiler prefix: arm-none-linux-gnueabi-

    * remove some extra applets from settings
