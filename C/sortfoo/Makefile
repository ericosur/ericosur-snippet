# simple stupid makefile

SRCFILE = sortfoo.cpp
CXXFLAGS += -Wall -O3 -std=c++11

all: app

app: ${SRCFILE}
	g++ ${CXXFLAGS} -o app $<

clean:
	rm -f *.o app

