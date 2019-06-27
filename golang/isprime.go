package main

import "fmt"
import "math"

func isPrime(m int) bool {
    if m <= 1 {
        return false
    }
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}
    r := int(math.Sqrt(float64(m)))
    fmt.Println(r)
    n := len(primes)
    if primes[n-1] >= r {
        for i := 0; i < n; i++ {
            p := primes[i]
            if m % p == 0 {
                fmt.Println("divided by", p)
                return false
            }
        }
    }

    fmt.Println("go beyond...")
    for j := primes[n-1] + 2; j <= r; j += 2 {
        if m % j == 0 {
            fmt.Println("divided by", j)
            return false
        }
    }

    return true
}


func main() {
    p := 1048577
    fmt.Printf("hello: %d\n", p)
    if isPrime(p) {
        fmt.Println("yes")
    } else {
        fmt.Println("no")
    }
}
