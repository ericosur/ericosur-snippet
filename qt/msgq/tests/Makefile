# makefile to build tester programs

CC=gcc
STRIP=strip
CFLAGS=-O3 -I../

all: sendtest testopt

sendtest:    sendtest.c
	@echo build $@
	$(CC) $(CFLAGS) -o $@ sendtest.c
	$(STRIP) $@

testopt:    testopt.c
	@echo build $@
	$(CC) $(CFLAGS) -o $@ testopt.c
	$(STRIP) $@

clean:
	rm -f *.o sendtest testopt

