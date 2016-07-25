FLAGS=-Wall -O3

all: main

main: main.cpp myinc foo.h
	g++ $(FLAGS) -c main.cpp
	g++ $(FLAGS) -o $@ main.o myinc.o

myinc: myinc.cpp myinc.h
	g++ $(FLAGS) -c myinc.cpp

clean:
	rm -f *.o main
