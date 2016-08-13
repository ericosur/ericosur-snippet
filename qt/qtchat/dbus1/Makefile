TARGET=ds

all: $(TARGET)

%: %.c
	$(CC) $(shell pkg-config --cflags dbus-1) \
	-o $@ $< $(shell pkg-config --libs dbus-1)

clean:
	rm -f $(TARGET) *.o
