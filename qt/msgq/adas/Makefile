# makefile to build tester programs

CC=gcc
STRIP=strip
MFLAGS=-O3 -Wall

all: adasmsgq.o adastx adasrx testadas

adasmsgq.o:	adasmsgq.h adasmsgq.c
	@echo build ADAS MSGQ
	$(CC) $(MFLAGS) -c adasmsgq.c

adastx:	adasmsgq.h adastx.c adasmsgq.o
	@echo build TX
	$(CC) $(MFLAGS) -o $@ adasmsgq.o adastx.c

adasrx:	adasmsgq.h adasrx.c adasmsgq.o
	@echo build RX
	$(CC) $(MFLAGS) -o $@ adasmsgq.o adasrx.c

testadas:	testadas.c adasmsgq.h
	@echo build testadas...
	$(CC) $(MFLAGS) -o $@ adasmsgq.o testadas.c

clean:
	rm -f *.o adastx adasrx testadas
