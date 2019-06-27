package main

import (
    "fmt"
    "math/rand"
    "time"
    "myutil"    // myutil is my own module
)

// will return two int
func swap(p, q int) (int, int) {
	return q, p
}

func show(p, q int) {
	fmt.Printf("gcd(%d, %d) = %d\n", p, q, myutil.Gcd(p, q))
}

// naked return
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	rand.Seed(time.Now().Unix())

	width := 1920
	height := 1080
	show(width, height)

    for i := 0; i < 10; i++ {
    	m := rand.Intn(100000)
    	n := rand.Intn(200000)
    	show(m, n)
    	show(swap(m, n))
    }

    r := rand.Intn(999)
    fmt.Printf("split(%d):", r)
    fmt.Println(split(r))
}
