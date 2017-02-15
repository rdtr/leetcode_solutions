package main

func searchInsert(nums []int, target int) int {
	nlen := len(nums)

	left, right := 0, nlen-1
	for right-left > 0 {
		mid := (left + right) / 2
		if target < nums[mid] {
			right = mid - 1
		} else if target > nums[mid] {
			left = mid + 1
		} else {
			return mid
		}
	}

	if target <= nums[left] {
		return left
	}
	return left + 1
}
