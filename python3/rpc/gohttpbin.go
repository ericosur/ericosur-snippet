package main

import "fmt"
import "log"
import "net/http"
import "strconv"

func main() {
    n := 32

    // type struct http.Response
    // https://golang.org/pkg/net/http/#Response
    resp, err := http.Get("https://httpbin.org/range/" + strconv.Itoa(n))
    if err != nil {
        log.Fatal(err)
        return
    }

    fmt.Printf("type: %T\n", resp)
    fmt.Printf("resp: %v\n", resp)

}
