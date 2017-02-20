package main

import "math"

func divide(dividend int, divisor int) int {
	// handle overflow
	if divisor == -1 && dividend == math.MinInt32 {
		return math.MaxInt32
	}

	u := 1
	switch {
	case dividend < 0 && divisor < 0:
		dividend, divisor = -1*dividend, -1*divisor
	case dividend < 0 && divisor > 0:
		u, dividend = -1, -1*dividend
	case dividend > 0 && divisor < 0:
		u, divisor = -1, -1*divisor
	}

	if dividend == divisor {
		return 1 * u
	} else if dividend < divisor {
		return 0
	}

	res := 0
	for {
		p := 1
		for {
			if (p<<1)*divisor >= dividend {
				break
			}
			p = p << 1
		}
		res += p
		dividend -= p * divisor
		if dividend < divisor {
			break
		}
	}
	return res * u
}
