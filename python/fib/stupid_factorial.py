import math

def stupid_factorial(m):
	if m <= 1:
		return 1
	else:
		return m * stupid_factorial(m - 1)

def main():
    n = 300 # try to get n!
    ans = stupid_factorial(n)
    print n, "! =", ans
    print "log10(ans) = ", math.log10(ans)
    print "string len: ", len(str(ans))
    '''
    try to use Stirling's approximation for value of n!
    n! ~ sqrt(2*pi*n)*(n/e)^n
    but (n/e)^n is too large

    try to know how many digits for n!
    log10(n!) ~ log10(sqrt(2*pi*n)) + n * log10(n/e)

    '''
    val = math.log10(2*math.pi*n) + n * math.log10(n/math.e)
    print "log(val) =", val

if __name__ == '__main__':
    main()
