import urllib
import re

''' script to solve Python Chanllenge #4
'''

def get_web(url):
	print "get_web: ", url
	web = urllib.urlopen(url)
	content = web.read()
	return content

cnt = 0
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46059"
while (url != None and cnt < 200):
	cnt += 1
	print "cnt = ", cnt,
	cont = get_web(url)
	url = None
	#if cnt > 1: print cont
	for line in cont.splitlines():
		m0 = re.search('Yes',line)
		if m0 != None:
			print cont
			break
		m = re.search('and the next nothing is (\d+)', line)
		if m != None:
			print "match: ", m.group(1)
			url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + m.group(1)
			print "try to get: ", url
			break
