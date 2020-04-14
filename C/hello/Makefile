# CC=gcc
# CXX=g++
CC=clang
CXX=clang++

all: hello

MYFLAG=-Wall -O3

hello: crt base child
	$(CXX) $(MYFLAG) -o $@ hello.o HelloBase.o HelloChild.o

crt:	hello.cpp
	$(CXX) $(MYFLAG) -c hello.cpp

base:	HelloBase.cpp HelloBase.h
	$(CXX) $(MYFLAG) -c HelloBase.cpp

child:	HelloChild.cpp HelloChild.h
	$(CXX) $(MYFLAG) -c HelloChild.cpp

clean:
	rm -f *.o hello
