phony: all

all: gdrive

the_date:
	D=$(date +%Y%m%d) ; echo $D

gdrive:
	@python driving_data.py --run

check:
	@python check_csv.py -i /tmp/__driving_datasheet__.csv

plot:
	@python driving_data.py -i /tmp/__driving_datasheet__.csv --years --run
	@python commune_all.py

# use boxplot_by_years.py to plot boxplot by year
boxplot:
	@python boxplot_by_years.py

help:
	@echo you may use: the_date, gdrive, check, plot, boxplot
	@echo default is gdrive

