# makefile to build tester programs

CC=gcc
CFLAGS=-O3 -I../

all: sendtest testopt

sendtest:
	@echo build $@
	$(CC) $(CFLAGS) -o $@ sendtest.c

testopt:
	@echo build $@
	$(CC) $(CFLAGS) -o $@ testopt.c

clean:
	rm -f *.o sendtest testopt

