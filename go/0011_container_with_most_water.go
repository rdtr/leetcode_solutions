package main

func maxArea(height []int) int {
	w, max := 0, 0
	left, right := 0, len(height)-1
	for left < right {
		if hl, hr, dist := height[left], height[right], right-left; hl > hr {
			w = dist * hr
			right--
		} else {
			w = dist * hl
			left++
		}

		if w > max {
			max = w
		}
	}
	return max
}
