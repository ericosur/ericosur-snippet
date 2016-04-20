#MYLIB=-L/opt/local/lib
MYLIB=-L/opt/local/lib -lprotobuf
MYINC=-I/opt/local/include
TARGET=pinput pread

all: $(TARGET)

pinput:	input.cpp address.pb.o
	g++ -Wall -O3 $(MYINC) -o $@  input.cpp address.pb.o  $(MYLIB)

pread:	read.cpp address.pb.o
	g++ -Wall -O3 $(MYINC) -o $@  read.cpp address.pb.o  $(MYLIB)

address.pb.o:	address.proto
	protoc -I=./ --cpp_out=./ ./address.proto
	g++ -Wall -O3 -c $(MYINC) -o $@ address.pb.cc

clean:
	rm -f *.o $(TARGET)
