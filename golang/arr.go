/// arr.go

package main

import "fmt"

func main() {
    var a = [4]int {1,2,3,4}

    for i := range a {
        fmt.Println(a[i])
    }
}
