APPS = \
	pipeline \
	reqrep \
	pair \
	pubsub \
	survey \
	bus \
	tx \
	rx \
	mypub

CFLAGS = -O3 -Wall
LFLAGS = -lnanomsg

all: $(APPS)

pipeline: pipeline.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

reqrep: reqrep.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

pair: pair.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

pubsub: pubsub.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

survey: survey.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

bus: bus.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

tx: tx.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

rx: rx.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

mypub: mypub.c
	gcc $(CFLAGS) -o $@ $< $(LFLAGS)

style:
	astyle --style=kr --indent=spaces=4 \
		--pad-oper \
		--add-brackets \
		*.c

clean:
	rm -f *.o $(APPS)
