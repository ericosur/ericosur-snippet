TARGET=main c11 c14
FLAGS=-Wall -O3
BASIC=$(FLAGS) -std=c++11

all: $(TARGET)

main: main.cpp myinc.cpp foo.h
	g++ $(BASIC) -c myinc.cpp
	g++ $(BASIC) -c main.cpp
	g++ $(BASIC) -o $@ main.o myinc.o

c11: c11.cpp
	g++ $(BASIC) -o $@ $<

c14: c14.cpp
	g++ $(FLAGS) -std=c++14 -o $@ $<

clean:
	rm -f *.o $(TARGET)
