#
# this is a simple and unscientific set of tests to measure marshal
# against cPickle. This is not a module; you run things directly.
# The context is
# http://utcc.utoronto.ca/~cks/space/blog/python/MarshalVsCPickle
# (This is the test framework I used for it.)

# http://utcc.utoronto.ca/~cks/programs/python/marshal-vs-cpickle.py
# http://www.dup2.org/node/789

# will not port to python3
# pylint: skip-file

import sys
import marshal, cPickle
import timeit

obj = { 'mtimes': {'/a/b': 1000.10, '/e/f': 9000.10 },
 	'ctimes': {'/a/e': 91010.10, "/e/f/g": 890010.59 }
      }
obj2 = (obj, ("asdfasd fasdlfkjnasdlfkjasdl;fkjasdf asfdasdfjkl;sdjfsdaf" * 200,
	      ("abc", "def", "ghi"),
	      True,
	      "a title"), )

tobj = None
robj1 = ""
robj2 = ""

def domarsh():
	return marshal.dumps(tobj, 2)
def dopickle():
	return cPickle.dumps(tobj, -1)

def unmarsh():
	return marshal.loads(robj1)
def unpickle():
	return cPickle.loads(robj2)

t1 = timeit.Timer(stmt = "domarsh()", setup="from __main__ import domarsh")
t2 = timeit.Timer(stmt = "dopickle()", setup="from __main__ import dopickle")
t3 = timeit.Timer(stmt = "unmarsh()", setup="from __main__ import unmarsh")
t4 = timeit.Timer(stmt = "unpickle()", setup="from __main__ import unpickle")

print("big tests")
for i in ( {'a': {'b': {'c': {}, 'd': {}}, 'e': {'f': 'g'}}, 'h': 'i'},
	   {'a': [10]*10, 'b': [20]*10},
	  obj, obj2, 10, "abc", [10] * 10, (10,) * 10, ("abc",) * 10,
	  True, False, None, 10.58, [10.58] * 10,
	  "asdfasd fasdlfkjnasdlfkjasdl;fkjasdf asfdasdfjkl;sdjfsdaf" * 200,
	  u"asdfasd fasdlfkjnasdlfkjasdl;fkjasdf asfdasdfjkl;sdjfsdaf" * 200,
	  ({}, ('abc', ('a', 'b', 'c'), True, "a title")),
	  {}, {'abc': 'def'}, {'abc': {}}, {'abc': {}, 'def': {}}):
	tobj = i
	robj1, robj2 = domarsh(), dopickle()
	if tobj == obj2:
		msg = "big"
	else:
		msg = str(tobj)
		if len(msg) > 40:
			msg = msg[:30]+"<trunc>"
	print(msg, t1.timeit(), t3.timeit(), t2.timeit(), t4.timeit())

print("string length")
for i in (1, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 32768):
	tobj = "*" * i
	robj1 = domarsh(); robj2 = dopickle()
	print(i, t1.timeit(), t3.timeit(), t2.timeit(), t4.timeit())

