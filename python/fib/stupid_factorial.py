def stupid_factorial(m):
	if m <= 1:
		return 1
	else:
		return m * stupid_factorial(m - 1)

print stupid_factorial(5)
