func trailingZeroes(n int) int {
	res := 0
	for {
		res = res + (n / 5)
		n = n / 5
		if n/5 == 0 {
			break
		}
	}
	return res
}