func moveZeroes(nums []int) {
	cur, skipped := 0, 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			skipped++
			continue
		}
		nums[cur] = nums[i]
		cur++
	}

	for i := len(nums) - 1; skipped > 0; i-- {
		nums[i] = 0
		skipped--
	}
}