#!/usr/bin/env python

# demo of using raw_input
str = raw_input('input you name: ')
print str

# demo of using getpass
import getpass
pw = getpass.getpass('password: ')
print 'pw: ' + pw
