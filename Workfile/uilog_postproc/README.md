Handy Scripts to Post-Process Log
=================================

[elsp.pl](./elsp.pl) and [minus_base.pl](./minus_base.pl) are
handy scripts to convert absolute time stamp into relative
epoch numbers.

Usage
-----

Just use stdin/stdout.

```
cat abc.log | ./elsp.pl | minus_base.pl
```

------------------------------------------------------------

Original abc.log:
```
[21:00:06.808] W: yoseui starting...
[21:00:06.930] D: [ 1 ] class: "YoseDbus" : register path: "/hu/MainUi" result: ok
[21:00:06.931] D: [ 2 ] class: "YoseDbusMusic" : register path: "/hu/MainUi/LocalMusic" result: ok
[21:00:06.932] D: [ 3 ] class: "YoseDbusA2dp" : register path: "/hu/MainUi/BtA2dp" result: ok
[21:00:06.938] D: [ 4 ] class: "YoseDbusBluetooth" : register path: "/hu/MainUi/Bluetooth" result: ok
```

after [elsp.pl](./elsp.pl) processed:

```
[75606.808] W: yoseui starting...
[75606.930] D: [ 1 ] class: "YoseDbus" : register path: "/hu/MainUi" result: ok
[75606.931] D: [ 2 ] class: "YoseDbusMusic" : register path: "/hu/MainUi/LocalMusic" result: ok
[75606.932] D: [ 3 ] class: "YoseDbusA2dp" : register path: "/hu/MainUi/BtA2dp" result: ok
[75606.938] D: [ 4 ] class: "YoseDbusBluetooth" : register path: "/hu/MainUi/Bluetooth" result: ok
```

and then [minus_base.pl](./minus_base.pl) processed:

```
[0.000] W: yoseui starting...
[0.122] D: [ 1 ] class: "YoseDbus" : register path: "/hu/MainUi" result: ok
[0.123] D: [ 2 ] class: "YoseDbusMusic" : register path: "/hu/MainUi/LocalMusic" result: ok
[0.124] D: [ 3 ] class: "YoseDbusA2dp" : register path: "/hu/MainUi/BtA2dp" result: ok
[0.130] D: [ 4 ] class: "YoseDbusBluetooth" : register path: "/hu/MainUi/Bluetooth" result: ok
```

