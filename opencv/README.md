# readme

On my dev environment, multiple openCV are installed.
One is built-from-source with opencv_contrib. The other is pre-compiled from
Intel (openVINO).

At **CMakeLists.txt** you may setup following commands:

1. you may use the current environment and without setting **CMakeLists.txt**

2. specify opencv cmake config dir:

> opencv from **/usr/local/**

```cmake
set(OpenCV_DIR    "/usr/local/share/OpenCV")
```

> opencv from **Intel OpenVINO**
```cmake
set(OpenCV_DIR    "/opt/intel/opencv/share/OpenCV")
```

3. Recommend that add this into **CMakeLists.txt**
```cmake
include_directories(${OpenCV_INCLUDE_DIRS})
```

It will avoid some include file conflicts, because version differs for self-
compiled and intel-pre-compiled.
