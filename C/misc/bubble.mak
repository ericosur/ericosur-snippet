CXXFLAGS = -Wall -O3 -std=c++11
CFLAGS = -Wall -O3
#CXX=g++
#CC=gcc
TARGET=bubblesort

CXX=clang++
CC=clang

all: bubblesort

%.o: %.c %.h
	$(CC) $(CFLAGS) -o $@ -c $<

bubblesort: bubblesort.o loadutil.o
	$(CC) $(CFLAGS) bubblesort.o loadutil.o -o $@

rand: rand.dat
	dd if=/dev/urandom of=$< bs=2048 count=400

clean:
	rm -f *.o $(TARGET)
