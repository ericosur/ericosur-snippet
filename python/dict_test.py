#!/usr/bin/python

# python dictionary

def print_dict(**foo):
	for x in foo:
		print x,"=>",foo[x]

rec = {	'name': {'first': 'Brown', 'last': 'Smith'},
		'job': ['dev', 'mgr'],
		'age': 40.5}
print("print rec: ")
print_dict(**rec)
		
print("rec['name']: ", rec['name'])
print("rec['name']['first']:", rec['name']['first'])
print("rec['name']['last']", rec['name']['last'])

rec['job'].append('foo')

# cannot pass at python 3.0
print(('age' in rec))


''' map() test '''
def cube(x):
	return x*x*x

mm = range(5, 9)
mm = map(cube, mm)
print "map(): ", mm
