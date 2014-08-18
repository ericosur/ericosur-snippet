def stupid_factorial(m):
	if m <= 1:
		return 1
	else:
		return m * stupid_factorial(m - 1)

result = stupid_factorial(100)
print result
allchar = list(str(result))
sum = 0
for xx in allchar:
	sum += int(xx)
print "sum", sum
