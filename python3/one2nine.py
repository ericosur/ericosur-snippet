#!/usr/bin/python
# coding: utf-8

def get_number(i):
	digits = ""
	rep = str(i)
	for d in range(i):
		digits += rep
	return digits

def main():
	summ = 0
	vals = []
	for i in range(1, 10):
		val = get_number(i)
		vals.append(val)
		summ += int(val)

	print(f"The sum of these values:\n{vals}\n{summ}\nAnd mod 9 = {summ % 9}")

if __name__ == '__main__':
	main()
