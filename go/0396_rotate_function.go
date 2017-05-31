func maxRotateFunction(A []int) int {
	if len(A) == 0 {
		return 0
	}

	max := 0
	digitSum := 0
	for i, num := range A {
		max += i * num
		digitSum += num
	}

	curMax := max
	if len(A) > 1 {
		for i := len(A) - 1; i >= 1; i-- {
			newMax := curMax - (len(A)-1)*A[i] + (digitSum - A[i])
			if newMax > max {
				max = newMax
			}
			curMax = newMax
		}
	}
	return max
}