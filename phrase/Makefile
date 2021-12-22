.phony: help

help:
	@echo "__make action__ to generate tables..."

clean:
	rm -f out.json out.txt storable.dat

action:
	@echo "exec mygrep.pl..."
	perl mygrep.pl
	perl listarr.pl
