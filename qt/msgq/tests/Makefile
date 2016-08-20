# makefile to build tester programs

CC=gcc
STRIP=strip
CFLAGS=-O3 -Wall -I../
TARGET=testopt foo

all: $(TARGET)

sendtest:    sendtest.c
	@echo build $@
	$(CC) $(CFLAGS) -o $@ sendtest.c
	$(STRIP) $@

%: %.c
	$(CC) -O3 -Wall $(shell pkg-config --cflags libconfig) \
	-o $@ $< $(shell pkg-config --libs libconfig)

clean:
	rm -f *.o $(TARGET)
