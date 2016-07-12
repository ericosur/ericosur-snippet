all: logc logj

logc: log.c
	gcc -O3 -Wall -o $@ $< -lm

logj: log.java
	javac $<

clean:
	rm -f *.o *.pyc *.class logc
