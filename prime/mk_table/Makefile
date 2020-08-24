all: smallprimes.xlsx sp.gpg

nothing:
	@echo "**make clean** to cleanup"

smallprimes.xlsx:	mk_table.py
	@python3 mk_table.py

sp.gpg: smallprimes.xlsx
	@bash sendit.sh

clean:
	rm -f smallprimes.xlsx sp.gpg
