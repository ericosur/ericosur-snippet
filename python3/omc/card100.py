#!/usr/bin/python

def main():
	cards = [ x for x in range(1, 101) ]
	t3 = list()
	for c in cards:
		if c % 3 == 0:
			continue
		t3.append(c)
	t7 = list()
	for c in t3:
		if c % 7 == 0:
			continue
		t7.append(c)
	print(t7)


if __name__ == '__main__':
	main()
