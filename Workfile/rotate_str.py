#!/usr/bin/env python

# input "ab"
# output "ab" "aB" "Ab" "AB"
def rotate_upper(input_str):
	#input_str = "flac"
	input_list = list(input_str)
	max = 2**len(input_str)
	format_str = '0' + str(len(input_str)) + 'b'
	res = ''
	hh = {}
	for i in xrange(max):
		s = format(i, format_str)
		#print(s)
		dgt = 0
		for j in list(s):
			if j=='1':
				res = res + input_list[dgt].upper()
			else:
				res = res + input_list[dgt].lower()
			dgt = dgt + 1
		#print(res)
		hh[res] = 1
		res = ''
	for x in hh:
		print('*.' + x + ','),
	print

if __name__ == "__main__":
	tails = ['mp3', 'wav', 'aac', 'm4a', 'wma', 'mp4', 'wmv', 'png', 'jpg']
	for x in tails:
		rotate_upper(x)

