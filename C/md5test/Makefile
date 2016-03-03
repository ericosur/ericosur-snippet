all:	main

toolbox:
	gcc -O3 -c toolbox.cpp

main: toolbox
	gcc -O3 -o main main.cpp toolbox.o -lcrypto -lstdc++

clean:
	rm -f *.o
	rm main
