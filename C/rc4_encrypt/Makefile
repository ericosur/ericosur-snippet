all:    myenc mydec hdr

mymd:	md5main.o ToolBox.o
	gcc -o mymd md5main.o ToolBox.o -lcrypto -lstdc++

myrc:   rc4main.o ToolBox.o
	gcc -o myrc rc4main.o ToolBox.o -lcrypto -lstdc++

myenc:	myenc.o ToolBox.o
	gcc -o myenc myenc.o ToolBox.o -lcrypto -lstdc++

mydec:	mydec.o ToolBox.o
	gcc -o mydec mydec.o ToolBox.o -lcrypto -lstdc++

hdr:   ReadHeader.o
	gcc -o hdr ReadHeader.o ToolBox.o -lcrypto -lstdc++


clean:
	rm -f *.o
