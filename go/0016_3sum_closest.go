package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	nlen := len(nums)

	curClosest := math.MaxInt32
	for i := 0; i < nlen-2; i++ {
		if i != 0 && nums[i-1] == nums[i] {
			continue
		}

		start, end := i+1, nlen-1
		for start < end {
			if threeSum := nums[i] + nums[start] + nums[end]; threeSum == target {
				return threeSum
			} else if threeSum < target {
				if abs(threeSum-target) < abs(curClosest-target) {
					curClosest = threeSum
				}
				for start < end && nums[start] == nums[start+1] {
					start++
				}
				start++
			} else {
				if abs(threeSum-target) < abs(curClosest-target) {
					curClosest = threeSum
				}
				for start < end && nums[end] == nums[end-1] {
					end--
				}
				end--
			}
		}
	}
	return curClosest
}

func abs(i int) int {
	if i < 0 {
		return -1 * i
	}
	return i
}
