package main

import (
    "fmt"
    "myutil"    // myutil is my own module
)


func main() {
    fmt.Println("hello world")
    fmt.Println(myutil.Add(5, 6))
    fmt.Println(myutil.Mypow(2,3,20))
}
