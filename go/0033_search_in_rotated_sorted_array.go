package main

func search(nums []int, target int) int {
	nlen := len(nums)
	if nlen == 0 {
		return -1
	}

	left, right := 0, nlen-1
	for left < right {
		mid := (left + right) / 2
		// found case
		if nums[mid] == target {
			return mid
		}

		// nums[mid:right] is not rotated
		if nums[mid] < nums[right] {
			if nums[mid] > target {
				right = mid - 1
				continue
			}

			if target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
			continue
		}
		// nums[left:mid] is not rotated
		if target > nums[mid] {
			left = mid + 1
			continue
		}

		if nums[left] <= target {
			right = mid - 1
		} else {
			left = mid + 1
		}

	}

	if left == right && target == nums[left] {
		return left
	}
	return -1
}
