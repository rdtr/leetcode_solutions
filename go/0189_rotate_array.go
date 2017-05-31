package main

func rotate(nums []int, k int) {
	nlen := len(nums)
	if nlen <= 1 {
		return
	}

	k = k % nlen
	if k == 0 {
		return
	}

	newNums := make([]int, len(nums))
	copy(newNums[:k], nums[nlen-k:])
	copy(newNums[k:], nums[:nlen-k])
	copy(nums, newNums)
}
