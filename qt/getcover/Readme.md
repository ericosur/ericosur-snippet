Comparision Table
-----------------

| item | description |
| ---- | ----------- |
| Input file | alice.mp3 |
| size | 24,032,119 bytes |
| embedded jpeg | DSC01769.jpg |
| size | 8,192,000 bytes |


```
$ identify DSC01769.jpg
DSC01769.jpg JPEG 4912x3264 4912x3264+0+0 8-bit sRGB 8.192MB 0.040u 0:00.039
```

At x222 machine, file read from SSD, write to tmpfs

At rpi2 machine, file read from microSD, write to tmpfs

| Machine    | Method     | Time Usage  | multipler to better case |
| ---------- |:---------- |------------:|----------:|
| x222       | jpg to png | 6.581s      | 7.061x |
| x222       | jpg to jpg | 0.932s      | 1.000x |
| rpi2       | jpg to png | 54.545s     | 12.828x |
| rpi2       | jpg to jpg | 4.252s      | 1.000x |


###Test Log if Follow Thumbnail Image Format or not###


#### if jpeg thumbnail, save to png ####
```bash
rm /tmp/*.png
time ./getcover -t alice.mp3
identify /tmp/*.png
```
```
[23:15:40.226] [I] use thumbnail hash table? no
[23:15:40.226] [I] get thumbnail for: "alice.mp3"
[23:15:40.235] [I] APIC type: "[image/jpeg]"
[23:15:40.610] [I] pf->picture().size(): 8192000
[23:15:40.735] [I] _img.byteCount(): 64131072
[23:15:46.795] [I] getThumbnail() tbfn: "/tmp/8451db53a9adcee8287c4b638dc61432.png"

/tmp/8451db53a9adcee8287c4b638dc61432.png PNG 4912x3264 4912x3264+0+0 8-bit sRGB 25.14MB 0.000u 0:00.000
```

#### if jpeg thumbnail, save to jpeg ####
```bash
rm /tmp/*.png
time ./getcover -ti alice.mp3
identify /tmp/*.png
```
```
[23:15:46.821] [I] use thumbnail hash table? no
[23:15:46.822] [I] will follow thumbnail image format...
[23:15:46.822] [I] get thumbnail for: "alice.mp3"
[23:15:46.827] [I] APIC type: "[image/jpeg]"
[23:15:47.122] [I] pf->picture().size(): 8192000
[23:15:47.247] [I] _img.byteCount(): 64131072
[23:15:47.748] [I] getThumbnail() tbfn: "/tmp/8451db53a9adcee8287c4b638dc61432.png"

/tmp/8451db53a9adcee8287c4b638dc61432.png JPEG 4912x3264 4912x3264+0+0 8-bit sRGB 2.565MB 0.000u 0:00.000
```

### At Raspbeery Pi 2 ###
#### if jpeg thumbnail, save to png ####
```
[23:17:08.629] [I] use thumbnail hash table? no
[23:17:08.632] [I] get thumbnail for: "alice.mp3"
[23:17:08.672] [I] APIC
                       uCv type: "[image/jpeg]"
[23:17:10.134] [I] pf->picture().size(): 8192000
[23:17:10.881] [I] _img.byteCount(): 64131072
[23:18:03.121] [I] getThumbnail() tbfn: "/tmp/6fc64553c7560f3ff8e606b8fc2213c3.png"

/tmp/6fc64553c7560f3ff8e606b8fc2213c3.png PNG 4912x3264 4912x3264+0+0 8-bit sRGB 25.04MB 0.000u 0:00.000
```

#### if jpeg thumbnail, save to jpeg ####
```
[23:18:03.228] [I] use thumbnail hash table? no
[23:18:03.229] [I] will follow thumbnail image format...
[23:18:03.230] [I] get thumbnail for: "alice.mp3"
[23:18:03.270] [I] APIC
                       �:v type: "[image/jpeg]"
[23:18:04.730] [I] pf->picture().size(): 8192000
[23:18:05.475] [I] _img.byteCount(): 64131072
[23:18:07.440] [I] getThumbnail() tbfn: "/tmp/6fc64553c7560f3ff8e606b8fc2213c3.png"

/tmp/6fc64553c7560f3ff8e606b8fc2213c3.png JPEG 4912x3264 4912x3264+0+0 8-bit sRGB 2.558MB 0.000u 0:00.000
```