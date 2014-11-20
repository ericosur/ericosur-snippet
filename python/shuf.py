#!/usr/bin/python
#
# a simple demo to ultilize function in the other script
#

# use shuffle_array() in fisher_yates_shuffle.py
from fisher_yates_shuffle import shuffle_array

name_list = ['zoo', 'bob', 'tim', 'david', 'pineapple',
	'fred', 'victory', 'limb']

print(name_list)

# repeat 5 times
for i in range(5):
	shuffle_array(name_list)
	print(name_list)
