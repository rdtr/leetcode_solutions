func smallestRangeI(A []int, K int) int {
	alen := len(A)
	if alen == 0 {
		return 0
	}

	max, min := A[0], A[0]
	for i := 1; i < alen; i++ {
		if max < A[i] {
			max = A[i]
		}
		if min > A[i] {
			min = A[i]
		}
	}

	diff := abs(max-min) - 2*K
	if diff < 0 {
		return 0
	}
	return diff
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}