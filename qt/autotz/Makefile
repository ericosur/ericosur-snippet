
CFLAGS=-O3 -pedantic -Wall -I"."

all:	autotz

autotz:
	$(CC) $(CFLAGS) -o autotz autotz.cpp  -lm -lc -lstdc++
# clang -O3 -Wall -o autotz autotz.cpp  -lm -lstdc++
clean:
	rm -f *.o
	rm -f autotz
