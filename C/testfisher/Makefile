all: clean fisher

fisher: fisher.cpp
	gcc -O3 -Wall -o $@ $<

clean:
	rm -f fisher *.o fisher*.log
