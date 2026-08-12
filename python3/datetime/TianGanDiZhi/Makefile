PYTHON = /home/user/src/ericosur-snippet/python3/.venv/bin/python

Y ?= 2030
A ?= 1
B ?= 3

.PHONY: help demo year ab list tests lint

help:
	@echo "TianGanDiZhi Makefile targets"
	@echo "  make demo            # run default demo (year and AB query)"
	@echo "  make year Y=2030     # show GanZhi of the specified year"
	@echo "  make ab A=1 B=3      # show possible years for a pair"
	@echo "  make list            # list all TianGan/DiZhi/生肖"
	@echo "  make tests           # run unit tests"
	@echo "  make lint            # run ruff lint for this folder"
	@echo ""
	@echo "A (天干 index): 0..9"
	@echo "B (地支 index): 0..11"
	@echo "A+B must be even"

demo:
	@echo "[demo-1] Year to TianGan/DiZhi"
	@$(MAKE) --no-print-directory year Y=$(Y)
	@echo ""
	@echo "[demo-2] TianGan/DiZhi to possible years"
	@$(MAKE) --no-print-directory ab A=$(A) B=$(B)

year:
	@$(PYTHON) ganzhi.py $(Y)

ab:
	@$(PYTHON) ganzhi.py -a $(A) -b $(B)

list:
	@$(PYTHON) ganzhi.py --list

tests:
	@$(PYTHON) -m unittest -v test_gngan_yaljux.py

lint:
	@$(PYTHON) -m ruff check .
