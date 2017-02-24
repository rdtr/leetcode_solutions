package main

func searchRange(nums []int, target int) []int {
	nlen := len(nums)
	if nlen == 0 {
		return []int{-1, -1}
	} else if nlen == 1 {
		if target == nums[0] {
			return []int{0, 0}
		} else {
			return []int{-1, -1}
		}
	}

	left, right := searchLeft(nums, target), searchRight(nums, target)
	if left == -1 && right == -1 {
		return []int{-1, -1}
	}
	return []int{left, right}
}

func searchLeft(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for right-left > 1 {
		mid := (left + right) / 2
		if nums[mid] < target && nums[mid+1] == target {
			return mid + 1
		} else if nums[mid] < target {
			left = mid
		} else {
			right = mid
		}
	}

	if nums[left] == target {
		return left
	}
	if nums[right] == target {
		return right
	}
	return -1
}

func searchRight(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for right-left > 1 {
		mid := (left + right) / 2
		if nums[mid+1] > target && nums[mid] == target {
			return mid
		} else if nums[mid] <= target {
			left = mid
		} else {
			right = mid
		}
	}

	if nums[right] == target {
		return right
	}
	if nums[left] == target {
		return left
	}
	return -1
}
