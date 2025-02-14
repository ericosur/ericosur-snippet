.phony:	help

PY := python3

help:
	@echo "available targets: help, target, hello, json, clean"

target:
	@echo "run chataes.py"
	@${PY} chataes.py

hello:
	@echo "'Hello world' as plain text"
	@echo $(shell echo "Hello world" > _b64.txt)
	@${PY} passutil.py -o hello.json $(shell cat _b64.txt)
	@${PY} decpu.py hello.json
	@rm _b64.txt hello.json

json:
	@echo "run passutil.py to generate json"
	@${PY} passutil.py -o my.json A123456789

clean:
	rm -f *.bin *.json _b64.*
