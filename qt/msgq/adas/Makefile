# makefile to build tester programs

CC=gcc
STRIP=strip
CFLAGS=-O3 -Wall

all: adastx adasrx

libadasmsgq.a:	adasmsgq.h adasmsgq.c
	@echo build libadasmsgq.a
	$(CC) $(CFLAGS) -c adasmsgq.c
	$(AR) crv -o $@ adasmsgq.o

adastx:	adasmsgq.h libadasmsgq.a adastx.c
	@echo build TX
	$(CC) $(CFLAGS) -o $@ adastx.c -ladasmsgq -L.

adasrx:	adasmsgq.h libadasmsgq.a adasrx.c
	@echo build RX
	$(CC) $(CFLAGS) -o $@ adasrx.c -ladasmsgq -L.

testadas:	adasmsgq.h libadasmsgq.a testadas.c
	@echo build testadas...
	$(CC) $(CFLAGS) -o $@ testadas.c -ladasmsgq -L.

clean:
	rm -f *.o adastx adasrx testadas libadasmsgq.a

