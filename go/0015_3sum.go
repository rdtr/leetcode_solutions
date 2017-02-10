package main

import "sort"

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	numslen := len(nums)

	var res [][]int
	for i := 0; i < numslen-2; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}
		target := 0 - nums[i]
		for start, end := i+1, numslen-1; start < end; {
			twoSum := nums[start] + nums[end]
			if twoSum == target {
				res = append(res, []int{nums[i], nums[start], nums[end]})
				for start < end && nums[start+1] == nums[start] {
					start++
				}
				for start < end && nums[end-1] == nums[end] {
					end--
				}
				start++
				end--
			} else if twoSum < target {
				for start < end && nums[start+1] == nums[start] {
					start++
				}
				start++
			} else {
				for start < end && nums[end-1] == nums[end] {
					end--
				}
				end--
			}
		}
	}
	return res
}
