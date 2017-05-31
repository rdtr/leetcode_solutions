package main

func mySqrt(x int) int {
	if x == 0 {
		return 0
	}
	start, end := 1, x
	for {
		mid := (start + end) / 2
		if p := mid * mid; p > x {
			end = mid
		} else if p < x {
			start = mid
		} else {
			return mid
		}

		if start == end {
			return start
		} else if start+1 == end {
			if end*end < x {
				return end
			}
			return start
		}
	}
}
