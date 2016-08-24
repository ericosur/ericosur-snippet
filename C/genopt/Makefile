APPNAME = app
OBJECTS = main.o cmdline.o
TARGET = cmdline.c $(OBJECTS)

CC = gcc
CXX = g++
CFLAGS = -O3 -Wall

all: $(TARGET)
	$(CXX) $(CFLAGS) $(OBJECTS) -o $(APPNAME) -lstdc++

cmdline.o: cmdline.c
	$(CC) $(CFLAGS) -c $< -o $@

main.o: main.cpp
	$(CXX) $(CFLAGS) -c $< -o $@

cmdline.c: sample.ggo
	gengetopt --input=$< --include-getopt

clean:
	rm -rf *.o $(APPNAME) cmdline.*

