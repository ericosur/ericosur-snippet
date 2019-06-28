package main

import (
    "fmt"
    "math"
    "time"
    "math/rand"
    "myutil"
)


// studpid function, MUST always return 1.0
func sin2_plus_cos2(rad float64) float64 {
    ss, cc := math.Sincos(rad)
    sum := math.Pow(ss, 2.0) + math.Pow(cc, 2.0)
    return sum
}

// test sin^2 + cos^2, should be 1.0
func test() {
    for i:=0; i < 100; i++ {
        rad := myutil.Deg2rad(float64(rand.Intn(360)))
        diff := math.Abs(sin2_plus_cos2(rad) - 1.0)
        if diff != 0.0 {
            fmt.Printf("not ok: %v\n", diff)
        }
    }
}


func main() {
    rand.Seed(time.Now().Unix())

    //var ss, cc float64
    const mypi = 3.141592653589793238462643383279502884197169399375105820974944
    const myrad = mypi / 3.0

    ss, cc := math.Sincos(myrad)
    tt := math.Tan(myrad)
    uu := ss / cc

    fmt.Printf("abs pi vs mypi: %v\n", math.Abs(math.Pi - mypi))
    fmt.Printf("sin: %v, cos: %v\n", ss, cc)
    fmt.Printf("tan: %v vs %v abs: %v", tt, uu, math.Abs(tt - uu))

    diff := math.Abs(math.Cos(mypi/2.0) - math.Cos(math.Pi/2.0))
    fmt.Printf("cos(mypi/2) = %v\n", math.Cos(mypi/2.0))
    fmt.Printf("cos(pi/2) = %v\n", math.Cos(math.Pi/2.0))
    fmt.Printf("diff: %v\n", diff)

    test()
}
