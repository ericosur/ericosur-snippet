APPNAME = app
OBJECTS = main.o
TARGET = $(OBJECTS)

CC = gcc
CXX = g++
CXXFLAGS = -O3 -Wall -std=gnu++11

all: $(TARGET)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(APPNAME) -lstdc++

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf *.o $(APPNAME)

