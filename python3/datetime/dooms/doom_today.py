'''
provide get_today() to get today date in UTC timezone
'''

from datetime import date, datetime, timezone


def get_today() -> date:
    ''' get this year UTC as datetime '''
    return datetime.now(tz=timezone.utc).date()

if __name__ == '__main__':
    print(get_today())
