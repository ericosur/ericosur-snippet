.phony:	help

PY='python'

help:
	@echo "__make target__ or __make clean__"

target:
	@echo "run chataes.py"
	@${PY} chataes.py

test:
	@echo "run passutil.py"
	@${PY} passutil.py -d -o my.json A123456789

clean:
	rm -f encrypted.bin

