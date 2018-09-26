package main

import (
    "fmt"
    "time"
)

func foo(epoch int64) {
    fmt.Println(time.Unix(epoch, 0).UTC())
}

func main() {
    foo(1e9)
}
