func numTrees(n int) int {
	if n == 0 {
		return 1
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	}

	dp := make([]int, n+1)
	dp[0], dp[1], dp[2] = 1, 1, 2
	for i := 3; i <= n; i++ {
		for leftNum := 0; leftNum <= i-1; leftNum++ {
			dp[i] += dp[leftNum] * dp[i-1-leftNum]
		}
	}
	return dp[n]
}