.phony: all

all: weather.json tjout.json

weather.json: input.json query.sh
	./query.sh

tjout.json: input.json weather.json tj.sh
	./tj.sh

clean:
	rm -f weather.json tjout.json woeid.json
