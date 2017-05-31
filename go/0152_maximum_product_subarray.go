func maxProduct(nums []int) int {
	nlen := len(nums)

	curmin, curmax := nums[0], nums[0]

	res := nums[0]
	for i := 1; i < nlen; i++ {
		tmpmax := maxint(maxint(curmax*nums[i], curmin*nums[i]), nums[i])
		curmin = minint(minint(curmax*nums[i], curmin*nums[i]), nums[i])
		curmax = tmpmax

		if res < curmax {
			res = curmax
		}
	}
	return res
}

func maxint(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func minint(a, b int) int {
	if a < b {
		return a
	}
	return b
}