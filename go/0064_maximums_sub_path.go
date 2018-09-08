package main

func minPathSum(grid [][]int) int {
	mlen := len(grid)
	if mlen == 0 {
		return 0
	}
	nlen := len(grid[0])
	if nlen == 0 {
		return 0
	}

	dp := initDP(mlen, nlen)
	initFirstCol(dp, grid)
	initFirstRow(dp, grid)

	for i := 1; i < mlen; i++ {
		for j := 1; j < nlen; j++ {
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		}
	}
	return dp[mlen-1][nlen-1]
}

func initDP(mlen, nlen int) [][]int {
	dp := make([][]int, mlen)
	for i := 0; i < mlen; i++ {
		dp[i] = make([]int, nlen)
	}
	return dp
}

func initFirstCol(dp, grid [][]int) {
	for i := 0; i < len(dp); i++ {
		if i == 0 {
			dp[i][0] = grid[i][0]
		} else {
			dp[i][0] = grid[i][0] + dp[i-1][0]
		}
	}
}

func initFirstRow(dp, grid [][]int) {
	for i := 0; i < len(dp[0]); i++ {
		if i == 0 {
			dp[0][i] = grid[0][i]
		} else {
			dp[0][i] = grid[0][i] + dp[0][i-1]
		}
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
