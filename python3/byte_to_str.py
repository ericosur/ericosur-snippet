#!/usr/bin/env python3
# coding: utf-8

def b2s(byte_array):
    dd = byte_array.decode()
    print(dd)

def main():
    b2s(b'\xef\xa3\xbf')
    b2s(b'\xF0\x9F\x90\xB1')

if __name__ == '__main__':
    main()
