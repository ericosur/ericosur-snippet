MYINC=-I/opt/local/include
CC=clang
CFLAG=-O3 -Wall
TARGET=md5test

all:	$(TARGET)

toolbox:	toolbox.cpp
	$(CC) $(CFLAG)  $(MYINC) -c $<

md5test: toolbox main.cpp
	$(CC) $(CFLAG)  $(MYINC) -o $@ main.cpp toolbox.o -lcrypto -lstdc++

clean:
	rm -f *.o $(TARGET)
