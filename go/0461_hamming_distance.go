func hammingDistance(x int, y int) int {
	xor := x ^ y

	res := 0
	for xor != 0 {
		xor = xor & (xor - 1)
		res++
	}
	return res
}

