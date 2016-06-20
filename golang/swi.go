package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("when is Saturday")
    today := time.Now().Weekday()
    switch time.Saturday {
    case today + 0:
        fmt.Println("today")
    case today + 1:
        fmt.Println("tomorrow")
    case today + 2:
        fmt.Println("in two days")
    default:
        fmt.Println("too far away")
    }
}
