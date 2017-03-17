CXXFLAGS = -Wall -O2 -std=c++11 $(shell pkg-config --cflags sdl2)
CFLAGS = -Wall -O2 $(shell pkg-config --cflags sdl2)
LIBS = $(shell pkg-config --libs sdl2)
CXX=g++
CC=gcc
TARGET=first

all: $(TARGET)

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $< $(LIBS)

%: %.c
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

clean:
	rm -f *.o $(TARGET)
