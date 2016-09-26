CFLAGS=-Wall -O3
PROGS=isAlac

all: $(PROGS)

isAlac: is_alac.cpp
	gcc $(CFLAGS) -o $@ $<

clean:
	rm -f $(PROGS) *.o
