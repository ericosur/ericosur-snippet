# makefile to build tester programs

CC=gcc
STRIP=strip
CFLAGS=-O3 -Wall -I../
TARGET=testopt

all: $(TARGET)

sendtest:    sendtest.c
	@echo build $@
	$(CC) $(CFLAGS) -o $@ sendtest.c
	$(STRIP) $@

testopt:    testopt.c
	@echo build $@
	$(CC) -O3 -Wall -o $@ testopt.c
	$(STRIP) $@

clean:
	rm -f *.o sendtest testopt
