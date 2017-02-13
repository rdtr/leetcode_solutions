package main

func isPerfectSquare(num int) bool {
	if num == 1 {
		return true
	}

	start, end := 0, num
	var mid int
	for start <= end {
		mid = (start + end + 1) / 2
		if p := mid * mid; p == num {
			return true
		} else if p > num {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return false
}
