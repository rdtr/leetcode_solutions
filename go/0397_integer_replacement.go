func integerReplacement(n int) int {
	res := 0
	for n > 0 {
		if n == 1 {
			break
		}
		if n&1 == 1 {
			if n != 3 && checkLastTwo(n) {
				n++
			} else {
				n--
			}
			res++
		}
		n = n >> 1
		res++
	}
	return res
}

func checkLastTwo(n int) bool {
	for i := 0; i < 2; i++ {
		if n&1 != 1 {
			return false
		}
		n = n >> 1
	}
	return true
}