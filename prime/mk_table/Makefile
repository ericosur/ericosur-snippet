all: smallprimes.xlsx

nothing:
	@echo "**make clean** to cleanup"

smallprimes.xlsx:	mk_table.py
	@python3 mk_table.py

clean:
	rm -f smallprimes.xlsx
