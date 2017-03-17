CXXFLAGS = -Wall -O2 -std=c++11
CFLAGS = -Wall -O2
CXX=g++
CC=gcc
TARGET=anon stdc pi

all: $(TARGET)

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o $(TARGET)
