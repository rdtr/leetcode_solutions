package main

func myPow(x float64, n int) float64 {
	if n == 0 {
		return 1.0
	}
	negative := false
	if n < 0 {
		negative = true
		n = n * -1
	}

	res, base := 1.0, x
	for n > 1 {
		if n%2 == 0 {
			n = n >> 1
			base = base * base
			continue
		}
		n = n - 1
		res *= base
	}
	res *= base
	if negative {
		return 1.0 / res
	}
	return res
}
