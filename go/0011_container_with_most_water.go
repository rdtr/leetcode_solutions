package main

func maxArea(height []int) int {
	res := 0
	for l, r := 0, len(height)-1; l < r; {
		if tmp := (r - l) * min(height[r], height[l]); tmp > res {
			res = tmp
		}

		if height[r] >= height[l] {
			l++
		} else {
			r--
		}
	}
	return res
}

func min(a, b int) int {
	if a >= b {
		return b
	}
	return a
}
