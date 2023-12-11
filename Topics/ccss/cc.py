#!/usr/bin/env python3
# coding: utf-8

'''
client
'''

import socket


def main():
    ''' main '''
    HOST = '127.0.0.1'
    PORT = 9801

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        cmd = input("Please input msg:")
        s.send(cmd)
        data = s.recv(1024)
        print(data)

        #s.close()

if __name__ == '__main__':
    main()
