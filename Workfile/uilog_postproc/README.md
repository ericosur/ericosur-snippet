Handy Scripts to Post-Process Log
=================================

[TOC]

## part1

[elsp.pl](./elsp.pl) and [minus_base.pl](./minus_base.pl) are
handy scripts to convert absolute time stamp into relative
epoch numbers.

### Usage

Just use stdin/stdout.

```
cat abc.log | ./elsp.pl | minus_base.pl
```

Resut as:

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

## part2

[normalize.pl](./normalize.pl) provides an easier way to merge two logs into one, and sync'ed their timestamp as epoce.

### invoke

prepare **ipod.log** and **ipodsdk.log** 
then run:
```
$ perl normalize.pl
```
output file would be **merged.log**

merged log looks like:
```
[20618005][ipod] [05:43:38.005][ipodui][1240] D: sltWaitBtFinished enables PLM
[20618005][ipod] version --- 2 2
[20618007][sdk] 04-17 05:43:38.007:W: 
[20618007][sdk] == Set iPod Enable ==
[20618032][sdk] 04-17 05:43:38.032:D: dev found
[20618098][sdk] 04-17 05:43:38.098:I: iPodUsb add
[20618188][sdk] 04-17 05:43:38.188:D: iPodSDK UsbAttach +
[20618189][sdk] 04-17 05:43:38.189:D: MonitorInboudTraffic +
[20618189][sdk] 04-17 05:43:38.189:D: iPodSDK UsbAttach -
[20618189][sdk] 04-17 05:43:38.189:D: iAP2SendDetectCB=0
[20618254][sdk] 04-17 05:43:38.254:I: iAP2ConnectedCB=1
[20618259][sdk] 04-17 05:43:38.259:D: MFi auth copy 908
[20618265][sdk] 04-17 05:43:38.265:D: ChallengeData 20
[20618439][sdk] 04-17 05:43:38.439:D: PlaylistAttachCb 1+
[20618439][ipod] [05:43:38.439][ipodui][1240] W: device attached...
[20618440][ipod] [05:43:38.440][ libhu][WARN] +++request svc id is [SVC_HMI_IPOD]
[20618440][ipod] [05:43:38.440][ libhu][WARN] +++cur hmi is [SVC_HMI_IPOD]
[20618440][ipod] [05:43:38.440][ libhu][WARN] +++skip, hmi in foreground
[20618440][ipod] [05:43:38.440][ipodui][1240] D: void MainWindow::init_ipod_db()
[20618441][ipod] [05:43:38.441][ipodui][1240] D: PageRootBase: switch to ipod page...
```