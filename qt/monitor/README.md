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

now monitor is running and no foo running,
and then run foo again:
```
$ ./foo &
```

I assume that __monitor__ is long-live and more stable than __foo__.
It is not handled if __foo__ and __monitor__ are both running, and then
__monitor__ crashed, and __monitor__ is restarted. Due to __foo__ will not
send "foo starts" notification to __monitor__, __monitor__ would not
check **flock** of _foo.pid_. The state of __foo__ will be out of sync.

