package main

import (
    "fmt"
    "math"
)

func Sqrt(x float64) float64 {
    var z float64
    const REP = 700000000
    z = 1
    for i:=0; i<REP; i++ {
        z = z - (z * z - x) / 2*z
    }
    return z
}

func main() {
    fmt.Println("my Sqrt():", Sqrt(2))
    fmt.Println("math.Sqrt():", math.Sqrt(2))
}
