#!/usr/bin/python
#
# to list black Friday
#

import datetime


def get_blackfriday(from_year, to_year):
    MIN_MONTH = 1
    MAX_MONTH = 12
    # 0:MON, 1:TUE, 2:WED, 3:THU, 4:FRI, 5:SAT, 6:SUN
    WEEKDAY_FRIDAY = 4

    for yr in xrange(from_year, to_year+1):
        for mnth in xrange(MIN_MONTH, MAX_MONTH+1):
            dd = datetime.datetime(yr, mnth, 13)
            if dd.weekday() == WEEKDAY_FRIDAY:
                print get_date_str(dd), "is Black Friday"

def get_date_str(dd):
    str = dd.strftime("%d %b %Y")
    return str

def main():
    today = datetime.date.today()
    from_y = today.year
    get_blackfriday(from_y, from_y+15)


if __name__ == '__main__':
    #print(get_date_str(datetime.date.today()))
    main()
