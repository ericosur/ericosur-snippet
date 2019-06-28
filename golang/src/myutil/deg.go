package myutil

import "math"

func Rad2deg(rad float64) (deg float64) {
    deg = rad * 180.0 / math.Pi
    return
}

func Deg2rad(deg float64) (rad float64) {
    rad = deg * math.Pi / 180.0
    return
}
