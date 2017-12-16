func numWays(n int, k int) int {
	if n == 0 || k == 0 {
		return 0
	}

	var diff, same, tmp int
	for i := 0; i < n; i++ {
		switch i {
		case 0:
			diff, same = k, 0
		case 1:
			diff, same = k*k-k, k
		default:
			tmp = diff
			diff = (diff + same) * (k - 1)
			same = tmp
		}
	}
	return diff + same
}