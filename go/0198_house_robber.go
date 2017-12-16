func rob(nums []int) int {
	nlen := len(nums)
	dp := make([]int, nlen)

	if nlen == 0 {
		return 0
	} else if nlen == 1 {
		return nums[0]
	} else if nlen == 2 {
		return max(nums[0], nums[1])
	} else if nlen == 3 {
		return max(nums[0]+nums[2], nums[1])
	}

	dp[0] = nums[0]
	dp[1] = nums[1]
	dp[2] = nums[0] + nums[2]
	for i := 3; i < nlen; i++ {
		dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
	}
	return max(dp[len(dp)-1], dp[len(dp)-2])
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}