#
# pp.py will list all sys.path
# this script will search for modules from these path
#
#
# you may run it via python2 or python3 (or anaconda python)
# to see the difference
#

'''
list each item of sys.path
'''

import sys

for idx, pp in enumerate(sys.path):
    print('[{0:02d}]: {1}'.format(idx, pp))
