#!/usr/bin/python

# python 3.0 checked

import sys
import locale

def convert_temperature(argv):
	# Loop over the arguments
	for i in sys.argv[1:]:
		try:
			fahrenheit = float(locale.atof(i))	# note: string.atoi ==> locale.atoi
		except locale.atoi_error:	# string.atoi_error => locale.atoi_error
			print(repr(i), "not a numeric value")
		except locale.atof_error:
			# never get there
			print(repr(i), "not a numeric value")
		else:
			celsius = (fahrenheit - 32.0) * 5.0 / 9.0
			#print '%i\260F = %i\260C' % (int(fahrenheit), int(celsius+.5))
			#	print '%i degree F = %i degree C' % (int(fahrenheit), int(celsius+.5))
			#print('%i degree F = %i degree C' % (fahrenheit, celsius))
			print('%.2f degree F = %.2f degree C' % (fahrenheit, celsius))


def main():
	# If no arguments were given, print a helpful message
	if len(sys.argv)==1:
	    print('Usage: celsius temp1 temp2 ...')
	    sys.exit(0)

	print('convert fahrenheit to celsius')
	convert_temperature(sys.argv)


if __name__ == '__main__':
	main()