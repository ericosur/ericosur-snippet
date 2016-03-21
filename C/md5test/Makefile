MYINC=-I/opt/local/include

all:	main

toolbox:
	gcc -O3 -c toolbox.cpp $(MYINC)

main: toolbox
	gcc -O3 -o main main.cpp toolbox.o $(MYINC) -lcrypto -lstdc++

clean:
	rm -f *.o
	rm main
