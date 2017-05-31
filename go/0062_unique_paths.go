func uniquePaths(m int, n int) int {
	m, n = m-1, n-1
	if m == 0 || n == 0 {
		return 1
	}
	if m < n {
		m, n = n, m
	}

	d1, d2 := 1, 1
	for i := m + 1; i <= m+n; i++ {
		d1 *= i
	}
	for i := 1; i <= n; i++ {
		d2 *= i
	}
	return d1 / d2
}
