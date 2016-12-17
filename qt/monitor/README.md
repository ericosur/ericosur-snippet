foo & monitor
=============

How to monitor a process if it is running without polling it.

More details:
[[common] howto monitor a process without polling](https://docs.google.com/presentation/d/18jTjhWgQmHFkkOq7tb0dgMM-W2rpgt52zqf7BYSn6XE/edit#slide=id.p)

How to test
-----------

steps:

run foo first:
```
$ ./foo &
$ ./monitor &
$ killall foo
```

now monitor is running and no foo:
```
$ ./foo &
```


