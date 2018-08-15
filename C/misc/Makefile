CXXFLAGS = -Wall -O3 -std=c++11
CFLAGS = -Wall -O3
CXX=g++
CC=gcc

CTARGET=bubblesort pi ptz seeif
CPPTARGET=anon stdc
TARGET=$(CTARGET) $(CPPTARGET)

all: $(TARGET)

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o $(TARGET)
