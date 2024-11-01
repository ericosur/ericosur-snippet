phony: all

all: gdrive

the_date:
	D=$(date +%Y%m%d) ; echo $D

gdrive:
	@python driving_data.py --run

check:
	@python check_csv.py -i /tmp/__driving_datasheet__.csv
