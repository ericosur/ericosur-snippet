package main

import (
    "fmt"
    "math"
)

func main() {
    var ss, cc float64
    const mypi = 3.141592653589793238462643383279502884197169399375
    const myrad = mypi / 3.0
    ss, cc = math.Sincos(myrad)
    var tt = math.Tan(myrad)
    fmt.Printf("sin: %v, cos: %v\ntan: %v (%v)\n", ss, cc, tt, ss/cc)

    fmt.Printf("cos(pi/2) = %v\n", math.Cos(mypi/2.0))
}
