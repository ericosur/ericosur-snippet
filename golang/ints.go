package main

import "fmt"

func main() {
    var i32 int32 = 429496300
    var i64 int64

    i64 = int64(i32)
    fmt.Println("i64:", i64)
}
