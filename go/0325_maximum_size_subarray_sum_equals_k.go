func maxSubArrayLen(nums []int, k int) int {
	mp := make(map[int]int)
	mp[0] = -1

	res := 0
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]

		if index, ok := mp[sum-k]; ok {
			if i-index > res {
				res = i - index
			}
		}

		if _, ok := mp[sum]; !ok {
			mp[sum] = i
		}
	}
	return res
}