all: icv


icv:	try_iconv.cpp
	g++ -o $@ $< -liconv

clean:
	rm -f *.o icv
