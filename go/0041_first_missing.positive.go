package main

func firstMissingPositive(nums []int) int {
	nlen := len(nums)
	for i := 0; i < nlen; i++ {
		if nums[i] >= 1 && nums[i] <= nlen && nums[i] != nums[nums[i]-1] {
			nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
			i-- // keep the same index
		}
	}

	for i := 0; i < nlen; i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}
	return nlen + 1
}
