#!/usr/bin/python3
# coding: utf-8

'''
query players.db to find location coordinates
'''

import sqlite3
import sys

try:
    from hexdump import hexdump
except ImportError:
    print("need install module: hexdump")
    sys.exit(1)

class Solution():
    ''' sqlite and query '''
    def __init__(self):
        self.dbfile = 'players.db'
        self.con = sqlite3.connect(self.dbfile)

    @staticmethod
    def show_blob(buffer):
        ''' show blob '''
        print(type(buffer))
        print(len(buffer))
        hexdump(buffer)

    def query_blob(self):
        ''' query blob '''
        res = self.con.execute("SELECT data FROM localPlayers")
        blob = res.fetchone()
        self.show_blob(blob[0])

    def query_xy(self):
        ''' query x, y location '''
        res = self.con.execute("SELECT name,x,y FROM localPlayers")
        (name, x, y) = res.fetchone()
        print(f'player name: {name}')
        x = int(x)
        y = int(y)
        print(f'https://map.projectzomboid.com/#{x}x{y}')

    def run(self):
        ''' run '''
        self.query_xy()
        #self.query_blob()


def main():
    ''' main '''
    sol = Solution()
    sol.run()

if __name__ == '__main__':
    main()
