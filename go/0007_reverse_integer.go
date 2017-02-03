package main

import "math"

func reverse(x int) int {
	if x == 0 {
		return 0
	}

	negpos := 1
	if x < 0 {
		negpos = -1
		x *= -1
	}

	// check digit count
	xlen := 0
	for y := x; y != 0; {
		xlen++
		r := y % 10
		y -= r
		y /= 10
	}

	var res int
	for x != 0 {
		r := x % 10

		add := r * int(math.Pow10(xlen-1))
		if add > math.MaxInt32-res {
			return 0 // check overflow
		}

		res += add
		xlen--
		x -= r
		x /= 10
	}
	return res * negpos
}
