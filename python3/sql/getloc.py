#!/usr/bin/env python3
# coding: utf-8

'''
query players.db to find location coordinates
'''

import sqlite3
try:
    import hexdump
    USE_HEXDUMP = True
except ImportError:
    print("install module 'hexdump' to show blob")
    USE_HEXDUMP = False

# if module hexdump is not installed, the dump_nothing is used
def dump_nothing(_buffer) -> None:
    ''' dump nothing '''
    return None

class Solution():
    ''' sqlite and query '''
    def __init__(self):
        self.dbfile = 'players.db'
        self.con = sqlite3.connect(self.dbfile)

    @staticmethod
    def show_blob(buffer):
        ''' show blob '''
        limit = 512
        size = len(buffer)
        dump = hexdump.hexdump if USE_HEXDUMP else dump_nothing
        if size > limit:
            print(f'NOTE: only show first {limit} bytes')
            dump(buffer[:limit])
        else:
            dump(buffer)

    def query_blob(self):
        ''' query blob '''
        res = self.con.execute("SELECT data FROM localPlayers")
        for row in res.fetchall():
            self.show_blob(row[0])

    def query_xy(self):
        ''' query x, y location '''
        res = self.con.execute("SELECT name,x,y FROM localPlayers")
        for row in res.fetchall():
            name, x, y = row
            print(f'player name: {name}')
            # in the database, x, y are float, but we need int for map
            # will lose some precision, but it's ok for map
            x = int(x)
            y = int(y)
            print(f'https://map.projectzomboid.com/#{x}x{y}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.query_xy()
        #obj.query_blob()

if __name__ == '__main__':
    Solution.run()
