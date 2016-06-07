/// rand.go

package main

import (
    "fmt"
    //"math"
    "math/rand"
)

func add(x int, y int) int {
    return x + y
}


func main() {
    sum := 0
    for i:=0; i<10; i++ {
        sum += rand.Intn(10)
    }
    fmt.Println(sum)

}
