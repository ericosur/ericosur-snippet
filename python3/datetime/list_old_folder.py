#!/usr/bin/env python3

'''
    try to list the folder while is one month ago
'''


import os
import time
from datetime import datetime
from glob import glob

from datetime_common import prt  # type: ignore[import]


class ShowDirList:
    ''' show the folder list by epoch '''
    SEP_LEN = 60
    DEFAULT_DAYS = 30

    def __init__(self):
        self.dirs = []
        self.__collect_dirs__()

    def __collect_dirs__(self):
        ''' collect the folder list and sort it '''
        for d in glob('*'):
            if not os.path.isdir(d):
                continue
            if d[0] == '.' or d[0:2] == '__':
                continue
            self.dirs.append(d)
        self.dirs = sorted(self.dirs)

    @staticmethod
    def get_current_epoch() -> int:
        ''' get current epoch '''
        return int(time.time())

    @staticmethod
    def get_older_epoch(days: int) -> int:
        ''' get epoch for days ago '''
        return ShowDirList.get_current_epoch() - days * 24 * 3600

    @staticmethod
    def get_newer_epoch(days: int) -> int:
        ''' get epoch for days later '''
        return ShowDirList.get_current_epoch() + days * 24 * 3600

    @staticmethod
    def get_date_str_from_epoch(epoch: float) -> str:
        ''' get date string from epoch '''
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch))

    @staticmethod
    def sep() -> None:
        ''' print a separator '''
        prt('-' * ShowDirList.SEP_LEN)

    @staticmethod
    def get_datetime_from_epoch(epoch: float) -> datetime:
        ''' get datetime from epoch with local timezone '''
        return datetime.fromtimestamp(epoch).astimezone()

    def show_older_dirs(self, days: int=DEFAULT_DAYS) -> None:
        ''' show the older folders '''
        ago = ShowDirList.get_older_epoch(days)
        prt(f'> The folders are older than {days} days ago: {ShowDirList.get_datetime_from_epoch(ago)}')
        ShowDirList.sep()
        for d in self.dirs:
            ctime = os.path.getctime(d)
            if ctime <= ago:
                ftime = ShowDirList.get_date_str_from_epoch(ctime)
                prt(f"[yellow]{d:20s}[/]: ({ftime})")

    def show_newer_dirs(self, days: int=DEFAULT_DAYS) -> None:
        ''' show the newer folders '''
        ago = ShowDirList.get_older_epoch(days)
        prt(f'> The folders are newer, within {days} days: {ShowDirList.get_datetime_from_epoch(ago)}')
        ShowDirList.sep()
        for d in self.dirs:
            ctime = os.path.getctime(d)
            if ctime >= ago:
                ftime = ShowDirList.get_date_str_from_epoch(ctime)
                prt(f"[yellow]{d:20s}[/]: ({ftime})")

def main():
    ''' main '''
    obj = ShowDirList()
    DAYS_AGO = 60
    obj.show_older_dirs(DAYS_AGO)
    obj.show_newer_dirs()

if __name__ == '__main__':
    main()
