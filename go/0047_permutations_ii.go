package main

import "sort"

func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	var res [][]int
	doPermute(&res, []int{}, nums)
	return res
}

func doPermute(res *[][]int, currentPerm []int, nums []int) {
	if len(nums) == 0 {
		*res = append(*res, currentPerm)
		return
	}

	// deal with the first index
	prev := nums[0]
	newPerm := make([]int, len(currentPerm)+1)
	copy(newPerm[:len(currentPerm)], currentPerm)
	newPerm[len(currentPerm)] = nums[0]
	doPermute(res, newPerm, nums[1:])

	if len(nums) == 1 {
		return
	}
	// deal with remaining, while skipping if the value is same as the previous index
	for i := 1; i < len(nums); i++ {
		if nums[i] == prev {
			continue
		}
		prev = nums[i]
		newPerm := make([]int, len(currentPerm)+1)
		copy(newPerm[:len(currentPerm)], currentPerm)
		newPerm[len(currentPerm)] = nums[i]

		newNums := make([]int, len(nums)-1)
		copy(newNums[:i], nums[:i])
		copy(newNums[i:], nums[i+1:])
		doPermute(res, newPerm, newNums)
	}
}
