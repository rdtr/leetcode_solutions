package main

func nextPermutation(nums []int) {
	nlen := len(nums)
	if nlen <= 1 {
		return
	}

	for i := nlen - 1; i > 0; i-- {
		if nums[i] <= nums[i-1] {
			continue
		}

		j := i
		for ; j < nlen-1; j++ {
			if nums[j] > nums[i-1] && nums[j+1] <= nums[i-1] {
				break
			}
		}

		nums[i-1], nums[j] = nums[j], nums[i-1]
		reverse(nums[i:])
		return
	}

	// in case an arrangement is impossible
	reverse(nums)
}

func reverse(nums []int) {
	for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
		nums[i], nums[j] = nums[j], nums[i]
	}
}
