func findMin(nums []int) int {
	start, end := 0, len(nums)-1
	mid := start + (end-start)/2
	if nums[start] < nums[mid] && nums[mid] < nums[end] { // not rotated
		return nums[start]
	}

	for start <= end {
		if start == end {
			return nums[start]
		} else if start+1 == end {
			return min(nums[start], nums[end])
		}

		mid = start + (end-start)/2
		if nums[mid] < nums[end] { // right side is rotated
			end = mid
		}
		if nums[start] < nums[mid] { // left side is rotated
			start = mid
		}
	}
	return 0 // never reaches here
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}