package main

import (
    "fmt"
    "math"
    "time"
)

func foo(epoch int64) {
    fmt.Println(time.Unix(epoch, 0).UTC())
}

func main() {
    fmt.Println("power of 2")
    foo(int64(math.Pow(2, 10)))
    foo(int64(math.Pow(2, 20)))
    foo(int64(math.Pow(2, 30)))
    foo(int64(math.Pow(2, 31)))
    foo(int64(math.Pow(2, 32)))
    fmt.Println("power of 10")
    foo(1e7)
    foo(1e8)
    foo(1e9)
}
