func combinationSum4(nums []int, target int) int {
	cache := make(map[int]int)
	return helper(cache, nums, target)
}

func helper(cache map[int]int, nums []int, target int) int {
	if val, ok := cache[target]; ok {
		return val
	}

	res := 0
	for i := len(nums) - 1; i >= 0; i-- {
		switch num := nums[i]; {
		case num < target:
			res += helper(cache, nums, target-num)
		case num == target:
			res += 1
		}
	}
	cache[target] = res
	return res
}