func findTargetSumWays(nums []int, S int) int {
	nlen := len(nums)
	if nlen == 0 {
		return 0
	}

	res := 0
	helper(nums, 0, 0, S, &res)
	return res
}

func helper(nums []int, index int, sum int, target int, res *int) {
	// + case
	sum += nums[index]
	if index == len(nums)-1 {
		if target == sum {
			*res = *res + 1
		}
	} else {
		helper(nums, index+1, sum, target, res)
	}
	sum -= nums[index] // put the sum value back

	// - case
	sum -= nums[index]
	if index == len(nums)-1 {
		if target == sum {
			*res = *res + 1
		}
	} else {
		helper(nums, index+1, sum, target, res)
	}
}