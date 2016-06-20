package main

import "fmt"

func swap(x, y string) (string, string) {
    return y, x
}

func swap2(x, y string) (string, string, string) {
    return y, x, "dot"
}

func main() {
    a, b := swap("hello", "world")
    fmt.Println(a, b)
    a, b, c := swap2("hail", "hydra")
    fmt.Println(a, b, c)
}
