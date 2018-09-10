package myutil

import (
    "fmt"
    "math"
)

func Mypow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    } else {
        return lim
    }
}

func Add(x int, y int) int {
    return x + y
}

// will not be exported
func main() {
    fmt.Printf( "%f\n", Mypow(3, 2, 10) )
    fmt.Println( Add(3, -1) )
}
