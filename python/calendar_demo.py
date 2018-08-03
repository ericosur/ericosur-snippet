#!/usr/bin/python

'''use module calendar to show calendar of this year'''

import calendar
from datetime import date

YEAR = date.today().year
calendar.prcal(YEAR)
