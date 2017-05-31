func fourSumCount(A []int, B []int, C []int, D []int) int {
	var res, sum int

	abSum := make(map[int]int)
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(B); j++ {
			sum = A[i] + B[j]
			if count, ok := abSum[sum]; !ok {
				abSum[sum] = 1
			} else {
				abSum[sum] = count + 1
			}
		}
	}

	for i, sum := 0, 0; i < len(C); i++ {
		for j := 0; j < len(D); j++ {
			sum = C[i] + D[j]
			if count, ok := abSum[-sum]; ok {
				res += count
			}
		}
	}
	return res
}