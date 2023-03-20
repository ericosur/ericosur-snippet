.phony:	help


PY3='python3'

help:
	@echo "__make target__ or __make clean__"

target:
	cp -f fibo.py fibo.pyx
	${PY3} setup.py build_ext --inplace
	rm -f fibo.pyx

clean:
	rm -rf build/ fibo.c fibo*so fibo.pyx
