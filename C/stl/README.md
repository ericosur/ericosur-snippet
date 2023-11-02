# readme

C++ STL samples.

## simple stupid makefile

```make
SRCFILE = sortfoo.cpp
CXXFLAGS += -Wall -O3 -std=c++11

all: app

app: ${SRCFILE}
    g++ ${CXXFLAGS} -o app $<

clean:
    rm -f *.o app
```

###### tags: ```programming``` ```c++``` ```stl```
