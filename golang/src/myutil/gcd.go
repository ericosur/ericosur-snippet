package myutil

func Gcd(m int, n int) int {
    if (n == 0) {
    	return m
    }
    return Gcd(n, m % n)
}
