/// rand.go

package main

import (
    "fmt"
    "time"
    "math/rand"
)

func add(x int, y int) int {
    return x + y
}

func get_rand() int {
    return rand.Intn(100)
}

func get_sum(repeat int) int {
    sum := 0
    for i := 0; i < repeat; i++ {
        sum += i
    }
    return sum
}

func main() {
    var tt64 = time.Now().Unix()
    rand.Seed(tt64)
    fmt.Println("get one random num:", get_rand())

    const REPEAT = 10
    sum := get_sum(REPEAT)
    fmt.Println("sum:", sum)

}
