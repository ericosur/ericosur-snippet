all: hello

MYFLAG=-Wall -O3

hello: crt base child
	g++ $(MYFLAG) -o $@ hello.o HelloBase.o HelloChild.o

crt:	hello.cpp
	g++ $(MYFLAG) -c hello.cpp

base:	HelloBase.cpp HelloBase.h
	g++ $(MYFLAG) -c HelloBase.cpp

child:	HelloChild.cpp HelloChild.h
	g++ $(MYFLAG) -c HelloChild.cpp

clean:
	rm -f *.o hello
