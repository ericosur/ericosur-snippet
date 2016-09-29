all: hello

MYFLAG=-Wall -O3 -g -rdynamic

hello: test.c
	$(CC) $(MYFLAG) -o $@ $<

clean:
	rm -rf *.o $(all) hello.dSYM/
