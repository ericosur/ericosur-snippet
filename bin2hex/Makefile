all: demo

example.bin:
	dd if=/dev/random of=example.bin bs=128 count=1

demo: example.bin
	perl bin2hex.pl $< 1 > $@.c

clean:
	rm -f demo.c example.bin
