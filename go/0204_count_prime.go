func countPrimes(n int) int {
	if n <= 1 {
		return 0
	}

	flags := make([]bool, n)

	flags[0], flags[1] = true, true
	for i := 2; i < n; i++ {
		if flags[i] {
			continue
		}
		for j := 2; i*j < n; j++ {
			flags[i*j] = true
		}
	}

	cnt := 0
	for i, _ := range flags {
		if !flags[i] {
			cnt++
		}
	}
	return cnt
}