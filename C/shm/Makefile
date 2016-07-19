CFLAGS=-Wall -O3
PROGS=\
	proc1 \
	proc2

all: $(PROGS)

# crt: shm_create.c
# 	gcc $(CFLAGS) -o $@ $<

proc1: proc1.c shmem.h
	gcc $(CFLAGS) -o $@ $<

proc2: proc2.c shmem.h
	gcc $(CFLAGS) -o $@ $<

clean:
	rm -f $(PROGS) *.o
